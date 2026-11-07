# Incident note

The outage started when the cache filled up during the nightly import. The service then used the database for every request. This lasted until the import job ended an hour later.
