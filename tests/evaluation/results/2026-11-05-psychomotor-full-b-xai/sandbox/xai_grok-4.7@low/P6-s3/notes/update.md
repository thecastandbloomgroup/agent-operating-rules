# Update

The queue depth fell after the fix. The consumer now drains a burst of ten thousand messages in under a minute. This happens because the batch size rose from ten to five hundred. The workers no longer share one connection.
