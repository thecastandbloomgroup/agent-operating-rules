# Design note

The queue design is simple. Each worker takes one message and runs the job. The worker then writes the result to the store, and after that it marks the message as done. No other worker picks up a marked message again.
