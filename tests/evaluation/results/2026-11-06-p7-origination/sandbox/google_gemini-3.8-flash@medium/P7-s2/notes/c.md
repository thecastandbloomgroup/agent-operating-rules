# Design note

The queue is simple. Each worker takes one message and runs the job. Next, it writes the result to the store. The worker then marks the message as done so that no other worker picks it up again.
