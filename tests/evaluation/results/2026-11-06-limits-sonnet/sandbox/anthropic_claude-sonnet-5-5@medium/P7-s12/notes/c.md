# Design note

The queue is simple. Each worker takes one message and runs the job. Then it writes the result to the store. Last, it marks the message as done. No other worker then picks up that message again.
