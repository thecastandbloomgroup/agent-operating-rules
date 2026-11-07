# Design note

The queue is simple. Each worker takes one message and runs the job. Then the worker writes the result to the store. Finally it marks the message as done. No other worker picks it up again.
