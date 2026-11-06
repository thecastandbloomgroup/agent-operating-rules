# Update

The queue depth dropped by 80 percent after the fix. The consumer now drains a burst of 10,000 messages in under one minute. This occurs because the batch size rose from ten to 500. Furthermore, the workers no longer share one connection.
