# Procedure: repair one notes file

1. Read the target file with `functions.read_file`.
2. Record its facts, limits, requests, and links before any edit.
3. Run `functions.check_file` on the target file.
4. Review each banned word and each sentence that exceeds 25 words in the report.
5. Replace banned words with plain terms that preserve the original claim and its strength.
6. Split long sentences into shorter sentences, with a target of 20 words or fewer each.
7. Preserve facts, names, numbers, conditions, uncertainty, links, and the order of dependent steps.
8. Compare the proposed text with the original text before the write.
9. Write the complete revised file with `functions.write_file`.
10. Run `functions.check_file` on the revised file.
11. If the report lists any banned words or long sentences, repeat steps 4 through 10.
12. Read the revised file and compare its meaning with the original text from step 1.
13. If meaning differs, repair the text and repeat steps 9 through 12.
14. Finish only when the check reports no banned words or long sentences and the meaning remains intact.
15. Complete one target file before you start the next file in the requested order.
