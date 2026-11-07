# Update

The queue depth fell after the fix. The batch size rose from ten to five hundred, and the workers no longer share one connection. As a result, the consumer now drains a burst of ten thousand messages in under a minute.
