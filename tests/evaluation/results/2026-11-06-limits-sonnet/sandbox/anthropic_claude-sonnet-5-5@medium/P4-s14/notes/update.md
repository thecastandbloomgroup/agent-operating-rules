# Update

The queue depth fell after the fix. The consumer now drains a burst of ten thousand messages in under a minute. This change has two causes. First, the batch size rose from ten to five hundred. Second, the workers no longer share one connection.
