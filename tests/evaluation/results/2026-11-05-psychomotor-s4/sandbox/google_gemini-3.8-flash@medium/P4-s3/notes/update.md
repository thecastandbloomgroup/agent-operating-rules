# Update

The queue depth dropped by 90% after the fix.
The consumer now drains a burst of 10,000 messages in under one minute.
This improvement occurred because the batch size rose from 10 to 500 messages.
In addition, the workers no longer share one connection.
