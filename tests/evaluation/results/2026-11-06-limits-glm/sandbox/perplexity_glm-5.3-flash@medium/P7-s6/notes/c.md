# Design note

The queue is simple. Each worker takes one message and runs the job. It writes the result to the store and then marks the message as done. This stops another worker from picking up the same message again.
