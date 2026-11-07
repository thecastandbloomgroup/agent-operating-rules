# Design note

The queue is simple. Each worker takes one message and runs the job. The worker writes the result to the store. It then marks the message as done. No other worker picks the message up again.
