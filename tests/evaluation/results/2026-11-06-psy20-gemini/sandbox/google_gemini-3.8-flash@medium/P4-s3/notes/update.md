# Update

Queue depth fell after the fix. The consumer now drains ten thousand messages in under one minute. This speedup happened because the batch size rose from 10 to 500. Furthermore, workers no longer share one connection.
