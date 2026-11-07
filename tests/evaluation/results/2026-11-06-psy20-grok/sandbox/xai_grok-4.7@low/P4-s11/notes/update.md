# Update

The queue depth fell by a large margin after the fix. The consumer now drains a burst of ten thousand messages in under a minute. Two changes cause this result. First, the batch size rose from ten to five hundred. Second, the workers no longer share one connection.
