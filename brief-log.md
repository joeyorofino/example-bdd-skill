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
| Rationale | Required whenever the session made a nontrivial decision.
One paragraph: what was decided and what informed it. When the decision
was filling a gap the brief left open, say so explicitly — separate what
the brief specified from what Claude decided on its own. Omit when there
was no decision to justify. |
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

### 002 — 2026-07-07 — Add percent argument to gc_content

**Brief:** `briefs/002-2026-07-07-add-argument.md`

**Expected:**
- Given: the gc_content function with the optional flag percent set by default as false
- When: the function is run with the optional flag percent is true
- Then: [test] gc_content("GGGC", percent=True) should return 100
- Then: [test] gc_content("GGGC", percent=False) should return 1.0
- Then: [test] gc_content("GGGC") should return 1.0

**Changed:**
- `gc_content.py` — added optional `percent` argument (default `False`) to `gc_content`; when `True`, multiplies the proportion by 100.
- `[test]` items: <!-- confirm pass/fail from your own run -->

**Rationale:**
—

**Fix:** —

---

### 003 — 2026-07-07 — CLI script for gc_content

**Brief:** `briefs/003-2026-07-07-cli-script.md`

**Expected:**
- Given: the gc_content_script.py and a string
- When: python gc_content_script.py "GCGC" is run
- Then: [test] python gc_content_script.py "GCGC" should return 1.0
- Then: [test] python gc_content_script.py "GCGC" --percent should return 100

**Changed:**
- `gc_content_script.py` — new file; self-contained (no import of `gc_content.py`, per Scope), with its own `gc_content(sequence, percent=False)` implementation. Takes the sequence as a positional CLI argument and an optional `--percent` flag (default off), and prints the result.
- test suite passes

**Rationale:**
The brief specified that the script must not import code and must contain everything it needs itself, so Claude duplicated the GC-counting logic from `gc_content.py` into `gc_content_script.py` rather than importing it — this is intentional duplication per Scope, not an oversight. The brief didn't specify how the result should be surfaced or how `--percent` should be parsed; Claude decided to use `argparse` with a `store_true` flag and to print the result to stdout, since a CLI script has no return value in the way a function does.

The original brief was underspecified and ended up with a script that imported the original function, and used a positional
sys argv for the input. Claude chose to use argparse in this new iteration rather than sys.argv.

**Fix:** -

---
