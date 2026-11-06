# Design note

The queue is simple. Each worker runs the job, then writes the result to the store and marks the message as done. No other worker picks the message up again.
