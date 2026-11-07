# Design note

The queue is simple. Each worker takes one message and runs the job. The worker writes the result to the store and marks the message as done, so no other worker picks it up again.
