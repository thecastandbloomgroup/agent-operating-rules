# Update

The queue depth dropped after the fix.
The consumer now drains a burst of ten thousand messages in under one minute.
This happened because the batch size rose from ten to five hundred messages.
In addition, the workers no longer share one connection.
