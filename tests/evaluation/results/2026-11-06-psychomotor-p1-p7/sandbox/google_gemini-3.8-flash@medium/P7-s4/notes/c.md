# Design note

The queue design is simple. Each worker takes one message and runs the job. Next, it writes the result to the store. Finally, it marks the message as complete so that other workers do not process it again.
