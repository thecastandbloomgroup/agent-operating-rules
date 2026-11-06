# Design note

Each worker takes one message from the queue. The worker runs the job and writes the result to the store. Then it marks the message as done. No other worker picks the message up again.
