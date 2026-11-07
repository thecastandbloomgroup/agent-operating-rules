# Update

The queue depth dropped after the fix. The consumer now drains a burst of 10,000 messages in under one minute. This speed improvement occurred because the batch size rose from 10 to 500. In addition, workers no longer share one connection.
