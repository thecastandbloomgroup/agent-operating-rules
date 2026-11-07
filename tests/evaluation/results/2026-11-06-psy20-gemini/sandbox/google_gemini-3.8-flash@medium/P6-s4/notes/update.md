# Update

The queue depth fell after the fix. The consumer drains a burst of ten thousand messages in under one minute. This improvement occurs because the batch size rose from ten to five hundred. In addition, workers no longer share one connection.
