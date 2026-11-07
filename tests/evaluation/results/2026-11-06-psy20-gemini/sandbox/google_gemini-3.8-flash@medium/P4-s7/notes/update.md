# Update

The queue depth dropped sharply after the fix. The batch size rose from ten to five hundred. In addition, workers no longer share one connection. Therefore, the consumer now drains a burst of ten thousand messages in under a minute.
