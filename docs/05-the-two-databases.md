# 05 — the two databases: seventeen chunks of twenty-two are byte-identical, and the five that are not are a person deleting thirteen heroes

*Measure: `python tools/lcf.py walk rpgmaker2003-steam/rpg_rt.ldb.dat --level 1`
and the same on the sample's, in `notes/lcf-walk-root.txt` and
`notes/lcf-walk-sample.txt`; `python tools/lcfdiff.py <root .ldb> <sample .ldb>
--only-text --verbose --expect-identical 17 --expect-differing 5`, in
`notes/lcfdiff.txt`; `python tools/lcfdiff.py --selftest` — 17 checks, 0
failures.*

---

## Two files, one format, never compared

```
rpg_rt.ldb.dat                            388,574 bytes   the editor's default
Sample/ArcheiaPictureTutorial/RPG_RT.ldb  374,229 bytes   a real project's
```

`lcf.py` opens both **without a change**, at residue 0, with twenty-two
top-level chunks each, tags 11 to 32 strictly ascending, shapes
`{'LIST': 15, 'RECORD': 3, 'SCALAR': 4}`, and — unlike the previous object —
**zero chunks where both readings close**, so no chunk's shape had to be settled
by an invariant. Twenty-two against the 2000's sixteen: **six new tags, 27 to
32.**

That is a confirmation and is worth exactly this paragraph. **What nobody had
done is put the two files beside each other**, and it needs no new format work:
762,803 bytes of structure `lcf.py` already walks.

---

## The chunk table

```
python tools/lcfdiff.py rpgmaker2003-steam/rpg_rt.ldb.dat \
    rpgmaker2003-steam/Sample/ArcheiaPictureTutorial/RPG_RT.ldb \
    --only-text --verbose --expect-identical 17 --expect-differing 5
```

| chunk | default | project | verdict |
|---:|---:|---:|---|
| 11 | 18,329 | 1,302 | **DIFFERS** |
| 12 | 18,779 | 18,779 | identical |
| 13 | 12,796 | 12,796 | identical |
| 14 | 12,671 | 12,671 | identical |
| 15 | 6,955 | 6,955 | identical |
| 16 | 492 | 492 | identical |
| 17 | 346 | 346 | identical |
| 18 | 1,278 | 1,278 | identical |
| 19 | 268,167 | 268,167 | identical |
| 20 | 3,290 | 3,290 | identical |
| 21 | 1,695 | 1,695 | identical |
| 22 | 436 | 439 | **DIFFERS** |
| 23 | 201 | 201 | identical |
| 24 | 201 | 611 | **DIFFERS** |
| 25 | 141 | 2,414 | **DIFFERS** |
| 26 | 0 | 0 | identical |
| 27 | 0 | 0 | identical |
| 28 | 0 | 0 | identical |
| 29 | 162 | 159 | **DIFFERS** |
| 30 | 23,487 | 23,487 | identical |
| 31 | 0 | 0 | identical |
| 32 | 19,069 | 19,069 | identical |

```
chunks in both        : 22
byte-identical        : 17
differing             : 5
only in A / only in B : 0 / 0
```

**369,226 bytes are byte-identical on both sides.** That is **95.0208 %** of the
default database and **98.6631 %** of the project's. The five differing chunks
are 19,269 bytes in the default and 4,925 in the project, and the remaining 79
and 78 bytes are the header and the tag/size overhead.

**Three of the six new chunks — 27, 28 and 31 — are declared with a size of
zero in both files.** A chunk that exists and holds nothing is a field the
format reserves and this product never fills, which is the same statement the
four empty `RTP\` directories make in a different vocabulary
([09](09-the-sample-project.md)).

---

## Chunk 11: thirteen heroes deleted and one renamed

```
records : A 14, B 1, common 1, only A 13, only B 0, common but changed 1
record 1 :
   field 1     A 'Zack'      B 'Brian'
   field 2     A 'None'      B 'Survivor'
```

The default database ships fourteen heroes — `Zack`, `Albert`, `Vance`,
`Craise`, `Arthur`, `Ardis`, `Fey-Lin` and seven more. **The project has one.**
Its id is 1, it was `Zack` and it is `Brian`, and his class field went from
`None` to `Survivor`.

**And the map tree calls the second map `Brian's House`** ([04](04-the-maps.md)).
A name typed into a database record and a name typed into a map title agree,
across two files written by two parts of the editor, and neither had been read
before this session.

---

## Chunk 22: the system record, and it is where the taste is

Chunk 22 is a RECORD on both sides — one bag of fields, no ids — and the first
version of `lcfdiff.py` printed `not a LIST on at least one side` and stopped.
That was a defect in the tool and it is fixed; the chunk is where the most
legible edits are.

| field | default | project | what it resolves to |
|---:|---|---|---|
| 19 | `SystemC` | **`SystemB`** | the window skin |
| 22 | `01 00 02 00 03 00 04 00` | `01 00` | **the starting party: four members, then one** |
| 41 | `Cursor1` | `Cursor1` + a level | the cursor sound |
| 42 | `Decision1` | **`Decision2`** | the confirm sound |
| 43 | `Cancel1` | **`Cancel2`** | the cancel sound |
| 44 | `Buzzer1` | **`Buzzer3`** | the error sound |
| 91 | 19,604 | 31,124 | a counter |

Fields 41 to 44 are nested records of the same shape as the map tree's field 12,
and they close inside their own lengths:

```
41  A  01 07 "Cursor1"   00
    B  01 07 "Cursor1"   03 01 32 00
42  A  01 09 "Decision1" 00
    B  01 09 "Decision2" 03 01 32 00
```

**All seven stems resolve to files that exist**, and the project's four all
gained a field 3 holding `0x32` = 50, which the default's do not carry at all:

```
Cursor1 Decision1 Decision2 Cancel1 Cancel2 Buzzer1 Buzzer3
   -> rpgmaker2003-steam/RTP/Sound/<name>.wav, 7 of 7 present
```

**Three of the four system sounds were changed and a volume was set on all
four.** That is what using the tool looks like from the outside.

**And field 22 is the party.** Eight bytes reading four `u16` — 1, 2, 3, 4 — in
the default, and two bytes reading one — 1 — in the project. Four heroes to one,
in a record, agreeing with fourteen heroes to one in chunk 11, in a different
chunk with a different shape.

### The one field this tool got wrong first, and it is recorded here

Field 91 is two bytes. The first version of `lcfdiff.py` decoded short values as
text before trying them as numbers, and printed:

```
field  91   A 猫    B 輩
```

— a cat and a fellow, invented by the renderer out of a counter. **cp932 will
turn almost any two numeric bytes into a plausible kanji**, and a document that
had quoted that line would have published a finding that does not exist. The
tool now renders one- and two-byte values as numbers first and its selftest
carries the case.

---

## Chunks 24 and 25: two lists doubled, and nine names typed by hand

| | default | project |
|---|---:|---:|
| chunk 24 | 100 records, none named | **200 records, nine named** |
| chunk 25 | 10 records, none named | **20 records, none named** |

The nine names, in record order:

```
  1  CHARACTER_POSE        9  INPUT_X
  2  CHARACTER_ZOOM       10  INPUT_Y
  6  INPUT_NUMBER_ORIG    11  DIGIT
  7  INPUT_NUMBER        100  EVENT_TRIGGER
  8  INPUT_ID_COUNTER
```

**Eight of the nine are the only capitals-with-underscores strings in 762,803
bytes of database, and all eight are in the project's file:**

```
grep -aoE "[A-Z][A-Z0-9]+_[A-Z0-9_]+" rpgmaker2003-steam/rpg_rt.ldb.dat
    (nothing)
grep -aoE "[A-Z][A-Z0-9]+_[A-Z0-9_]+" rpgmaker2003-steam/Sample/…/RPG_RT.ldb
    CHARACTER_POSE CHARACTER_ZOOM EVENT_TRIGGER INPUT_ID_COUNTER
    INPUT_NUMBER INPUT_NUMBER_ORIG INPUT_X INPUT_Y
```

The ninth, `DIGIT`, has no underscore. Everything else in both files is either
English
prose a translator wrote (`Poison Attack`, `Hi-Potion`, `Grassland 1`) or a
proper name. The nine are a programmer's naming convention inside a
game-making tool, in a project called `Picture Tutorial`, and `INPUT_X`,
`INPUT_Y` and `DIGIT` say what the tutorial is teaching.

Both lists doubled — 100 to 200 and 10 to 20 — which is what raising a project's
limit does. Chunk 25's records carry no name field at all in either file, only
`{11: 5, 21: 4, 22: 0}`, identical in all thirty; **this repository does not
claim to know which of the two lists is which**, and the reason it does not is
in [15](15-leftovers.md).

---

## What the diff is worth, and what it is not

**It is the only thing in this collection that shows one person's work against
its own starting point**, and it cost no new format work at all: `lcf.py` was
written for another object, `lcfdiff.py` is 250 lines on top of it, and the two
files were both already walking at residue 0 before this session began.

What it does not establish:

* **which of the two files is older.** The project's database is *not* the
  default with edits applied in the sense of a diff being a history; both are
  saved states and the direction is inferred from which one is the product's;
* **what the seventeen identical chunks mean.** They are identical, and this
  repository has read the names in six of them and no field's meaning in any;
* **the field numbering.** Field 19 of chunk 22 resolves to a `System\` file on
  all specimens tried, so it is the window skin; fields 41 to 44 resolve to
  `Sound\`; field 91 resolves to nothing and is called a counter because it is
  two bytes and it changed.
