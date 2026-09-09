# 13 — the tools: the argparse count did not move when the object changed completely, and a check that had never fired found three violations on its first run

*Measure: `python tools/toolscan.py`, in `notes/toolscan.txt`; `python
tools/toolsdiff.py ../pc-rpgmaker2000-doc/tools`, in `notes/toolsdiff.txt`;
`python tools/refusals.py rpgmaker2003-steam`, in `notes/refusals.txt` and
`notes/refusals-extended.txt`; `python tools/refusalclass.py <either>`, in
`notes/refusalclass.txt` and `notes/refusalclass-extended.txt`; `python
tools/pathcheck.py --needle …`, in `notes/pathcheck.txt`. Every selftest quoted
here was run at least once with `PYTHONIOENCODING` unset.*

---

## The box, counted and compared

```
python tools/toolscan.py
files scanned                      : 544
files with a forbidden control byte: 0
all three positive controls fired.

ls -1 tools/*.py | wc -l
544
```

**528 arrived and 544 leave.** The 528 were checked file by file against the
predecessor's box before anything was written, rather than assumed:

```
python tools/toolsdiff.py ../pc-rpgmaker2000-doc/tools \
    --ignore predbands.py --ignore toolsdiff.py \
    --expect-differing 0 --expect-common 528

mine   : 528 .py     theirs : 528 .py
only mine : none     only theirs : none
common    : 528      differing   : 0
```

**Sixteen written here**, and two modified:

| written | what it reads or checks | selftest |
|---|---|---:|
| `lcfmap.py` | `LcfMapUnit` and `LcfMapTree`, and the forced geometry | 19 |
| `lcfdiff.py` | two LCF databases, chunk / record / field | 17 |
| `projjoin.py` | a project's references, three destinations | 9 |
| `projdiff.py` | a project against the resource library | 8 |
| `crossnames.py` | crossing and non-crossing, and the rename classes | 14 |
| `jingles.py` | a duration split re-derived over three populations | 10 |
| `stampcheck.py` | three tests on a COFF `TimeDateStamp` | 19 |
| `psd.py` | Adobe's five sections | 14 |
| `pngchunk.py` | a named PNG chunk, CRC re-verified independently | 10 |
| `uuidscan.py` | version-1 UUID clocks, with the node redacted by program | 14 |
| `vendorhash.py` | third-party components, by a stated test | 13 |
| `compratio.py` | a shop's download figure against LZMA | 8 |
| `refusalclass.py` | why a refusal refused | 13 |
| `toolsdiff.py` | two tool boxes, by sha1 | 9 |
| `predbands.py` | the P11 bands of a predictions document | 10 |
| `pathcheck.py` | rule 7, over every tracked file | 10 |
| | | **197** |

| modified | why |
|---|---|
| `coverage.py` | three magics, `8BPS`, `LcfMapUnit`, `LcfMapTree` ([10](10-the-accounting.md)) |
| `refusals.py` | the previous object's file names unhard-coded, and nine readers added |

**197 checks across sixteen tools, 0 failures, every one run at least once with
`PYTHONIOENCODING` unset**, which is the previous session's `cptext.py` lesson
applied before it could bite. Every tool that prints recovered text sets its own
output encoding.

**And three selftests caught defects in the check rather than in the reader**,
which is the harder kind to notice:

* `psd.py` — the fixture wrote a Photoshop resource block whose empty Pascal
  name was one byte, where the format pads it to two. The walk failed with
  `the resource walk ends at 1070 of 49`, **and the reader was right**;
* `lcfdiff.py` — the renderer decoded two-byte values as text before trying
  them as numbers, and printed a database field as `A 猫  B 輩`. cp932 will turn
  almost any two bytes into a plausible kanji ([05](05-the-two-databases.md));
* `toolsdiff.py` — its first version refused `--selftest` on argument parsing
  because a positional was required, **which is precisely the `ispkg.py` defect
  this collection has been criticising for two objects**. Fixed, and the tool
  now refuses on reading a directory that holds no `.py`.

`lcfmap.py` accepts both `selftest` and `--selftest`, because sixteen tools that
take a flag and one that takes a subcommand is a harness that records refusals
it caused itself.

---

## The refusals, and the number that would not move

```
python tools/refusals.py rpgmaker2003-steam
readers pointed              : 67
refused with a non-zero exit : 42
exited 0 anyway              : 25
```

Against the previous object's 67, 40 and 27. `pc-rpgmaker2000-doc/docs/12`
classified those 40 by hand and found 23 argparse errors. **Doing it by hand
once is an observation; doing it by program gives a second population**, and
`refusalclass.py` decides each class from the harness's own captured message.

```
python tools/refusalclass.py notes/refusals.txt

  class        count   what it means
  argparse        23   the command line, not the object -- no byte was read
  oserror          9   the path was wrong for it
  format           9   it read bytes and said no
  exception        1   it fell over
  TOTAL           42
  argparse share of the refusals : 23 of 42 = 54.7619 %
```

**Twenty-three, both times.** The object changed completely — a different
product, a different decade of formats, 737 files against 477 — and the argparse
count did not move by one. That is because it is not a measurement of the object
at all: **twenty-three tools in this box take a subcommand and the harness never
gives one**, and it will be twenty-three on the next object too unless somebody
changes the harness.

**The nine format refusals are the ones that mean something**: `isz.py` and
`is32.py` refusing on magic within four bytes and naming both values,
`hashdb.py` saying `not a ZIP`, `isaccount.py` printing a complete accounting
table and a `VERDICT: DOES NOT CLOSE`. `ispkg.py` is still in the argparse
column, second appearance, unfixed.

### And two of the nine OS errors were the harness's own fault

```
itsf.py      REFUSED  FileNotFoundError: … 'rpgmaker2003-steam/rpg2000.chm'
runexpect.py REFUSED  the same
```

**`refusals.py` hard-coded the previous object's file names.** A reader that
opens `.chm` files perfectly was recorded as refusing, on an object that ships
one, because the table said `rpg2000.chm`. First appearance, and it is fixed
here: `%CHM%`, `%LDB%`, `%LMT%`, `%LMU%` and `%PSD%` are resolved against the
tree being pointed at, and a tree with no file of that kind gets a path that
does not exist so the refusal is recorded rather than hidden.

Extended with those fixes and with nine of this session's readers:

```
python tools/refusals.py rpgmaker2003-steam        (after the extension)
readers pointed              : 76
refused with a non-zero exit : 41
exited 0 anyway              : 35

  argparse        23      oserror  8      format  9      exception  1
```

**The argparse count is 23 for the third time**, over a third population.
`oserror` falls from 9 to 8 and `toolsdiff.py` appears in `format`, refusing on
reading a directory of data rather than on its command line — which is the
lesson, applied.

---

## The dangerous ones

### `jstore.py`, and the fifth through tenth false closure

The prediction was written before the run: *it will close at residue 0 on all
six by construction, because it solves for a filler term.* It does.

```
python tools/jstore.py <each of the six LCF files>

rpg_rt.ldb.dat   lists 1   GUIDs 18687   5 x 1 + 16 x 18687 + 89577 = 388574   residue 0
RPG_RT.ldb       lists 1   GUIDs 18687   5 x 1 + 16 x 18687 + 75232 = 374229   residue 0
RPG_RT.lmt       lists 0   GUIDs 0       5 x 0 + 16 x 0 + 335       = 335      residue 0
Map0001.lmu      lists 0   GUIDs 0       5 x 0 + 16 x 0 + 2752      = 2752     residue 0
Map0002.lmu      lists 0   GUIDs 0       5 x 0 + 16 x 0 + 7469      = 7469     residue 0
Map0003.lmu      lists 0   GUIDs 0       5 x 0 + 16 x 0 + 2414      = 2414     residue 0
```

**The four map files close with zero lists and zero GUIDs.** The arithmetic
consumed nothing at all and the residue is still 0, which is the mechanism at
its most naked: the filler is solved for, so it absorbs the entire file. Sixth,
seventh, eighth, ninth and tenth false closures, and the first three where the
tool found literally nothing and reported success.

Both databases claim **18,687 GUIDs** in files of 388,574 and 374,229 bytes, and
1,829 and 1,843 of them "repeated". `lcf.py` reads the same two files as 22
chunks each ([05](05-the-two-databases.md)).

### `kfaccount.py`, fifth appearance, and this time the reason

It exits 0 having printed its usage, again. **The mechanism, which is what P10
asks for rather than the occurrence**: every one of its arguments is optional —
`--root`, `--selftest`, `--format`, `--author` — none selects an action by
itself, and `main()` falls through to `print_help()` and returns 0. There is no
argument that makes it *do* anything, so any harness invoking it correctly gets
a usage message and a success code.

```
python tools/kfaccount.py --root rpgmaker2003-steam
usage: kfaccount.py [-h] [--root ROOT] [--selftest] [--format] [--author]
exit 0
```

### The inherited quiet ones, with their counts

| tool | defect | appearance |
|---|---|---|
| `namecensus.py` | `ZeroDivisionError` on an empty population | **twenty-first** |
| `dircensus.py` | a complete formatted table over `Director containers found : 0`, exit 0 | **twenty-second** |
| `protscan.py` | eleven pre-2010 optical markers, 9 files of 737, 0 hits | **seventeenth** |
| `mzcensus.py` | filters by the `.EXE` extension: 3 of 9, missing 2,425,856 bytes | **tenth** |
| `pecensus.py` | `impossible mtimes : 0 of 9` while seven are false | **third** |
| `pecensus.py` | **truncates a long path from the LEFT** | **first** |
| `jstore.py` | residue 0 by construction | fifth to tenth |
| `kfaccount.py` | exits 0 printing its usage | fifth |
| `refusals.py` | counts an argparse error as a refusal | third |
| `refusals.py` | **hard-codes the previous object's file names** | **first**, fixed |
| `ispkg.py` | refuses without reading a byte | second |
| `coverage.py` | three magics missing, and closes anyway | **first**, fixed |
| `buildroot.py` | **`--root` and `--file` default to another object's paths** | **first** |
| `pdbpaths.py` | looks only for CodeView RSDS records | first here |
| `ne.py` | **crashes on a directory instead of refusing** | **first**, found after publication |
| `sift.py` | eight-bit only — correct again here, and `utf16sift.py` reporting 0 is what says so | quiet |

**`pecensus.py`'s truncation is worth its own line** because the fix is not
obvious in the wrong direction. It prints
`mple/ArcheiaPictureTutorial/ultimate_rt_eb.dll`, eating `Sa` from the front.
A column that eats the *end* of a path loses which file it is; one that eats the
*front* loses which directory. **Both ends are load-bearing**, and the tools
written here truncate the middle and mark it with an ellipsis.

**And the two specialised build-path readers were both useless where a generic
one was not.** `pdbpaths.py --root` reports `binaries examined : 6`, `carrying a
CodeView RSDS path : 0`, `drive letters : {}` — on an object where
`sift.py --group buildpath` finds seventeen hits in one line and
`buildroot.py`, once told where to look, finds **fifty-eight**
([08](08-the-programs.md)). `buildroot.py`'s own defaults point at
`karmaflow-steam\Binaries\Win64\KFGame.exe` and it dies on them.

---

## Rule 7, checked by program for the first time, and it fired

`pc-rpgmaker2000-doc/docs/13` found a rule-7 violation **inside a captured
traceback committed under `notes/`** — a place nobody was checking because
nobody writes those by hand. `pathcheck.py` checks every tracked text file
rather than the documents, distinguishes this machine's paths from third
parties' by an allow-list that names its reason for each entry, and requires its
own positive control to fire.

**On its first run it found nineteen hits and three real classes of violation:**

| where | what |
|---|---|
| `docs/00-predictions.md:122` | the source installation's absolute path, quoted in §A |
| `notes/namecensus.txt`, `notes/ne.txt` | **five absolute paths inside two captured Python tracebacks** — the exact defect the previous session recorded |
| `tools/pathcheck.py` itself | its own selftest fixtures carried this machine's real directory name |

**The third one is the `redact.py` defect, in a new tool, on its first day** — the same defect that had stood in a published neighbour for two objects and that [12](12-whose-bytes.md) closes. A
checker that hard-codes the string it looks for publishes that string. Its
fixtures now use a fictional root, and the needles are given on the command line
so the list is visible rather than compiled in.

All three are repaired. The tracebacks carry a header saying what was replaced:

```
python tools/pathcheck.py --needle <four directory names this work lives under>
tracked files            : 657
text files checked       : 629
hits excused as artefacts: 2
VIOLATIONS               : 0
   the check fires on a planted line : True
   the negative control's unexcused hits : 0
```

The two excused hits are `D:\ha\` — a third party's build root, which the
standing rule publishes as an artefact ([08](08-the-programs.md)) — and an
environment variable name in an inherited tool's list.

---

## The position, stated plainly

**This object needed nine new readers where the previous one needed six, and
almost none of them was needed because the object was shut.** ITSF, LCF, PNG,
MIDI, RIFF WAVE, PE and the resource join opened 99.7986 % of it unchanged.

What the nine readers are for is the other 0.2014 % and, more than that, **the
comparisons**: two databases against each other, a project against a library,
one object's hashes against another's, one duration split against three
populations, one stamp against three tests. Six of the sixteen tools written
here take **two** inputs, which is not a shape this box had before, and it is
what an object with a documented predecessor asks for.
