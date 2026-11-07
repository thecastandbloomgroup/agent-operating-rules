# Design note

The queue design remains simple. Each worker takes one message and runs the job. Next, it writes the result to the store. Finally, it marks the message as done so no other worker picks it up.
