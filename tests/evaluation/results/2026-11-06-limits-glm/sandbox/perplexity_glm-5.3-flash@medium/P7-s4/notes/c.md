# Design note

The queue serves one purpose: each worker processes one message at a time. The worker runs the job, writes the result to the store, and then marks the message as done. So no other worker picks it up again.
