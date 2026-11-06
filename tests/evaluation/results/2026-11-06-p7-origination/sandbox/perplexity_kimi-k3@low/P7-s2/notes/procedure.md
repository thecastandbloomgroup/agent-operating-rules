# Procedure: fix one notes file

1. Read the notes file with the read_file tool.
2. Run check_file on the file path.
3. Note the banned words it reports.
4. Note the sentences over 25 words it reports.
5. Replace each banned word with a neutral word or remove it. Keep the meaning.
6. Split each long sentence into two or more short sentences. Keep the meaning.
7. Write the revised text back to the same file with write_file.
8. Run check_file on the file again.
9. If check_file still reports problems, repeat steps 5 to 8. If it reports none, stop.
