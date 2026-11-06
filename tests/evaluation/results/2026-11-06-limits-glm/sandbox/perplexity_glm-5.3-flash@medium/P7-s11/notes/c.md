# Design note

The queue is simple. Each worker takes one message and runs the job. It then writes the result to the store. It marks the message as done, so no other worker picks it up again.
