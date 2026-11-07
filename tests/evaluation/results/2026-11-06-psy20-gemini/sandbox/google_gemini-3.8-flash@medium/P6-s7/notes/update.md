# Update

The queue depth fell after the fix. The consumer drains a burst of 10,000 messages in under one minute. This occurs because the batch size rose from 10 to 500 messages. In addition, workers no longer share one connection.
