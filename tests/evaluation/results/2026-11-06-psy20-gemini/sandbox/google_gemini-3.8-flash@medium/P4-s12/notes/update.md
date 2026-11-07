# Update

Queue depth dropped after the fix. The consumer now drains a burst of ten thousand messages in under one minute. This speedup happened because the batch size rose from ten to five hundred messages. Furthermore, workers no longer share one connection.
