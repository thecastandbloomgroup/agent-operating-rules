# Update

The fix led to a large drop in queue depth. The consumer now drains a burst of ten thousand messages in under a minute. Two changes caused this gain. The batch size rose from ten to five hundred. The workers no longer share one connection.
