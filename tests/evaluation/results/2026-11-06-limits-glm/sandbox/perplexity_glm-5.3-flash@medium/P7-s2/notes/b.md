# Incident note

The cache filled up during the nightly import. The service then fell back to the
database for every request. This fallback lasted until the import job ended, an
hour later. The outage covered that whole period.
