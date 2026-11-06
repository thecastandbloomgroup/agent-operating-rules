# Incident note

The service fell back to the database for every request. The cache filled up during the nightly import, so this state lasted an hour, until the import job ended.
