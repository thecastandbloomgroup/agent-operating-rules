# Incident note

The outage started when the cache filled up during the nightly import. The service then fell back to the database for every request. This state lasted until the import job ended an hour later.
