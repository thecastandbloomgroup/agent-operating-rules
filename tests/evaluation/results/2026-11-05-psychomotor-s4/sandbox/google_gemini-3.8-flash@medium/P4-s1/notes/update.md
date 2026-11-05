# Update

The queue depth fell sharply after the fix. The consumer now drains a burst of 10,000 messages in under a minute. This happens because the batch size rose from 10 to 500. Furthermore, the workers no longer share one connection.
