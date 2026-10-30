"""Order status service: a small HTTP API over the orders database."""

import json
import os
import sqlite3
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

DB_PATH = os.environ.get("ORDERS_DB", "orders.db")
PORT = int(os.environ.get("PORT", "8080"))
SLOW_MS = 500


def connect():
    print("opening database", DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn):
    print("checking schema")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS orders ("
        "id INTEGER PRIMARY KEY, customer TEXT, status TEXT, total REAL, updated REAL)"
    )
    conn.commit()
    print("schema ok")


def get_order(conn, order_id):
    row = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
    if row is None:
        print("order not found:", order_id)
        return None
    return dict(row)


def list_orders(conn, customer):
    rows = conn.execute(
        "SELECT * FROM orders WHERE customer = ? ORDER BY updated DESC", (customer,)
    ).fetchall()
    print("listed", len(rows), "orders for", customer)
    return [dict(r) for r in rows]


def update_status(conn, order_id, status):
    allowed = {"new", "paid", "shipped", "cancelled"}
    if status not in allowed:
        print("WARNING: bad status", status, "for order", order_id)
        return False
    conn.execute(
        "UPDATE orders SET status = ?, updated = ? WHERE id = ?",
        (status, time.time(), order_id),
    )
    conn.commit()
    print("order", order_id, "is now", status)
    return True


class Handler(BaseHTTPRequestHandler):
    conn = None

    def send_json(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        started = time.monotonic()
        parts = self.path.strip("/").split("/")
        try:
            if len(parts) == 2 and parts[0] == "orders":
                order = get_order(self.conn, int(parts[1]))
                if order is None:
                    self.send_json(404, {"error": "not found"})
                else:
                    self.send_json(200, order)
            elif len(parts) == 2 and parts[0] == "customers":
                self.send_json(200, list_orders(self.conn, parts[1]))
            else:
                self.send_json(404, {"error": "no route"})
        except Exception as error:
            print("ERROR in GET", self.path, error, file=sys.stderr)
            self.send_json(500, {"error": "internal"})
        elapsed = (time.monotonic() - started) * 1000
        if elapsed > SLOW_MS:
            print("slow request:", self.path, round(elapsed), "ms")

    def do_POST(self):
        parts = self.path.strip("/").split("/")
        length = int(self.headers.get("Content-Length", "0"))
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            print("bad JSON from", self.client_address[0])
            self.send_json(400, {"error": "bad json"})
            return
        if len(parts) == 3 and parts[0] == "orders" and parts[2] == "status":
            ok = update_status(self.conn, int(parts[1]), body.get("status", ""))
            self.send_json(200 if ok else 400, {"ok": ok})
        else:
            self.send_json(404, {"error": "no route"})

    def log_message(self, format, *args):
        print("request:", self.address_string(), format % args)


def main():
    print("starting order service on port", PORT)
    conn = connect()
    init_db(conn)
    Handler.conn = conn
    server = HTTPServer(("", PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("stopping")
    finally:
        conn.close()
        print("database closed")


if __name__ == "__main__":
    main()
