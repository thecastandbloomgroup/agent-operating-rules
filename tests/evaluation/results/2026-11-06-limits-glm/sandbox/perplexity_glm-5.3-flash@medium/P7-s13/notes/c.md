# Design note

The queue is simple. Each worker takes one message, runs the job, and writes the result to the store. Then it marks the message as done, so no other worker picks it up again.
