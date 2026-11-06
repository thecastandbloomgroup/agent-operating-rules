# Update

The queue depth fell by a large margin after the fix. The batch size rose from ten to five hundred. The workers no longer share one connection. Because of both changes, the consumer now drains a burst of ten thousand messages in under a minute.
