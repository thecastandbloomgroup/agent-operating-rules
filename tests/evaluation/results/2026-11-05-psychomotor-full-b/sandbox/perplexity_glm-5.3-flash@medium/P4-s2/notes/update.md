# Update

The queue depth fell to a small fraction of its old size after the fix. The consumer now drains a burst of ten thousand messages in under a minute. This is possible because the batch size rose from ten to five hundred. The workers also no longer share one connection.
