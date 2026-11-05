# Update

The queue depth fell sharply after the fix. The consumer now drains a burst of ten thousand messages in under a minute. This is because the batch size rose from ten to five hundred. The workers also no longer share one connection.
