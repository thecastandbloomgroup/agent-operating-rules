# Human marking sheet

Run `task marking` and open <http://localhost:5173> to mark the sheet in a web page. The page saves each answer to `sheet.csv`. The steps below are the same task by hand.

`sheet.csv` samples 24 judged actions for one blind marking session. The rows mix every judge disagreement of the judged runs with random agreements, shuffled, and the sheet shows no judge score.

For each row, open the response file of its run folder and read the named action. Fill two columns with True or False. The column domain_right_human asks whether the Cynefin label of the action fits the work. The column reason_cause_effect_human asks whether the reason states what effort it takes to know the effect. Use `note` for anything a judge misses.

After the fill, compare the marks with `action-checks.csv` and `action-checks-argon.csv` of each run. The agreement per column says how far each judge can be trusted, and it feeds the next judge instruction.

The sheet is complete. The [judge trust results](../2026-11-05-judge-trust-results.md) give the agreement of each judge with it.
