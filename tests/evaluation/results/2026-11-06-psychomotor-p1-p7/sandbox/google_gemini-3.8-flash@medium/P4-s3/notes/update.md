# Update

The queue depth dropped after the fix. The batch size rose from ten to five hundred. Also, the workers no longer share one connection. Therefore, the consumer now drains a burst of ten thousand messages in under one minute.
