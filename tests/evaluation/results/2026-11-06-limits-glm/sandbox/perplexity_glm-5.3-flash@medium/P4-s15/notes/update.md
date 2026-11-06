# Update

The queue depth fell after the fix. The consumer now drains a burst of ten thousand messages in under a minute. The batch size rose from ten to five hundred, so each drain cycle moves far more data. The workers also stopped sharing one connection, and this raised the throughput again.
