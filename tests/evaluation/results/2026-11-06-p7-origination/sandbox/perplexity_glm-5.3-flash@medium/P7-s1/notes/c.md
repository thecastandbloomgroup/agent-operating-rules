# Design note

The queue is simple. Each worker takes one message and runs the job. It writes the result to the store and marks the message as done. Because the message is marked done, no other worker picks it up again.
