# Update

The queue depth fell after the fix. The consumer now drains a burst of ten thousand messages in under a minute. The causes are two: the batch size rose from ten to five hundred, and the workers no longer share one connection.
