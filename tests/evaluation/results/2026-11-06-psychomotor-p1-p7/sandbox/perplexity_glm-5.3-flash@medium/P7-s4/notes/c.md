# Design note

The queue is simple. Each worker takes one message, runs the job, and writes the result to the store. It then marks the message as done, so no other worker picks it up again.
