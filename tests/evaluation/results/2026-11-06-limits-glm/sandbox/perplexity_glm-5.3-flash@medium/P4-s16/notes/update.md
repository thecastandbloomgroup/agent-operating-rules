# Update

The queue depth fell after the fix. The consumer now drains a burst of ten thousand messages in under a minute. The batch size rose from ten to five hundred. The workers also no longer share one connection. Therefore, faster batches and separate connections explain the drop.
