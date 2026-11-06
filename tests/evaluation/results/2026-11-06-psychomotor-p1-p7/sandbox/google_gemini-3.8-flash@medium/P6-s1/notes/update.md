# Update

The queue depth dropped steeply after the fix. The consumer now drains a burst of ten thousand messages in under one minute. This change happened because the batch size rose from ten to five hundred. In addition, the workers no longer share one connection.
