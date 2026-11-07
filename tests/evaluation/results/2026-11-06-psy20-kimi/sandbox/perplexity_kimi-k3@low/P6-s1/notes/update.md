# Update

The queue depth fell from a large value to near zero after the fix. The consumer now drains a burst of ten thousand messages in under a minute. This is because the batch size rose from ten to five hundred. Also, the workers no longer share one connection.
