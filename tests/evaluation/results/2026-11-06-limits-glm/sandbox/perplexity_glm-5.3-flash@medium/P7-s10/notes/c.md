# Design note

The queue is simple. Each worker takes one message and runs the job. Then it writes the result to the store and marks the message as done. Therefore no other worker picks the message up again.
