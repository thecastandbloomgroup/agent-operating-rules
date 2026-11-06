# Design note

The queue is simple. Each worker takes one message and runs the job. The worker writes the result to the store, then marks the message as done. This prevents other workers from taking that message again.
