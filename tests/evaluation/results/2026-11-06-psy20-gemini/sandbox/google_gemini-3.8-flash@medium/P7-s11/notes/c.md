# Design note

The queue design is simple. Each worker takes one message and runs the job. The worker writes the result to the store. Then it marks the message as done. Therefore, no other worker picks it up again.
