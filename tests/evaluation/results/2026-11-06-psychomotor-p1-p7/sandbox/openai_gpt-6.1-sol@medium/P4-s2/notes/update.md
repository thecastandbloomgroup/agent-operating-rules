# Update

The fix led to a large drop in queue depth. The consumer now drains a burst of ten thousand messages in under a minute. Two changes explain this: the batch size rose from ten to five hundred, and the workers no longer share one connection.
