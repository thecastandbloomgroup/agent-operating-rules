# Update

The queue depth fell after the fix. The consumer drains a burst of ten thousand messages in under one minute. This occurs because the batch size rose from ten to five hundred messages. In addition, workers no longer share one connection.
