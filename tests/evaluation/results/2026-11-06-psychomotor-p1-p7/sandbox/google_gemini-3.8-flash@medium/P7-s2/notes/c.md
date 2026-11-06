# Design note

The queue design is simple. Each worker takes one message, runs the job, and writes the result to the store. The worker then marks the message as done. Therefore, no other worker picks up the message again.
