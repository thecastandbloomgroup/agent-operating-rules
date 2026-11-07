# Procedure to Fix Notes Files

Follow these steps to fix banned words and long sentences in one notes file:

1. Run check_file on the target file path to identify violations.
2. Read the target file content with read_file.
3. Remove or replace banned words identified by check_file while preserving meaning.
4. Split any sentences exceeding 25 words into shorter sentences.
5. Write the revised content back to the target file path with write_file.
6. Run check_file on the target file path to verify zero failures remain.
