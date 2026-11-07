# Update

The queue depth dropped after the fix. The consumer now drains a burst of 10,000 messages in under one minute. This change happened because the batch size rose from 10 to 500. Furthermore, the workers no longer share one connection.
