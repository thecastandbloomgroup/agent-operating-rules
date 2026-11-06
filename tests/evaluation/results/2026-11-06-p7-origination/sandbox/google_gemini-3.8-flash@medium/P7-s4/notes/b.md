# Incident note

The outage started when the cache filled up during the nightly import. The service fell back to the database for every request. This load continued until the import job ended an hour later.
