# Update

The queue depth dropped after the fix.
The consumer now drains a burst of ten thousand messages in under a minute.
This improvement occurred because the batch size rose from ten to five hundred.
In addition, the workers no longer share one connection.
