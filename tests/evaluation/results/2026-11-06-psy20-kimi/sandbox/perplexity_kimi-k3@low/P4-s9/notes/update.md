# Update

Queue depth fell after the fix. The consumer now drains a burst of ten thousand messages in under a minute. This is because batch size rose from ten to five hundred. Also, workers no longer share one connection.
