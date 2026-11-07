# Incident note

The outage started when the cache filled during the nightly import. The service fell back to the database for each request. This database load lasted until the import ended one hour later.
