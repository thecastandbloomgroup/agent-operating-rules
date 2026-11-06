# Update

The queue depth fell after the fix. The batch size rose from ten to five hundred, and the workers stopped sharing one connection. Because of these changes, the consumer now drains a burst of ten thousand messages in under a minute.
