# Update

The queue depth fell by a large amount after the fix. The consumer now drains a burst of ten thousand messages in under a minute. Two changes enable this: the batch size rose from ten to five hundred, and the workers no longer share one connection.
