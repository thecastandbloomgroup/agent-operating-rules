# Update

The queue depth fell after the fix. The batch size rose from 10 to 500 messages. Furthermore, the workers no longer share one connection. Therefore, the consumer now drains a burst of 10,000 messages in under one minute.
