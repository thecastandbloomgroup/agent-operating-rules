# Procedure to fix one notes file

1. Read the target file with read_file.
2. Run check_file on the path.
3. From the report, collect each banned word and each sentence over 25 words.
4. Replace each banned word. Remove it when the claim carries a number or measurement. Keep the meaning.
5. Split each long sentence into two or more sentences. Put one idea per sentence. Keep the original order of ideas.
6. Write the fixed content with write_file. Do not add information. Do not remove meaning.
7. Run check_file on the path again.
8. Repeat steps 3 to 6 until check_file reports no failures.
