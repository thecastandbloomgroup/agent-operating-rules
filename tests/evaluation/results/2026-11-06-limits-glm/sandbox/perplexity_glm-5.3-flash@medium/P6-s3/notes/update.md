# Update

Queue depth fell after the fix. The consumer now drains a burst of ten thousand messages in under a minute. The batch size rose from ten to five hundred, and the workers no longer share one connection.
