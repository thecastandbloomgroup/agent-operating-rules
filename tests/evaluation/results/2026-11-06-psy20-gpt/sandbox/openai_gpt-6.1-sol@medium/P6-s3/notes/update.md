# Update

The queue depth fell after the fix. The batch size rose from ten to five hundred, and the workers no longer share one connection. These changes now let the consumer drain a burst of ten thousand messages in under a minute.
