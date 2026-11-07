# Design note

The queue is simple. Each worker takes one message and runs the job. Then it writes the result to the store. Finally it marks the message as done. This way no other worker picks it up again.
