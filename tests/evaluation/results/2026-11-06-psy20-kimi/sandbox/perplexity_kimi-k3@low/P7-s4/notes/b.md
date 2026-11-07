# Incident note

The outage started when the cache filled up during the nightly import. The service fell back to the database for every request. It stayed that way until the import job ended an hour later.
