# Update

The queue depth fell after the fix, from full to almost empty. The consumer now drains a burst of ten thousand messages in under a minute. This is because the batch size rose from ten to five hundred. Also, the workers no longer share one connection.
