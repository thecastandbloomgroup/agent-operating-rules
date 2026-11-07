# Design note

The queue is simple. Each worker takes one message. It runs the job and writes the result to the store. Then it marks the message as done. No other worker picks it up again.
