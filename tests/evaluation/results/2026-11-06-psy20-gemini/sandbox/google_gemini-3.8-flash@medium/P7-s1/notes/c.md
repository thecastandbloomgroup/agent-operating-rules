# Design note

The queue architecture is simple.
Each worker takes one message and runs the job.
The worker writes the result to the store.
Then the worker marks the message as done.
This sequence prevents other workers from taking the message again.
