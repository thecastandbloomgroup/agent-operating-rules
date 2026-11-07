# Update

The queue depth fell by a large amount after the fix. The consumer now drains a burst of ten thousand messages in under a minute because of two changes. The batch size rose from ten to five hundred. The workers no longer share one connection.
