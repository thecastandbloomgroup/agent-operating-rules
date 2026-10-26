# Standards used, by section

Each entry gives the what and why of a standard the rules file applies. Section numbers match the rules file.

## 0. Keywords and precedence

**What**: BCP 14 is the IETF convention for requirement words in standards. It defines MUST, SHOULD, MAY, and their negatives.

**Why**: it separates a hard rule from a preference and from a permission. A reader then knows which rules a response can fail.

## 1.5 Thematic analysis

**What**: thematic analysis groups qualitative data into themes, then checks each theme against the data. Braun and Clarke wrote the common method for psychology. In UX, Contextual Design groups notes from user interviews into an affinity diagram. Nielsen Norman Group teaches the method for user research. Its last step looks for data that does not support a theme.

**Why**: numbers have a test and a baseline, and statements need one too. A count of sources shows how much support a theme has. A source that disagrees shows where the theme is weak. The count does not show how much a theme matters, so the rule asks for a reason when a theme with few sources still matters.

## 3.1 Headline

**What**: the Minto pyramid puts the answer first, then the points that support it, then the evidence. Its common name is `BLUF`, bottom line up front. The rules use the alias Headline, per 4.2 item 6, so that each heading is one common word.

**Why**: a reader who stops after the first line still has the answer.

## 3.2 BRIEF

**What**: BRIEF is a five-part outline for short briefings: Background, Relevance, Information, End, Follow-up.

**Why**: it holds the body to one pass and gives each part a job.

## 4.1 Controlled style (ASD-STE100 subset)

**What**: ASD-STE100 is a controlled English for aerospace maintenance documents. It limits sentence length, grammar, and vocabulary.

**Why**: it removes ambiguity for readers who are not native speakers or who read under time pressure.

## 4.2 Reader level (CEFR B2)

**What**: CEFR is the Council of Europe scale for language ability, from A1 to C2. B2 is upper intermediate. A B2 reader understands the main ideas of complex text, including technical discussion in their own field.

**Why**: writing to B2 keeps the text readable for the widest professional audience without loss of precision.

## 4.4 Banned language and 4.5 Required text markers

**What**: Hyland's metadiscourse model classifies the words a writer uses to manage the reader rather than to carry content. It has two halves. Interactional markers manage stance: hedges, boosters, attitude markers, self-mentions, engagement markers. Interactive markers organise the text: transitions, frame markers, endophoric markers, evidentials, code glosses.

**Why**: naming the categories makes the rules testable. A list of example words alone is not. Section 4.4 bans the interactional half, because it adds stance without evidence. Section 4.5 requires the interactive half, because the simple-sentence rule in 4.2 would otherwise produce short, disconnected sentences with no visible reasoning chain.

## 4.6 Calibrated uncertainty

**What**: the IPCC guidance note defines likelihood terms with fixed probability ranges.

**Why**: a word like "likely" then means the same thing every time, and a reader can act on it.

## 5.2 Assumption log

**What**: assumptions-based planning records each assumption with its basis, its test, and its impact if wrong.

**Why**: a logged assumption can be tested later. An unlogged one becomes a hidden risk.

## 5.4 Citations and lineage

**What**: IEEE reference style numbers sources in order of first citation and lists them at the end.

**Why**: a bracket number is short, and the reader can follow every claim to its source.

Two house rules sit on top of IEEE style. A blank line separates each reference entry, and no rendered line in the text carries more than one citation. Markdown joins single line breaks into one paragraph, so without the blank lines the References list renders as one block. One citation per line lets a reader scan the lineage of a passage down the margin. It also lets a script test each citation against the References list without parsing sentences.

Source-type tags (P, S, T, U) mark each entry as primary, secondary, tertiary, or unclassified. A claim that drives the recommendation should rest on a primary or secondary source. The tag makes a weak chain visible without reading the source.

The tag follows how the claim uses the source, not the source alone. One source can be primary for one claim and secondary for another. The Wikipedia page on primary, secondary, and tertiary sources gives this point with examples. That page is a failed proposal, not a Wikipedia policy, so the rules file does not cite it.

## 6.4 Task kinds

**What**: Gherkin is the Given-When-Then syntax used in BDD. Kepner-Tregoe and Pugh are two weighted-criteria methods for choosing between options. ISO/IEC 25010 is the standard list of software quality characteristics.

**Why**: each gives a fixed form to a test so that two people would grade the same way.

## 6.5 Cynefin domain

**What**: Cynefin is Snowden's framework for classifying a situation by how cause and effect relate: Clear, Complicated, Complex, Chaotic, or Confused. Each domain has its own way of acting. Clear: apply best practice. Complicated: analyse, then act. Complex: probe, then act. Chaotic: act, then assess. Confused: find out which domain you are in.

**Why**: ordering actions by leverage assumes the leverage can be estimated. That holds in Clear and Complicated work. In Complex work the effect of an action is visible only afterward. A leverage number is then a guess, and the action must be a small probe with a budget. In Chaotic work stabilising comes before everything. Section 6.5 states the ordering rules that follow.
