# Incident note

The outage started when the cache filled during the nightly import. The service fell back to the database for every request. The issue ended when the import job completed an hour later.
