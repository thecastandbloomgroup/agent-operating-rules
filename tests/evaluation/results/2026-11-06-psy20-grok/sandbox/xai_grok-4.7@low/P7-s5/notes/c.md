# Design note

The queue is simple. Each worker takes one message and runs the job. It writes the result to the store. It then marks the message as done so no other worker takes it again.
