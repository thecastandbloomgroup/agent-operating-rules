# Design note

The queue design is simple. Each worker takes one message and runs the job. Next, it writes the result to the store. It then marks the message as done. Therefore, no other worker picks up the message again.
