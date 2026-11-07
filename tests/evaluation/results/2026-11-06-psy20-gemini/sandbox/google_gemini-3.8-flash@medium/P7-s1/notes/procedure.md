# Procedure for Cleaning Notes Files

Follow these steps to clean a notes file:

1. Read the target file with the `read_file` tool to inspect its content.
2. Run the `check_file` tool on the target file path to identify violations.
3. Rewrite the text to remove banned words and shorten any sentence that exceeds twenty words.
4. Keep the original meaning and preserve factual details.
5. Save the updated text to the file path with the `write_file` tool.
6. Run the `check_file` tool again to verify that zero failures remain.
