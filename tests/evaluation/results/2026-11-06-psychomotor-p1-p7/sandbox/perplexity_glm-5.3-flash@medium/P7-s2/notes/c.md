# Design note

The queue is simple. Each worker takes one message and runs the job. It writes the result to the store and marks the message as done. No other worker then picks it up again.
