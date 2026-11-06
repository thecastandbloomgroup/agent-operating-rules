# Design note

The queue takes work in simple order. Each worker performs these steps. It takes one message. It runs the job. It writes the result to the store. It marks the message as done. Then no other worker picks it up again.