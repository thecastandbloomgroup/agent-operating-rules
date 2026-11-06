# Update

The queue depth fell after the fix, and the drop was large. The consumer now drains a burst of ten thousand messages in under a minute. Two changes made this possible. First, the batch size rose from ten to five hundred. Second, the workers no longer share one connection.
