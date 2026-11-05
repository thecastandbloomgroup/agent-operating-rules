# Update

The queue depth fell by a large amount after the fix. The consumer now drains a burst of ten thousand messages in under one minute. This drain is faster because the batch size rose from ten to five hundred. It is also faster because the workers no longer share one connection.
