# Design note

The queue is simple. Each worker takes one message and runs the job. The worker writes the result to the store. The worker then marks the message as done. No other worker takes that message again.
