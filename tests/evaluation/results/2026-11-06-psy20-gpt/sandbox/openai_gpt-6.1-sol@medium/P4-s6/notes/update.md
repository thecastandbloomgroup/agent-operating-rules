# Update

The queue depth fell after the fix. The consumer now drains a burst of ten thousand messages in under a minute because of two changes. The batch size rose from ten to five hundred. Also, the workers no longer share one connection.
