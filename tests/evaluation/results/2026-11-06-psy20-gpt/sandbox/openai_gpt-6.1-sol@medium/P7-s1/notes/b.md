# Incident note

The outage started when the cache reached capacity during the nightly import. The service then used the database for every request until the import job ended an hour later.
