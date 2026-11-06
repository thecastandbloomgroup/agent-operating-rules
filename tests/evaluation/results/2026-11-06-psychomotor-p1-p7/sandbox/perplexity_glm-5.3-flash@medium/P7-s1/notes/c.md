# Design note

The queue is simple. Each worker takes one message and runs the job. The worker then writes the result to the store and marks the message as done. No other worker picks up the message again.
