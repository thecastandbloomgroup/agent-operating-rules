# Design note

The queue design is simple. Each worker takes one message, runs the job, and writes the result to the store. Then the worker marks the message as done. This step prevents duplicate processing.
