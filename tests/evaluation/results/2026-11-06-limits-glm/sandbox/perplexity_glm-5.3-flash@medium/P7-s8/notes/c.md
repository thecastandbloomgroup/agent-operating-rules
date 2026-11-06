# Design note

The queue is simple. Each worker takes one message, runs the job, writes the result to the store, and then marks the message as done. Then no other worker picks it up again.
