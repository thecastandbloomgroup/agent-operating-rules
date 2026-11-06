# Update

The queue depth fell by a large margin after the fix. The note gives no number for the drop, so this stays a qualitative claim.

The consumer now drains a burst of ten thousand messages in under a minute. Two changes produced this result: the batch size rose from ten to five hundred, and the workers no longer share one connection.
