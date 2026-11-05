# Update

The fix led to a large drop in queue depth. The batch size rose from ten to five hundred. The workers no longer share one connection. These changes let the consumer drain a burst of ten thousand messages in under a minute.
