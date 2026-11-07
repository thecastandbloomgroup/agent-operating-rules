# Update

The queue depth fell a lot after the fix. The batch size rose from ten to five hundred. The workers no longer share one connection. Because of this, the consumer now drains a burst of ten thousand messages in under a minute.
