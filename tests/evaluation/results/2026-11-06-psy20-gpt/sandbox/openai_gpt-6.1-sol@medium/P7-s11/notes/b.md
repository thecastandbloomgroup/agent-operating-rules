# Incident note

The outage started when the cache filled during the nightly import. The service then used the database for every request until the import job ended an hour later.
