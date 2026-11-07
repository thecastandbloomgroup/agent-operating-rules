# Update

The queue depth fell after the fix. The consumer now drains a burst of 10,000 messages in under a minute. This speedup happened because the batch size rose from 10 to 500. In addition, the workers no longer share one connection.
