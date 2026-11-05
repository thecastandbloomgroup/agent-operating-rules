# Update

The queue depth dropped by a large margin after the fix. The consumer now drains a burst of ten thousand messages in under one minute. This result happened because the batch size rose from ten to five hundred. In addition, the workers no longer share one connection.
