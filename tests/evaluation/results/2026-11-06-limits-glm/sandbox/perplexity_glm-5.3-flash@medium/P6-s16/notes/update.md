# Update

Queue depth fell from a high value to near zero after the fix [judgment]. The consumer now drains a burst of ten thousand messages in under a minute. The gain came from two changes. The batch size rose from ten to five hundred. Also, the workers no longer share one connection.
