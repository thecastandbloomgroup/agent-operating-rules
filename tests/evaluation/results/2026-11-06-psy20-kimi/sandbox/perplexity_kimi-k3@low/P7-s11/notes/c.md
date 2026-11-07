# Design note

The queue is simple. Each worker takes one message. It runs the job. It writes the result to the store. Then it marks the message as done. This means no other worker picks it up again.
