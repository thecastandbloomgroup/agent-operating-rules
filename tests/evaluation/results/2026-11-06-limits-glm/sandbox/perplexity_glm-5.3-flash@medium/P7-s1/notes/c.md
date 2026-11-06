# Design note

The queue is simple. Each worker takes one message and runs the job. Then it writes the result to the store and marks the message as done. So no other worker picks it up again.
