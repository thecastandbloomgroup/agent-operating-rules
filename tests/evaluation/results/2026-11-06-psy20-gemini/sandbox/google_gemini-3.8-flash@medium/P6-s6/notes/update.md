# Update

The queue depth fell after the fix. The consumer drains a burst of ten thousand messages in under one minute. This improvement happened because the batch size rose from ten to five hundred. In addition, the workers no longer share one connection.
