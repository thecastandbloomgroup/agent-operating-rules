# Design note

The queue is a simple design. Each worker runs one job. It takes one message,
runs the job, writes the result to the store, and then marks the message as
done. No other worker picks up a message that is marked as done.
