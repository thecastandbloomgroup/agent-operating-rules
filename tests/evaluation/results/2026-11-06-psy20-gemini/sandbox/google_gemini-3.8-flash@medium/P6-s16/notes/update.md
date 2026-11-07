# Update

The queue depth fell after the fix. The consumer now drains a burst of 10,000 messages in under one minute. This change occurred because the batch size rose from 10 to 500 messages. In addition, the workers no longer share one connection.
