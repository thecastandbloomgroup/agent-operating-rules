# Incident note

The outage started when the cache filled during the nightly import. The service then sent every request to the database. This pattern continued until the import job ended one hour later.
