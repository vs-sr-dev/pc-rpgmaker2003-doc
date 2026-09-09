# 01 — the object: 737 files of which half are already published next door, and the eight denominators that follow from it

*Measure: `python _work/copyverify.py`, in `notes/copyverify.txt`; `python
tools/hashall.py rpgmaker2003-steam`, in `notes/hashall.txt`; `python
tools/coverage.py tree --root rpgmaker2003-steam`, in `notes/coverage-tree.txt`.
Every percentage below names its denominator on the same line.*

---

## What it is

**RPG Maker 2003**, Steam app **362870**, published by **KADOKAWA GAMES**: the
licensed English re-release of a Japanese game-making tool, copied from the
owner's own installation and verified against it on four criteria. It is the
third consecutive object in one product family, after
[`pc-rpgmaker95-doc`](https://github.com/vs-sr-dev/pc-rpgmaker95-doc) (an
unauthorised translation) and
[`pc-rpgmaker2000-doc`](https://github.com/vs-sr-dev/pc-rpgmaker2000-doc)
(bought), and it is the first object in this collection **half of whose content
is already published in another repository**.

```
rpgmaker2003-steam/     737 files   33,578,445 bytes   41 directories, 19 empty
                        731 distinct sha1 over 737 files
copy verified           737/737 on size, on mtime to the 100-ns tick, on sha1
                        41 directories of 41, and 19 empty of 19
```

The copy program is the same one, retargeted by the same two constants, that
has run on thirteen objects. **Its fourth axis has something to do here for the
first time since it was written.** The previous object had thirteen directories
and none empty; this one has forty-one and nineteen. A file-by-file copy would
have lost nineteen directories and every per-file check would still have
reported 737 of 737.

```
python _work/copyverify.py

source files       : 737
source directories : 41, of which empty 19
size agrees             : 737 of 737
mtime agrees to 100 ns  : 737 of 737
sha1 agrees             : 737 of 737
directories, source     : 41   copy : 41   agree : True
empty directories       : 19   copy : 19   agree : True
```

---

## The shop closes against the tree twice

```
python tools/steamacf.py --path <steamapps>/appmanifest_362870.acf \
    --root rpgmaker2003-steam --check

SizeOnDisk declared      : 33578445
the tree, counted        : 33578445 over 737 files
residue                  : 0
installed depots:
   362871           33578445   manifest 837722761356681434
   residue against SizeOnDisk : 0
```

Build **2173406**, `LastUpdated` **1788949101**, `LastPlayed` **"0"**,
`BytesToDownload` **22,100,528** against `BytesToStage` **33,578,445**, and an
`InstallScripts` block naming `2k3_install.vdf` — which the previous object's
manifest did not have, and which `pc-rpgmaker2000-doc/docs/14` left open. **The
discrepancy resolves in favour of this object being normal.**

The tool's own warning is carried and is not softened: *a total that closes to
the byte says the tree weighs what Steam thinks it weighs. It is not a checksum.*
What the download figure is worth is measured in [03](03-the-shop.md).

`LastOwner` is a SteamID64 and the program redacts it. `LauncherPath` names a
directory on this machine and is not reproduced here either.

---

## The eight denominators

Every figure in this repository names which of these it is over.

| # | denominator | value | what it is for |
|---:|---|---:|---|
| 1 | files in the tree | **737** | anything counted per file |
| 2 | bytes in the tree | **33,578,445** | coverage, shares by format |
| 3 | directories | **41**, of which **19** empty | the shape, and [09](09-the-sample-project.md) |
| 4 | distinct sha1 | **731** | anything compared with another object |
| 5 | binaries | **9**, all PE32, 0 NE — 7,893,678 bytes | [08](08-the-programs.md) |
| 6 | the `RTP\` subtree | **676** files, 18,062,304 bytes | the shared library |
| 7 | the `Sample\` subtree | **47** files, 2,107,878 bytes | somebody's project |
| 8 | **hashes that do NOT cross** | **363** of 731, 19,984,119 bytes | **[07](07-what-does-not-cross.md)** |

**The eighth is the one that bites**, and it is new in this collection. 368 of
the 731 distinct hashes are already published by `pc-rpgmaker2000-doc`
([06](06-the-crossings.md)). A sentence about *what RPG Maker 2003 is* that
divides by 737 is dividing a numerator about the 2003 by a denominator that is
half the 2000.

The `Sample\` subtree adds a ninth reading that is not a denominator but a
warning: **47 of the 737 files are not the publisher's work at all**
([09](09-the-sample-project.md)).

---

## By directory — 22 rows carrying files, 19 empty, 41 in all

```
find rpgmaker2003-steam -type d | wc -l        # 42, counting the root
find rpgmaker2003-steam -type d -empty | wc -l # 19
```

| directory | files | bytes | of 33,578,445 |
|---|---:|---:|---:|
| `.` | 14 | 13,408,263 | 39.9312 % |
| `RTP\Sound` | 206 | 9,080,352 | 27.0422 % |
| `RTP\Music` | 151 | 4,292,221 | 12.7827 % |
| `RTP\Backdrop` | 34 | 1,687,238 | 5.0248 % |
| `Sample\ArcheiaPictureTutorial` | 9 | 1,544,945 | 4.6010 % |
| `RTP\Panorama` | 13 | 833,538 | 2.4824 % |
| `RTP\Monster` | 115 | 549,449 | 1.6363 % |
| `RTP\BattleCharSet` | 64 | 465,830 | 1.3873 % |
| `RTP\Battle` | 54 | 342,309 | 1.0194 % |
| `RTP\Title` | 4 | 269,386 | 0.8023 % |
| `Sample\…\Picture` | 24 | 227,622 | 0.6779 % |
| `Sample\…\ChipSet` | 5 | 190,715 | 0.5680 % |
| `RTP\ChipSet` | 5 | 170,322 | 0.5072 % |
| `RTP\CharSet` | 15 | 159,558 | 0.4752 % |
| `RTP\FaceSet` | 5 | 140,023 | 0.4170 % |
| `Sample\…\FaceSet` | 5 | 134,337 | 0.4001 % |
| `RTP\GameOver` | 1 | 27,367 | 0.0815 % |
| `RTP` | 1 | 23,558 | 0.0702 % |
| `RTP\System` | 4 | 10,921 | 0.0325 % |
| `Sample\…\System` | 4 | 10,259 | 0.0306 % |
| `RTP\BattleWeapon` | 1 | 5,665 | 0.0169 % |
| `RTP\System2` | 3 | 4,567 | 0.0136 % |
| | **737** | **33,578,445** | |

The nineteen empty directories are named and accounted for in
[09](09-the-sample-project.md): **four are the product's and fifteen are the
project's**, and they mean two different things.

---

## Six hashes are used twice, and two of them undo a disguise

The previous object had 477 distinct sha1 over 477 files. This one has **731
over 737**, and each of the six repeats is a statement.

```
python tools/hashall.py rpgmaker2003-steam
files 737  bytes 33578445  distinct sha1 731  unreadable 0
```

| bytes | one path | the other |
|---:|---|---|
| 1,032,704 | `rpg_rt.exe.dat` | `Sample\…\RPG_RT.exe` |
| 124,928 | `ultimate_rt_eb.dll.dat` | `Sample\…\ultimate_rt_eb.dll` |
| 3,045 | `RTP\System\SystemC.png` | `Sample\…\System\SystemC.png` |
| 2,783 | `RTP\System\SystemA.png` | `Sample\…\System\SystemA.png` |
| 2,075 | `RTP\System\System.png` | `Sample\…\System\System.png` |
| 52 | `RM2003 EN PRELIMINARY 13.09.2017.url` | `RPG Maker 2003.url` |

**The first two undo the object's own disguise with a hash.** The previous
session had to open a version resource to show that `rpg_rt.exe.dat` is an
executable calling itself `RPG_RT.exe`. Here the same bytes ship twice in one
tree, once as `.dat` and once as `.exe`, and sha1 says so without opening
either.

**And the three `System` PNG are three of four.** `SystemB.png` is *not* on that
list — 3,018 bytes in `RTP\` against 2,356 in the project — and it is exactly the
one the project's database selects ([05](05-the-two-databases.md)). The six
repeats also explain the shop's download figure ([03](03-the-shop.md)).

---

## The coverage, and the box was wrong about it until this session

```
python tools/coverage.py tree --root rpgmaker2003-steam
```

| bucket | files | bytes | of 33,578,445 |
|---|---:|---:|---:|
| specified | 730 | 26,534,548 | **79.0226 %** |
| decoded | 7 | 7,043,897 | **20.9774 %** |
| derived | 0 | 0 | 0.0000 % |
| opaque | 0 | 0 | 0.0000 % |
| **sum** | **737** | **33,578,445** | 100.0000 %, residue **0** |

**Before this session the same command printed 78.8598 % and put 67,623 bytes
in the wrong bucket**, because the classifier knew `LcfDataBase` and not
`LcfMapUnit`, `LcfMapTree` or `8BPS`. It closed at residue 0 while doing it,
which is the dangerous part. The three magics, the two different sentences that
have to be written about the two halves of those 67,623 bytes, and the
arithmetic are in [10](10-the-accounting.md).

The previous three objects started from 0.8387 %, 2.1516 % and 75.7882 %.

---

## Where the rest of this repository goes

The confirmations are worth a line each and are in `docs/00`'s §A: the `.chm`
opens with nine closures, both databases walk at residue 0, 355 PNG close and
1,848 CRCs verify, 141 MIDI close, 216 WAV close, 299 resource references
resolve. **None of that is a discovery on this object and none of it gets a
chapter.**

The work is in four places:

* **the four LCF map files nobody had opened** — 12,970 bytes, and the geometry
  they do not declare turns out to be forced ([04](04-the-maps.md));
* **the two databases, never compared** — 762,803 bytes of already-parsed
  structure, seventeen chunks byte-identical and five not
  ([05](05-the-two-databases.md));
* **half the tree being somebody else's chapter** — what that measures is a
  publishing decision ([06](06-the-crossings.md)), and what is left is the
  product ([07](07-what-does-not-cross.md));
* **the programs**, which name a compiler version, a hook library, a German
  developer and the missing middle of a corporate chain
  ([08](08-the-programs.md)).
