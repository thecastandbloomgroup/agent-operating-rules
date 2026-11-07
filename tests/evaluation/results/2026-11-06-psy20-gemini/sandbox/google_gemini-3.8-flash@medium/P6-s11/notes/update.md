# Update

The queue depth fell after the fix. The consumer now drains ten thousand messages in under one minute. This improvement happened because the batch size rose from 10 to 500. In addition, the workers no longer share one connection.
