# Incident note

The cache filled up during the nightly import. The service then fell back to the database for every request. The fallback ran until the import job ended one hour later.
