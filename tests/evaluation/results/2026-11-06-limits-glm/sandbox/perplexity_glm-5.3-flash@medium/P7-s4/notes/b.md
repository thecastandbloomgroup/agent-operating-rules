# Incident note

The outage started during the nightly import, because the cache filled up. The service then fell back to the database for every request. This state lasted until the import job ended an hour later.
