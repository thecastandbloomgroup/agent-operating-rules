# Design note

Each worker takes one message, runs the job, and writes the result to the store. Then the worker marks the message as done so that no other worker picks it up again.
