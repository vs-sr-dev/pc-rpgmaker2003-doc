# 04 — the maps: two grammars in twelve thousand bytes, a reader that was supposed to work and did not, and a geometry the files never declare

*Measure: `python tools/lcfmap.py walk <file> --expect-residue 0` on all four,
in `notes/lcfmap-walk.txt`; `python tools/lcfmap.py tree <…>/RPG_RT.lmt`, in
`notes/lcfmap-tree.txt`; `python tools/lcfmap.py geometry <…>/Map000{1,2,3}.lmu
--expect 20x15`, in `notes/lcfmap-geometry.txt`; `python tools/lcfmap.py
selftest` — 19 checks, 0 failures.*

---

## What was actually unopened

**12,970 bytes in four files, 0.0386 % of the object.** Three map files and one
map tree, in the sample project:

```
RPG_RT.lmt      335   0a 4c 63 66 4d 61 70 54 72 65 65 04 00 01 10 50  |.LcfMapTree....P|
Map0001.lmu    2752   0a 4c 63 66 4d 61 70 55 6e 69 74 01 01 04 0b 01  |.LcfMapUnit.....|
Map0002.lmu    7469   0a 4c 63 66 4d 61 70 55 6e 69 74 01 01 03 0b 01  |.LcfMapUnit.....|
Map0003.lmu    2414   0a 4c 63 66 4d 61 70 55 6e 69 74 0b 01 00 2a 01  |.LcfMapUnit...*.|
```

`pc-rpgmaker95-doc` could name the map format and never saw one.
`pc-rpgmaker2000-doc` had none. **This object ships three specimens of one
variant and one of another, which is more specimens of an unopened format than
this pipeline has ever had at once.**

---

## The reader that was supposed to work, and both ways it fails

`lcf.py` takes its header name from the file rather than assuming it, so the
pre-briefing supposed it would probably read these four. **It does not, and the
two refusals are the two grammars.**

```
python tools/lcf.py walk <…>/RPG_RT.lmt
    Bad: tag 1 at offset 13 does not exceed the previous tag 4

python tools/lcf.py walk <…>/Map0001.lmu
    Bad: a tag of 0 at top level, at offset 2751
```

**Both refusals are correct** and each names its own reason, which is what a
refusal is for. `lcf.py` requires the top level to be tag/size chunks with
strictly ascending tags and no terminator, because that is what a database is.

* **`LcfMapUnit` is a RECORD at top level.** Fields, tag/size/data, terminated
  by a tag of 0 — and that terminator is the file's **last byte**. The tags do
  ascend; the terminator is what `lcf.py` cannot allow;
* **`LcfMapTree` is a LIST at top level.** The two bytes after the name are
  `04 00`: a count of four and an id of zero. `lcf.py` must read them as tag 4
  with size 0, after which the next tag is 1 and does not ascend.

`lcfmap.py` implements both. The ENCINT is the same big-endian seven-bit varint
`lcf.py` derived, and that is agreement rather than assumption: decode it any
other way and none of the four lands anywhere near its own end.

---

## All four close on their own last byte

```
python tools/lcfmap.py walk <…>/Map0001.lmu --expect-residue 0
```

| file | bytes | top level | fields / entries | walk ends at | residue |
|---|---:|---|---:|---:|---:|
| `Map0001.lmu` | 2,752 | FIELDS + terminator | 10 fields, 10 events | 2,752 | **0** |
| `Map0002.lmu` | 7,469 | FIELDS + terminator | 10 fields, 19 events | 7,469 | **0** |
| `Map0003.lmu` | 2,414 | FIELDS + terminator | 10 fields, 6 events | 2,414 | **0** |
| `RPG_RT.lmt` | 335 | LIST of 4 + a trailing block | 4 entries | 335 | **0** |

The three `.lmu` carry the same ten fields in the same order, and the tag sets
differ in exactly one position: `Map0001` and `Map0002` carry tag 1 and
`Map0003` carries tag 42 instead.

```
Map0001  1 11 50 60 61 62 71 72 81 90
Map0002  1 11 50 60 61 62 71 72 81 90
Map0003 11 42 50 60 61 62 71 72 81 90
```

**A field that is absent from one file and present in two is the format's own
statement that the field has a default** — and that is the mechanism the
geometry turns on. It is visible a second time inside the event lists:
`Map0001`'s event 3, `MgicCircle`, carries no tag 2 while the other nine events
all do, and its neighbour at tag 3 reads 14. **An omitted field is a default,
not a missing one.**

---

## The map tree, read

```
python tools/lcfmap.py tree <…>/RPG_RT.lmt

entries : 4 (id 0 is the root and is the project title)
   id 0  Picture Tutorial      fields 1 4 7 11 12 21 31 32 33 41 44 51
   id 1  Basement              fields 1 2 3 4 11 12 21 31 32 33 41 51
   id 2  Brian's House         fields 1 2 3 4 11 12 21 31 32 33 41 51
   id 3  World Map             fields 1 3 4 5 6 7 11 12 21 31 32 33 41 51
order   : [0, 3, 2, 1]
RESIDUE : 0
```

**Entry 0's name is `Picture Tutorial`, sixteen characters with the length in
front of it, and `Sample\…\RPG_RT.ini` says `GameTitle=Picture Tutorial`.** Two
files written by different parts of the editor agree on one string, and neither
had been read.

**Three maps besides the root, and there are three `.lmu` on disk.**

Field 12 of each entry is a nested record with its own terminator, and it closes
inside its own declared length on all four:

| entry | field 12, inner field 1 | resolves to |
|---|---|---|
| `Picture Tutorial` | `(OFF)` | **nothing — it is not a file name** |
| `Basement` | `2003Sorrow` | `RTP\Music\2003Sorrow.mid` |
| `Brian's House` | `Village 2` | `RTP\Music\Village 2.mid` |
| `World Map` | `SESea` | `RTP\Music\SESea.wav` |

**Two of those three are files whose names were changed between the 2000 and the
2003** — `Village2` gained a space and `Sea` gained an `SE` prefix
([06](06-the-crossings.md)) — so a map tree in a tutorial project references the
renaming policy of a publisher, and the reference resolves.

**And the fourth resolves to nothing on purpose.** `(OFF)` is the one map-tree
music reference in `notes/projjoin.txt` that lands nowhere, and it is not a
missing file: it is the absence of one, spelled.

### The one place the closure is ambiguous, and it is said so

The sixteen bytes after the four entries close at residue 0 under **two**
readings:

```
04 00 03 02 01 01 01 01 02 02 01 0a 03 01 06 00

reading A   count 4, then ids 0 3 2 1, then three fields, then the terminator
reading B   five tag/size fields, the first of size zero, then the terminator
```

Both land on byte 335. `lcfmap.py` reports the ambiguity rather than hiding it
and prefers A, **on an invariant rather than on a closure**: the four values
reading A recovers are `0 3 2 1`, which is exactly a permutation of the four
entry ids. Reading B has to explain a zero-length field and explains nothing
about why those four bytes are a permutation.

**That is weaker than a closure and it is the same instrument
`pc-rpgmaker2000-doc/docs/05` had to reach for on chunk 21**, on a different
format, one session earlier. Two arithmetics that both close are not a
measurement; a counting invariant that only one of them explains is the next
best thing.

---

## The geometry, which no file declares and which is forced anyway

**Not one of the three maps carries a width or a height.** The dimensions are
still determined, in three steps, each of which can be checked:

**One. The two layer chunks are 600 bytes each, in all three maps.**

```
Map0001  tag 71 : 600 bytes    tag 72 : 600 bytes
Map0002  tag 71 : 600 bytes    tag 72 : 600 bytes
Map0003  tag 71 : 600 bytes    tag 72 : 600 bytes
```

**Two. The cell is two bytes.** Read as little-endian `u16` the six layers hold
values up to **10,131**, which does not fit in eight bits. Read as single bytes,
the odd positions would have to be a second independent plane and they are not:
every one of the 300 odd bytes is non-zero in five of the six layers. 600 ÷ 2 =
**300 cells**.

**Three. The events pin the aspect.** Across the three maps the event
coordinates reach **x = 18** and **y = 14**, so W ≥ 19 and H ≥ 15.

```
python tools/lcfmap.py geometry <…>/Map0001.lmu <…>/Map0002.lmu <…>/Map0003.lmu

cells per layer : 300  (two bytes each)
event extremes  : max x 18, max y 14  ->  W >= 19, H >= 15
factorisations of 300 meeting both bounds : 20x15
THE GEOMETRY IS FORCED : 20 x 15
```

**Twenty by fifteen is the only factorisation of 300 that survives.** 19 and 18
do not divide 300; 25 × 12 and 30 × 10 fail the height; everything wider fails it
worse.

**That is a measurement and not a manual reading.** The product's default new
map is twenty by fifteen and this repository did not have to know that: the
number falls out of a layer length, a cell width and two event coordinates.
What it does not establish is that *every* RPG Maker 2003 map is 20 × 15 — these
three are, and all three omit the field, which is consistent with the field
being omitted when it holds the default and with nothing else in this object.

---

## The events, and one of them is the tutorial's subject

```
python tools/lcfmap.py events <…>/Map0002.lmu
```

Thirty-five events over three maps, every event list closing at residue 0.
Each event carries a name, a position, and a list of pages; a page's field 21 is
a character-graphic stem that resolves ([09](09-the-sample-project.md)).

```
Map0001  10 events   EV0001 EV0002 MgicCircle EV0004 COFFIN×4 Inti Lenne
Map0002  19 events   DIARY EV0002..EV0017 ALEX Basement "Return Tint"
Map0003   6 events
```

**`ALEX` is the 2000's default hero and he is not in either of this object's
databases.**

```
grep -c -a Alex rpgmaker2003-steam/rpg_rt.ldb.dat                        0
grep -c -a Alex rpgmaker2003-steam/Sample/…/RPG_RT.ldb                   0
grep -c -a Alex ../pc-rpgmaker2000-doc/rpgmaker2000-steam/rpg_rt.ldb.dat 1
```

The 2003's own first hero is `Zack` ([05](05-the-two-databases.md)). So a
tutorial shipped inside RPG Maker 2003 names, as one of its nineteen events, the
default hero of the previous product — a string that exists nowhere in the
2003's 33,578,445 bytes except in that event name. `Inti` and `Lenne` are in
neither database either. `Return Tint` is a screen effect and `MgicCircle` is a
misspelling that shipped.

---

## What the maps still do not say

* what the other seven top-level fields hold — tags 11, 42, 50, 60, 61, 62 and
  90 are read as lengths and offsets and not as meanings;
* what a tile value like 4,350 or 10,131 indexes into. The chipset the map
  points at is resolved ([09](09-the-sample-project.md)); the tile numbering
  inside it is not;
* whether the event pages' remaining eleven fields are a command list. They are
  a nested structure that walks, and this repository stopped there;
* whether any RPG Maker 2003 map that is *not* 20 × 15 declares its size in tags
  2 and 3. That is the obvious next specimen and this object has none.
