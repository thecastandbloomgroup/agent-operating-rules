# Update

The fix reduced the queue depth. The consumer now drains a burst of ten thousand messages in under a minute. This is because the batch size rose from ten to five hundred, and the workers no longer share one connection.
