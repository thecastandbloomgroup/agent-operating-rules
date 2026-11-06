# Design note

The queue has a simple design. Each worker takes one message and runs the job. The worker writes the result to the store and marks the message as done. Therefore, no other worker picks up the same message.
