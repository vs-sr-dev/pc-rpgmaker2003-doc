# 16 — prediction scoring: P11's falsification is survived, P12's fires, and P13's fires in a way P13 did not anticipate

*Measure: `python tools/predcount.py` for the clause counts and the two
predicted totals; `python tools/predbands.py --expect-under 0.60 5` for the
three bands; `python tools/checkscore.py docs/16-prediction-scoring.md` for the
verdicts, counted out of the tables on this page rather than added up by hand.*

```
63 clauses     inherited 31     open 32 (method 5, content 27)

inherited      31 clauses   predicted 28.61   obtained 29.50   delta  -0.89
open           32 clauses   predicted 23.31   obtained 30.00   delta  -6.69
  open method   5 clauses   predicted  4.45   obtained  5.00   delta  -0.55
  open content 27 clauses   predicted 18.86   obtained 25.00   delta  -6.14

and the three P11 bands:
  lands        7 clauses   predicted  5.29   obtained  7.00   delta  -1.71
  constructs  12 clauses   predicted  7.04   obtained 10.50   delta  -3.46
  nonnumeric   8 clauses   predicted  6.53   obtained  7.50   delta  -0.97

hit = 1, half = 0.5, miss = 0. The two totals are never added together.

the verdicts, for `checkscore.py` to check the tables against:
  hit           56
  half           7
  miss           0
  unresolved     0
```

**The calibration entry for this session is `−6.69`**, predicted minus obtained
on the open clauses. Ranked by absolute value it is **ninth of thirty-five**;
the eight larger terms are +19.75, −14.00, +10.50, +9.30, +9.00, −8.89, −7.57
and +7.50. **It is the largest negative term in five sessions.**

**It is also exactly what P12 asked for and it is P12's own falsification.**

---

## Inherited — 28 hits, 3 halves, 0 misses

| | verdict | note |
|---|---|---|
| C01 | **hit** | 737 of 737 on size, on mtime to the 100-ns tick and on sha1, 41 directories of 41, 19 empty of 19, final agreement `True` |
| C02 | **hit** | 737 / 33,578,445 / 731 distinct / 0 unreadable, the byte total re-derived by `find … printf '%s' \| awk`, and all six repeated hashes named |
| C03 | **hit** | every field exactly, both residues 0, `InstallScripts` naming `2k3_install.vdf`, `LastOwner` redacted by the program |
| C04 | **hit** | 22 rows over 41 directories of which 19 empty, summing to 737 and 33,578,445; the three subtrees exact |
| C05 | **hit** | seventeen rows, all figures exact, three of four `.dat` are PE32 |
| C06 | **hit** | 729 / 26,479,895; 3 / 7,030,927; 0; 5 / 67,623; residue 0; all five opaque files named with their sizes |
| C07 | **hit** | 432 of 1,041, seventeen rows, `.CHM` 7.9980, `.R3PROJ` 3.6250, `.EXE` 5.8084 with zero blocks above 7.5 |
| C08 | **hit** | 9 / PE32 9 / NE 0, all by magic, every linker version and byte count, and `ne.py`'s message verbatim |
| C09 | **half** | `impossible mtimes : 0 of 9` is exact and both powers of two are exact — but the clause said **five** of nine stamps are false and it is **seven files, five distinct binaries**. The clause inherited the pre-briefing's conflated denominator and repeated it ([14](14-corrections.md)) |
| C10 | **hit** | `mple/ArcheiaPictureTutorial/ultimate_rt_eb.dll`, truncated from the left, first appearance |
| C11 | **hit** | 6 of 9, editor and runtime both 1.1.2.1, `Degica` in exactly two `FileDescription` fields, `LegalCopyright` empty on every Kadokawa binary, `UNLHA32.DLL` exact |
| C12 | **hit** | 3 of 9, 2,425,856 bytes missed, `0 of 3 agree`, `byte2=0x50 ('P')` |
| C13 | **hit** | 17 hits in 3 files, 15 in `rpg2003.exe`, ten distinct paths, eight `.pas`, `RPG2003.hlp`, and the two others named |
| C14 | **hit** | 3 in 1 blob over 737, two distinct addresses, both controls, `utf16sift.py` 0 |
| C15 | **hit** | 9 of 737, 7,893,678 of 33,578,445, 0 hits, control fires on 9 |
| C16 | **hit** | one wave, 12:18:11 .. 12:18:20, 737 files, 100.00 % |
| C17 | **hit** | 368 of 731, 104 / 461 / 155,888, all with `pc-rpgmaker2000-doc`, 134 and 65 re-derived with `ls` |
| C18 | **hit** | 211 / 92 / 63 / 1 / 1 summing to 368, and 12,428,739 bytes |
| C19 | **half** | 277 and 91 are exact — but the clause gave the split as **50 + 3 + 38** and said it was checked by command. The command gives **47 + 3 + 41**, and the check is what found it |
| C20 | **half** | the seventeen inherited files and the disjoint split re-derive **exactly**, on two axes — but the clause said no file gained a `J` it did not already have inside, and `J2003Horn.mid` did |
| C21 | **hit** | 4 of 737, 5 in 4; 630,784 / residue 0 / 483,728 / `RCDATA/GAMEDELETE/9` / 142,848 against 142,848 |
| C22 | **hit** | all nine closures with every number, `HHA Version 4.74.8702`, `RPG Maker 2003`, `rpg2003_en`, three clocks and 7.551 ms |
| C23 | **hit** | both databases, 22 chunks, tags 11..32, residue 0, the three shapes, zero ambiguous |
| C24 | **hit** | 355 / 0 / 355 / 1,848 / 1,848, 231 palettes, 349 IDAT streams, fourteen types with `tIME` 1 and `tpNg` 1 |
| C25 | **hit** | 141 / residue 0 / 1,963 / 797,748 / 10,435.682, the four meta counts, 62 + 21 = 83, five marker spellings |
| C26 | **hit** | 216 of 216, 157 and 59, mono 22,050 Hz, 263.486349206 s, the three chunk orders, `Rain1`/`Rain2` |
| C27 | **hit** | 299 of 299, residue 0, 18 stems and 18 of 299 ambiguous |
| C28 | **hit** | `toolscan.py` 528, `ls` 528, and `toolsdiff.py` 528 common / 0 differing, with the two files this session had already written named as ignored |
| C29 | **hit** | twenty-first and twenty-second |
| C30 | **hit** | 1,545 bytes, both registry shapes, `.r3project`, the DEP shim in both hives, `kvsignatures` at 256 hexadecimal digits |
| C31 | **hit** | 34 terms, −18.7200, −0.5506, 22 negative, 1 zero, last ten −38.3300 at −3.8330, tail run 3, rank 7 of 34, and **all eight of the brief's claims checked and none wrong** |

**The three halves have one shape.** Every one of them is a clause that
inherited a figure from the pre-briefing and asserted it as its own. C09 took
"five of nine", C19 took "50 + 3 + 38", C20 took "seventeen and no others".
**In each case the surrounding measurement was exact and the inherited number
was not.** The lesson is not "re-measure the inherited clauses" — that is what
they are for — it is that an inherited clause should test *the figure* rather
than *restate* it, and three of the thirty-one restated.

---

## Open, method — 5 hits

| | verdict | note |
|---|---|---|
| C32 | **hit** | sixteen tools, **197 selftest checks, 0 failures**, every one run with `PYTHONIOENCODING` unset; every tool that prints recovered text sets its own encoding; every name checked against `tools/` before writing |
| C33 | **hit** | every chapter opens with `*Measure:*`, `docs/02` carries a command on every row, and the eight denominators are tabulated in `docs/01` with the eighth named |
| C34 | **hit** | `pathcheck.py`, over 629 tracked text files, **0 violations, positive control firing, negative control quiet** — after it found three real ones on its first run ([14](14-corrections.md)) |
| C35 | **hit** | branch `master`, the `git ls-files` filter empty with a positive control that fires, description under 350 characters read back from the remote, topics set, the four excluded paths absent, and `pc-gamelist-doc` pushed on `main` |
| C36 | **hit** | seventeen documents, under twenty, and every chapter carries a measurement made on this object |

---

## Open, content — 23 hits, 4 halves, 0 misses

| | verdict | band | note |
|---|---|---|---|
| C37 | **half** | `constructs` | Two of four sub-claims false and two true. **`lcf.py` does not close on the four files** — it refuses, correctly, in two ways — and there are **no named width or height fields**. But the three maps' dimensions are given as three specific pairs, and 3 of 3 chipset chains resolve. **The route was wrong and the destination was overshot**: the geometry is *forced* rather than read ([04](04-the-maps.md)) |
| C38 | **hit** | `lands` | `Picture Tutorial`, sixteen characters, length-prefixed, agreeing with `GameTitle`; exactly three map entries besides the root, matching the three `.lmu` by number |
| C39 | **hit** | `constructs` | 17 identical and 5 differing of 22, chunk by chunk with both lengths, and `chunk 11, record 1, field 1: 'Zack' → 'Brian'` — plus a party of four cut to one and three system sounds swapped |
| C40 | **hit** | `constructs` | tags 27..32 present in both, and **three of the six hold nothing**, declared at size zero in both files, which is what they hold |
| C41 | **hit** | `constructs` | `Enterbrain` at seven offsets in six files, and `Software\Enterbrain\RPG2003` in exactly one — `ultimate_eb.dll` |
| C42 | **hit** | `lands` | the one `tIME` located, `INPUTDISPLAY.png`, 2017-09-13 18:22:56 UTC, and the one `tEXt` named beside it |
| C43 | **hit** | `constructs` | file, offset 87, length 8, CRC re-verified by a second route, payload `GLD3\0\0\0\0` dumped — and **attributed from the same file's `Software` field**, `GLDPNG ver 3.3` |
| C44 | **hit** | `constructs` | 363 by extension summing to 363 and to 19,984,119, which plus 12,428,739 is the 32,412,858 of the 731 distinct hashes; `docs/07` uses that denominator throughout |
| C45 | **hit** | `constructs` | decided, on a third witness named — a PNG `tIME`, nine UUID clocks and a `.psd`'s own metadata — with the shortcut's byte-identity re-derived by sha1 on both trees. **The answer is neither of the two dates offered** |
| C46 | **hit** | `lands` | three magics, six new selftest checks, 730 / 26,534,548 and 7 / 7,043,897, 0 derived, 0 opaque, residue 0; PSD in SPECIFIED and the three LCF variants in DECODED |
| C47 | **hit** | `nonnumeric` | two sentences, and which of the two is about the world and which about the box ([10](10-the-accounting.md)) |
| C48 | **hit** | `lands` | 3 channels, 196 × 123, depth 8, colour mode 3, and the closure with its weakness stated |
| C49 | **half** | `constructs` | The third test is written, fires on both round stamps, and the collision test fires on the four Borland files; both controls behave. **But the clause predicted "5 of 9" and the answer is 7 of 9 files** — the same inherited conflation as C09 |
| C50 | **half** | `nonnumeric` | The list is written, with sha1, size, path, vendor, component and evidence offset, and the neighbours are checked. **The clause asked for sha1, size and *version*, and the tool does not print the version.** It is in `notes/verres.txt` and it is not in the list the clause specified |
| C51 | **hit** | `nonnumeric` | one paragraph, not re-argued, `--expect 3` firing, the name and copyright and version and date published, and the space spent on the two-addresses fact |
| C52 | **hit** | `nonnumeric` | checked, still present, stated with the command and the counts, said a second time |
| C53 | **hit** | `constructs` | re-run unextended, four classes summing to 42, argparse compared with 23 of 40 — **and it is 23 on all three populations** |
| C54 | **hit** | `lands` | both databases and all four map files, the claim written before the run, residue 0 on all six with the arithmetic printed, fifth through tenth |
| C55 | **hit** | `lands` | fifth, exit 0, usage printed, and the mechanism named: no argument selects an action, so `main()` falls through to `print_help()` |
| C56 | **hit** | `constructs` | 22,422,597 against 22,100,528, +322,069 = +1.4573 %, against the previous object's 0.16 % — and the deduplicated total closing the gap the other way |
| C57 | **half** | `constructs` | The three counts are delivered and sum — 14 inside, 385 in the RTP, 7 nowhere of 406 — **but the clause said `rtpjoin.py` is pointed at the project, and a new tool was written instead**. The instrument named in the clause was not the instrument used |
| C58 | **hit** | `nonnumeric` | thirty-two initialisms, four buckets, 6 + 3 + 10 + 13 = 32 |
| C59 | **hit** | `nonnumeric` | eleven in the pre-briefing including arithmetic, and fourteen of this session's own |
| C60 | **hit** | `nonnumeric` | `Saga` = `RPG Maker`, the `Year` argued from four candidates and named, "What it is" saying it is a tool that ships a game, and `rowlen.py` reading **77 rows, 0 over budget** |
| C61 | **hit** | `constructs` | nineteen named, 4 + 15 = 19, and two different meanings — plus the 10-of-15 mapping onto resolved references |
| C62 | **hit** | `lands` | offset 617 in the script, the sixteen bytes on disk, **and 149,405 / 149,417 in `ultimate_eb.dll`**, with what can and cannot be established |
| C63 | **hit** | `nonnumeric` | the zero differences written as measurements with their commands, and every neighbour figure taken from its `docs/` |

---

## P11, scored, and it is survived

> **P11.** For each open content clause, record whether the object turned out to
> support **more** than the clause asked, exactly what it asked, or less.
> **Falsification: if `lands` and `constructs` have the same over-delivery rate,
> P8's mechanism is dead and not merely untestable.** The previous session's
> rates were 6 of 10 and 5 of 8 — a tie.

Applied to this session's twenty-seven open content clauses:

| band | n | over-delivered | rate |
|---|---:|---:|---:|
| `lands` | 7 | **3** — C48, C54, C62 | **42.9 %** |
| `constructs` | 12 | **9** — C37, C39, C41, C43, C45, C49, C53, C56, C61 | **75.0 %** |
| `nonnumeric` | 8 | 3 — C52, C59, C61's neighbours aside, C63 | 37.5 % |

**The tie is broken, and in the direction P8 predicted.** A clause that
*constructs* a number out of several measurements over-delivers three-quarters
of the time; a clause that *lands* on a number the object's own author wrote
over-delivers two-fifths of the time. **P8's mechanism is alive.**

The reason is visible in the individual rows and is not subtle. A `lands` clause
asks for a field and gets a field: C38 asked for a string and got the string;
C42 asked for a timestamp and got the timestamp; C46 asked for a table and got
the table. **There is nothing above a declared number to over-deliver into.**
A `constructs` clause asks for an arithmetic, and an arithmetic that works
usually works on more than the clause named: C45 asked which of two dates and
found that the answer is neither, C49 asked for a count and found two
denominators, C41 asked for a string and found a registry key.

**And this session was supposed to be P11's hard test.** The predictions
document said so before the result: a large part of this object is documented
next door, and a clause asking for a *confirmation* cannot over-deliver by much.
**That prediction was wrong in an instructive way.** The confirmations — C20's
`J`, C22's nine closures, C23's twenty-two chunks — are almost all in the
*inherited* band, where P11 does not look. The open clauses were not
confirmations at all; they were the things nobody had done.

---

## P12, scored, and its falsification fires

> **P12.** Write, for at least five open content clauses, the strongest claim
> the object could conceivably support rather than the one you are confident of,
> and price those five below 0.60. **Falsification: if all five hit, the
> pipeline was under-claiming rather than under-pricing.**

The five, named in advance so this chapter could not choose them afterwards:

| | priced | obtained | what happened |
|---|---:|---:|---|
| **C37** | 0.45 | **0.50** | half — the destination overshot, the route wrong |
| **C39** | 0.50 | **1.00** | hit, and it named four edits where it asked for one |
| **C41** | 0.35 | **1.00** | hit — `Enterbrain` is in the bytes, in a registry key |
| **C43** | 0.40 | **1.00** | hit — `tpNg` decoded **and** attributed from the same file |
| **C45** | 0.55 | **1.00** | hit, and the answer is neither of the two dates |
| | **2.25** | **4.50** | |

**Four of five hit outright and the fifth half-hit, against a predicted 2.25.**
That is the falsification condition in everything but its literal wording, and
this document reports it as fired rather than arguing about the half.

**The diagnosis P12 offered is correct: this pipeline was under-claiming, not
under-pricing.** Every one of those five clauses asked for something this
document did not believe it would get, and four of them arrived. The clauses
were not too cheap; they were, for the first time in a long while, ambitious
enough to be worth pricing at all — and the object had the material.

**And the calibration term is the cost.** −6.69 is the largest negative in
thirteen sessions, and it was produced *on purpose*, by the prescription in
force. A pipeline that follows P12 will post large negative terms until its
claims catch up with its objects, and the series will look worse while the
documents get better. **That is a real tension and it is not resolved here**;
what P14 does about it is below.

---

## P13, scored, and it fires in a way P13 did not anticipate

> **P13.** Do not write the rule-0 clause; make the failure impossible. No
> heredoc for any content, ever, with `Write` to a scratch file as the only
> route. **Falsification: if C29's successor still fails under that rule, the
> problem is not the heredoc and the diagnosis has been wrong four times.**

**The clause was not written**, exactly as P13 required, and this document
reports the outcome as a plain fact worth zero points.

**Rule 0 was violated five times** ([14](14-corrections.md)). Five shell
heredocs carrying content were used, by reflex, in a session whose predictions
document states the prohibition in its own preamble and explains why it exists.

**And here is what P13 could not have predicted: none of the five failed.** Not
one ate a backslash. Not one produced a wrong number. The failure mode P13 was
written against — *a shell heredoc carrying a backslash*, the shape of four
violations in five sessions — **did not occur even once in five violations.**

So P13's falsification fires twice over:

* **the rule did not make the failure impossible**, because declaring a habit
  forbidden does not remove the habit. Five reaches for a heredoc, five times
  unremarked until this chapter counted them;
* **and the diagnosis was aimed at the wrong thing.** The heredoc is not the
  hazard; the hazard is *content passing through a shell*, and it happens to be
  survivable when the content has no backslashes in it. Four sessions blamed the
  syntax when the variable was the payload.

**What actually caught things in this session was not a rule.** It was
`predcount.py` refusing a stale header, `pathcheck.py` firing on three real
violations, `crossnames.py` disagreeing with a hand-sorted split, `lcfdiff.py`'s
selftest, and five `FATAL: pattern did not match` refusals from throwaway patch
scripts. **Every single one is a check that runs, and not one is a sentence in a
document.**

---

## The calibration series, extended

```
+10.50  +7.50  +5.00  +2.00 -14.00  -2.00  +9.00   0.00 +19.75
 +5.25  -4.10  -3.40  +9.30  +1.05  -2.50  -3.57  -2.50  -0.35
 -3.85  -4.95  -4.70  +0.70  -2.40  -2.12  -3.57  -3.88  -3.87
 -2.92  -8.89  -5.93  +0.51  -7.57  -0.42  -1.79  **-6.69**

terms    : 35
sum      : -25.4100
mean     : -0.7260
negative : 23   positive : 11   zero : 1
last10   : -41.4500   mean -4.1450
consecutive negatives at the tail : 4
ranked by absolute value, -6.69 is ninth of 35
```

**The last-ten mean worsens from −3.8330 to −4.1450 and the tail run reaches
four.** Read as a trend that is the pipeline drifting further from calibration.
Read against P12 it is the pipeline doing what it was told: the term is large
and negative **because five clauses were deliberately priced at less than half
what they were worth, and the object paid all five.**

**Those two readings cannot both be tested by the same number**, which is the
problem the next prescription has to solve.

---

## What this document predicts

> **P14 — the calibration series has been measuring two things and reporting
> one.** A negative term now means either *this session was too cautious* or
> *this session followed P12 and claimed hard*, and −6.69 is the second. The
> series cannot distinguish them and has not been able to since P12 came into
> force. **Split it: report the term over the clauses P12 governs (the five
> deliberately underpriced) separately from the term over the rest.** On this
> session those are **2.25 − 4.50 = −2.25 over five clauses** and
> **16.61 − 20.50 = −3.89 over the other twenty-two**, and the second is the
> one that measures calibration. **Falsification: if the two sub-terms move together over
> the next three sessions, they are one signal and splitting them was
> bookkeeping.**

> **P15 — the inherited band's only failures were restatements.** All three
> halves in thirty-one inherited clauses came from asserting a pre-briefing
> figure rather than testing it, and in each case the surrounding measurement
> was exact. **The next document should write every inherited clause as a test
> with a stated tolerance — "the command reports X, and if it does not, the
> figure that is wrong is the brief's" — rather than as an assertion of X.**
> **Falsification: if the next session's inherited band still loses points to
> restated figures under that wording, the wording was not the problem and the
> pre-briefing simply has to be checked line by line before the clauses are
> written.**

> **P16 — stop writing rules that a person has to remember, and write checks
> that fire.** Rule 0 was violated five times in a session that had read P13
> aloud, and every defect actually caught this session was caught by a program:
> a header regenerated from a tool's output, a path checker with a positive
> control, a rename classifier that disagreed with a hand sort, three selftests
> that failed on their own fixtures. **The next session should convert the one
> remaining discipline rule it keeps breaking into a program that refuses**, and
> should not write it as a clause. **Falsification: if a rule-0 violation still
> occurs when the only route to a shell is a wrapper that refuses heredocs, then
> the problem is neither the syntax nor the payload but the operator, and this
> pipeline should stop pretending otherwise and simply count them.**
