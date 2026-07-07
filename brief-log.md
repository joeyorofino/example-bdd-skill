# Session log

Each entry documents one session: what was asked, what
changed, and why. Every commit must have a corresponding
entry here.

**Student responsibility:** Claude drafts the `Changed` field,
but you must read the diff and edit/confirm it before
committing. This is the verification step.

## Schema

| Field    | Description |
|----------|-------------|
| #        | Sequential session number, zero-padded |
| Brief    | Link to `briefs/<NNN>-<slug>.md` |
| Expected | Copied from the brief verbatim, including `[test]`/`[manual]` tags — what should be true after this session |
| Changed  | Student-confirmed list of what actually changed and why. `[test]` items are reported passing/failing based on an actual run; `[manual]` items are listed as "pending student review," never characterized |
| Rationale | Required whenever the session made a nontrivial decision — a real tradeoff was weighed, not just requested work carried out. One paragraph: what was decided and what informed it. Omit when there was no decision to justify. |
| Fix      | — / manual / follow-up |

## Log

---

### 001 — 2026-07-07 — GC content function

**Brief:** `briefs/001-2026-07-07-function.md`

**Expected:**
- Given: A string containing various characters
- When: the gc_content function is called
- Then: [test] gc_content("GCAT") should return 0.5
- Then: [test] gc_content("GGGG") should return 1.0

**Changed:**
- `gc_content.py` — new file; added `gc_content(sequence)` returning the proportion of G/C bases in the input string.
- `[test]` items: not run by Claude — pending student's own test run.

**Rationale:**
The brief didn't specify behavior for characters outside G/C/A/T or for an empty string. Chose to count G/C case-insensitively and return 0.0 for an empty string, rather than raising an error, since neither case is covered by the given test cases.

**Fix:** —

---
