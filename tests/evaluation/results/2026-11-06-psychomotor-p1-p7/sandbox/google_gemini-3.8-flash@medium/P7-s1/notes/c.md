# Design note

The queue design uses a basic pattern. Each worker takes one message and runs the job. Next, it writes the result to the store. Finally, it marks the message as done so that no other worker picks it up again.
