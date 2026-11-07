# Design note

The queue is simple. Each worker takes one message and runs the job. It then writes the result to the store and marks the message as done. No other worker picks it up again.
