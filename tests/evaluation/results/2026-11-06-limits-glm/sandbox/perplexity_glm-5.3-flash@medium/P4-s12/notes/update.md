# Update

The queue depth fell after the fix. The queue depth fell because the batch size rose from ten to five hundred. The workers also stopped sharing one connection. Therefore, the consumer now drains a burst of ten thousand messages in under a minute.
