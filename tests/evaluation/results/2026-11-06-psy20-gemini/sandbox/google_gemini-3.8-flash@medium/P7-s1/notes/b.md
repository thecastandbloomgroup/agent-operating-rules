# Incident note

The outage started when the cache filled during the nightly import.
The service then queried the database for each request.
This condition lasted until the import ended one hour later.
