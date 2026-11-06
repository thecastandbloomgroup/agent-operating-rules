# Design note

The queue is simple. Each worker takes one message. The worker runs the job. It writes the result to the store. Then it marks the message as done. No other worker picks up a done message.
