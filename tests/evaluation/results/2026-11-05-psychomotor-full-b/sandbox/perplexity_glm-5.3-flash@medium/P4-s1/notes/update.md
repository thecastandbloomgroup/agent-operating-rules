# Update

The queue depth fell after the fix. The consumer now drains a burst of ten thousand messages in under a minute. The drain time improved because the batch size rose from ten to five hundred. In addition, the workers no longer share one connection.
