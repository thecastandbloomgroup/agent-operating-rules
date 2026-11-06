# Update

The queue depth dropped sharply after the fix. The consumer now drains a burst of ten thousand messages in under a minute. Therefore the fix worked through two changes. The batch size rose from ten to five hundred. The workers also no longer share one connection.
