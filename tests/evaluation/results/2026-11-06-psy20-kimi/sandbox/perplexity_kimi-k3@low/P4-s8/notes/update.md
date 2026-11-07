# Update

The queue depth fell by 80% after the fix. The consumer now drains a burst of ten thousand messages in under a minute. The batch size rose from ten to five hundred. The workers no longer share one connection.
