# Incident note

The outage started when the cache filled during the nightly import. The service fell back to the database for each request. This traffic lasted until the import job ended an hour later.
