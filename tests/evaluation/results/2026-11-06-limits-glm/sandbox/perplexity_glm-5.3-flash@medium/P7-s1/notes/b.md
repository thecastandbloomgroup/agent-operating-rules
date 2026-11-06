# Incident note

The outage started when the cache filled up during the nightly import. Then the service fell back to the database for every request. This went on until the import job ended an hour later.
