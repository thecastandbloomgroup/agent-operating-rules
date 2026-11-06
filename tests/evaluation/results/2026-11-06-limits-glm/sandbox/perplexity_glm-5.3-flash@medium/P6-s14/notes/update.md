# Update

The queue depth fell sharply after the fix. The consumer now drains a burst of ten thousand messages in under a minute. The reason is that the batch size rose from ten to five hundred. In addition, the workers no longer share one connection.
