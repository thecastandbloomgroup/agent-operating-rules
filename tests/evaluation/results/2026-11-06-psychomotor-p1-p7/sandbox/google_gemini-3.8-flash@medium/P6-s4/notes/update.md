# Update

The queue depth fell after the fix. The consumer now drains a burst of 10,000 messages in under one minute. This drop occurred because the batch size rose from 10 to 500. Furthermore, the workers no longer share one connection.
