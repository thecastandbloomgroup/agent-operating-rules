# Design note

The queue is simple. Each worker takes one message, runs the job, and writes the result to the store. The worker then marks the message as done so that no other worker takes it again.
