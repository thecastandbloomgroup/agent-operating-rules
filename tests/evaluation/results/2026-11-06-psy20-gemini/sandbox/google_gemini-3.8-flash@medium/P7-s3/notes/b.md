# Incident note

The outage started when the cache filled during the nightly import. Therefore, the service queried the database for every request. The issue stopped when the import ended one hour later.
