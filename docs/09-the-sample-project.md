# 09 — the sample project: somebody's unfinished work, shipped by a publisher, and the person it is named after is credited in the editor's About box

*Measure: `python tools/projdiff.py
rpgmaker2003-steam/Sample/ArcheiaPictureTutorial --against
rpgmaker2003-steam/RTP`, in `notes/projdiff.txt`; `python tools/projjoin.py
<project> --rtp rpgmaker2003-steam/RTP`, in `notes/projjoin.txt`; `find
rpgmaker2003-steam -type d -empty`, in `notes/empty-dirs.txt`, analysed in
`notes/empty-dirs-analysis.txt`; `python tools/psd.py <the .psd> --resources`,
in `notes/psd.txt`; `python tools/pngchunk.py rpgmaker2003-steam --type tpNg
--expect 1 --dump`, in `notes/pngchunk-tpng.txt`; the string sweeps in
`notes/archeia.txt` and `notes/credits.txt`.*

---

## What is in there

`Sample\ArcheiaPictureTutorial\`, **47 files, 2,107,878 bytes — 6.2775 % of the
object — in 19 directories of which 15 are empty**, plus the two directories
above it, which is where copyverify's count of 21 in this subtree comes from.

`pc-rpgmaker95-doc/docs/05` had to argue from a manifest's group table that a
sample game was in the package and never saw a byte of it.
`pc-rpgmaker2000-doc` had none and said so. **This one ships one, complete and
playable**: a runtime, a runtime DLL, a database, a map tree, three maps, an
INI, a project file, twenty-four pictures, five chipsets, five face sets and
four window skins.

---

## Who Archeia is, and the pre-briefing said it was nobody

The pre-briefing wrote that `Archeia` is "in a directory name and nowhere else
in the object". **It is in `rpg2003.exe`, twice**, inside a Delphi form
resource that is the editor's About box:

```
python - (the sweep in notes/archeia.txt)
'archeia' case-insensitively over all 737 files
   rpg2003.exe    2
   total occurrences : 2

rpg2003.exe @3342664 .. @3342869, one TLabel after another:

   ^RPG Maker 2003  Version 1.12a
   Translated by:
       Jie Xin "Cy" Tan
       Jasmin "Archeia" Toral
   Localized and Improved by:
       David "Cherry" Trapp
       Jasmin "Archeia" Toral
```

**Three named human beings, all of them claiming credit in a dialogue box, and
one of them is the sample project's directory name.** The tutorial is not an
anonymous third party's file that a publisher swept up: it is the work of a
person the publisher credits by name and handle on the product's own About page,
and the directory name is that handle.

`David "Cherry" Trapp` is the same name the licence block in four binaries
names ([08](08-the-programs.md)), and `TFormCherrySpritesheet` is one of his
forms in the same resource section. **The credits, the licence and the export
table agree.**

**And the About box settles the third version notation.** `Picture_Tutorial.r3proj`
is sixteen bytes reading `RPG2003 v1.12a\r\n`; the binaries' version resources
say 1.1.2.1; `RPG_RT.ini` says `KnownVersion=281479271809025`, which is
`0x0001_0001_0002_0001` — four `u16` reading 1, 1, 2, 1. The About box reads
**`RPG Maker 2003  Version 1.12a`**. So `1.12a` is the product's own display
version, `1.1.2.1` is its file version, and the project file records the former.
Three notations, one product, all three now sourced.

Under the rule in `pc-rpgmaker2000-doc/docs/10` — *publish what claims credit and
redact what routes a message* — **a credits list is credit and is published in
full**. What is redacted about the same person is in [12](12-whose-bytes.md), and
it is not their name.

---

## Which files the author actually made

```
python tools/projdiff.py rpgmaker2003-steam/Sample/ArcheiaPictureTutorial \
    --against rpgmaker2003-steam/RTP

project files      : 47
same relative name : 14
only in the project: 33
byte-identical to the product's copy : 3 of 14
differing                            : 11 of 14
```

| file | project | RTP | verdict |
|---|---:|---:|---|
| `ChipSet\Dungeon.png` | 31,898 | 32,109 | DIFFERS |
| `ChipSet\Exterior.png` | 37,418 | 37,494 | DIFFERS |
| `ChipSet\Interior.png` | **55,746** | 34,926 | DIFFERS — *carries `cHRM`, `iTXt`, `pHYs`* |
| `ChipSet\Ship.png` | 30,723 | 30,787 | DIFFERS |
| `ChipSet\World.png` | 34,930 | 35,006 | DIFFERS |
| `FaceSet\Actor1.png` … `People2.png` | | | DIFFERS ×5 |
| `System\System.png` | 2,075 | 2,075 | identical |
| `System\SystemA.png` | 2,783 | 2,783 | identical |
| `System\SystemB.png` | **2,356** | **3,018** | **DIFFERS** |
| `System\SystemC.png` | 3,045 | 3,045 | identical |

**Three of the four window skins are byte-identical to the product's and the
fourth is not — and the fourth is the one the project's database selects.**
Chunk 22 field 19 reads `SystemB` in the project and `SystemC` in the default
([05](05-the-two-databases.md)). The author picked a skin and redrew it, and
left the three they did not use untouched.

**`ChipSet\Interior.png` is the only one that grew** — 55,746 against 34,926 —
and it is the only one carrying `iTXt`, which is an XMP packet. It was opened in
an image editor; the other nine differing files were re-saved.

---

## Where its references go, and the empty directories are the answer

```
python tools/projjoin.py rpgmaker2003-steam/Sample/ArcheiaPictureTutorial \
    --rtp rpgmaker2003-steam/RTP

references counted                 : 406
resolve INSIDE the project         : 14
resolve into the shared RTP        : 385
resolve NOWHERE                    : 7
the three sum to the total         : True
```

**The chipset chain is the one a stem threshold cannot find**, because it is an
integer resolved through a table into a name resolved into a file:

```
Map0001.lmu    chipset id 4 -> Dungeon    -> project/ChipSet/Dungeon.png
Map0002.lmu    chipset id 3 -> Interior   -> project/ChipSet/Interior.png
Map0003.lmu    chipset id 1 -> World      -> project/ChipSet/World.png
chipset chains that resolve : 3 of 3
```

A map's field 1 indexes database chunk 20; that entry's field 2 is a graphic
stem; **all three land on files the project ships**, and `Map0003` has no field 1
at all and therefore takes the default of 1 ([04](04-the-maps.md)).

The seven that resolve nowhere are named and none is a defect: five are enemy
*display* names in a field where stock enemies are usually named after their
pictures (the tool warns about exactly this and prints them below its
threshold), one is the chipset display name `Basic` whose graphic is `World`,
and **one is `(OFF)`** — the root map's music, which is not a missing file but
the spelling of silence.

### The fifteen empty directories

```
find rpgmaker2003-steam -type d -empty | wc -l     19
  under RTP     4      Battle2  Frame  Movie  Picture
  under Sample 15
```

Set the fifteen against where the project's references actually go:

| the project's directory | empty | the RTP has files | the project resolves references there |
|---|---|---|---|
| `Backdrop` | EMPTY | yes | **yes, 9 names** |
| `Battle` | EMPTY | yes | **yes, 26** |
| `BattleWeapon` | EMPTY | yes | **yes, 1** |
| `CharSet` | EMPTY | yes | **yes, 4** |
| `GameOver` | EMPTY | yes | **yes, 1** |
| `Monster` | EMPTY | yes | **yes, 115** |
| `Music` | EMPTY | yes | **yes, 3** |
| `Sound` | EMPTY | yes | **yes, 1** |
| `System2` | EMPTY | yes | **yes, 1** |
| `Title` | EMPTY | yes | **yes, 1** |
| `BattleCharSet` | EMPTY | yes | no |
| `Panorama` | EMPTY | yes | no |
| `Battle2` | EMPTY | **no — empty in the RTP too** | no |
| `Frame` | EMPTY | **no — empty in the RTP too** | no |
| `Movie` | EMPTY | **no — empty in the RTP too** | no |
| `ChipSet` | files | yes | — |
| `FaceSet` | files | yes | — |
| `System` | files | yes | — |
| `Picture` | **files** | **no — empty in the RTP** | — |

**Ten of the fifteen empty project directories are empty because the reference
went to the shared library instead.** An empty directory here is not a gap: it
is the visible trace of a resolution that landed elsewhere, and `projjoin.py`
names how many references landed there.

**Three more are empty because the product ships nothing of that kind either** —
`Battle2`, `Frame` and `Movie` are empty in `RTP\` as well
([07](07-what-does-not-cross.md)).

**And `Picture` is the one directory that runs the other way.** The product
declares `RTP\Picture` and ships nothing in it; the project's `Picture\` holds
**twenty-four files, every one of them the author's own**. The one place the
publisher left blank is the one place the tutorial fills.

---

## The twenty-four pictures, and the tutorial explains itself

```
INPUTDISPLAY.png   POLAROID.png   RTPHEROES[3, 3].png   magiccircle.png
RTPHERO_1..9.png   Zahl0..9.png   [BONUS]_POLAROID_BASE.psd
```

`RTPHEROES[3, 3].png` carries square brackets, a comma and a space in a file
name, which is the sort of thing that breaks tools and did not break any here.

**And the pictures are referenced from the maps**, by name, inside the event
command payloads:

```
Map0002.lmu @1670, @1846   'POLAROID'
Map0002.lmu @3873          'RTPHEROES[3, 3]'
Map0002.lmu @4638          'RTPHERO_1'
Map0002.lmu @6101          'INPUTDISPLAY'
Map0001.lmu @1714          'magiccircle'
```

**`Zahl` is German for *number*, and the object says so itself.** The project's
database carries the tutorial's own comment text, in English, written by its
author:

```
// This sets the coordinates of the pictures.
// We will now divide the variable's original value
// and store the remainder on a new variable using
// the modulus variable command.
// For example, number 1337. In order to display it
// via pictures, we need to be able to take each digit
// and separate them to 1 (thousands), 3(hundreds), 3(tens),
// Mod 10 will take only the rightmost digit, and /10 will
// remove the rightmost digit
// In this picture command, we're using Variable 11
// as a suffix. If you go to the pictures folder, you
// will find files with the name Zahl (German word for number).
// You will also notice they have numbers like Zahl0, Zahl1, etc.
// The purpose of this is so you don't have to create a
// long conditional branch to show each number.
// Break loop once 7 digits are displayed.
```

**The tutorial is about drawing numbers on screen with pictures, and the German
file names are deliberate and glossed by the author in the object itself.** The
nine named database entries of [05](05-the-two-databases.md) — `INPUT_NUMBER`,
`INPUT_X`, `INPUT_Y`, `DIGIT` — are the variables this text describes, and
`Zahl0`..`Zahl9` are the ten digits it draws with.

That is the sample project explaining its own naming, its own variables and its
own subject, out of a format nobody in this pipeline had opened before this
session.

---

## The `.psd`, which Adobe specified and nobody here had implemented

```
python tools/psd.py "<…>/Picture/[BONUS]_POLAROID_BASE.psd" --resources

signature   : 8BPS, version 1
channels    : 3        size : 196 x 123
depth       : 8 bits   colour mode : 3 = RGB
  section              at   declared
  header                0         26
  colour mode data     26          0
  image resources      30      21880
  layer and mask    21914      24664
  compression word  46582          2
  image data        46584       8069
  WALK LANDS AT 54653 of 54653      RESIDUE 0
  compression : 1 = RLE (PackBits)
```

**Colour mode 3 is RGB. The pre-briefing said indexed** ([14](14-corrections.md));
indexed is mode 2. The closure is stated as weaker than the ones on ITSF and
LCF, because the image data length is not declared by the format: this is *the
four declared sections fit and what remains is the image data*, not *the file
states its own total*.

Twenty-six image resource blocks, of which the largest is **16,892 bytes of
XMP**, and one is a 306-byte big-endian TIFF block reading `Adobe Photoshop CC
2017 (Windows)` and `2017:09:28 11:30:00`. The clocks are
[11](11-the-clocks.md).

---

## The two anomalous PNG chunks are in one file and it names its own writer

`pngcensus.py` reports, over 1,848 chunks in 355 files, **`tIME` 1, `tEXt` 1 and
`tpNg` 1**. All three are in the same file, and it is the project's:

```
python tools/pngchunk.py rpgmaker2003-steam --type tpNg --expect 1 --dump

file          : Sample/ArcheiaPictureTutorial/Picture/INPUTDISPLAY.png
chunk         : tpNg at byte offset 87, length 8
CRC declared  : c871abbc   CRC computed : c871abbc   VERIFIES
registered in the PNG specification : NO
payload       : 47 4c 44 33 00 00 00 00     |GLD3....|
```

**`tpNg` is in no PNG specification** and its CRC verifies like the other 1,847,
so it was written on purpose. **And the same file says who wrote it**, in the
registered chunk that exists for exactly that:

```
python tools/pngchunk.py <that file> --type tEXt --dump
payload : 53 6f 66 74 77 61 72 65 00 47 4c 44 50 4e 47 20 76 65 72 20 33 2e 33
as text : 'Software\x00GLDPNG ver 3.3'
```

**`Software = GLDPNG ver 3.3`, and the private chunk's payload is `GLD3`** — the
tool's own name and its major version, in a chunk type that is a scramble of
`PNG` with the private bit set and the reserved bit clear, which is a
well-formed ancillary private safe-to-copy chunk.

The attribution is from the object: a private chunk of unknown meaning, four
bytes into its payload, matched against a `Software` field in the same file.
The chunk's *contents* past `GLD3` are four zero bytes and this repository does
not claim to know what they would hold if they were not zero.

**It is the only file of 355 written by that tool**, which is why it is also the
only one with a `tIME`.

---

## What the project is, and what this repository will not say about it

**It is somebody's unfinished work, shipped.** Fifteen of its nineteen
directories are empty, its database has one hero where the default has fourteen,
and its whole subject is one technique. It is not a demo of the product's range;
it is a lesson.

What this repository does not do with it:

* **it does not treat the author as anonymous.** They are credited by name in
  the product's About box, and the credit is published;
* **it does not treat the author's machine as credit.** What the metadata leaks
  about them is redacted by program and argued in [12](12-whose-bytes.md);
* **it does not run it.** The project is playable and rule 4 stands. Everything
  above is a walk, a hash, a join and a string.
