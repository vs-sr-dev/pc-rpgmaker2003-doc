# 00 — predictions: what you measure when half the object is already published in another repository and the readers for the rest were written last session

*Measure: `python tools/predcount.py` — the clause count and the two totals below
are that command's output and not a hand sum. This header was written from the
first run, before the first chapter, and regenerated from a second run after the
last chapter; both runs agree. The verdicts are in the last chapter of this
repository.*

```
document      : docs/00-predictions.md
clauses        : 63
  inherited    : 31
  open         : 32
  method       : 5
  content      : 58

the cross-tabulation, which is the one that matters:
  inherited method  : 0
  inherited content : 31
  open      method  : 5
  open      content : 27

TWO TOTALS, NEVER SUMMED TOGETHER:
  inherited predicted : 28.61 of 31
  open      predicted : 23.31 of 32

content share of the open clauses : 27 of 32 = 84.4 %
```

And the three P11 bands, which are the split the scoring chapter has to report:

```
lands       n= 7  total  5.29  mean 0.7557   C38 C42 C46 C48 C54 C55 C62
constructs  n=12  total  7.04  mean 0.5867   C37 C39 C40 C41 C43 C44 C45 C49 C53 C56 C57 C61
nonnumeric  n= 8  total  6.53  mean 0.8163   C47 C50 C51 C52 C58 C59 C60 C63

open content clauses priced below 0.60 : 5   C37=0.45 C39=0.50 C41=0.35 C43=0.40 C45=0.55
```

This document was written after `prompt.txt` and the eight files of `_pre\` were
read; after `pc-rpgmaker2000-doc/docs/15` and its **P11**, **P12** and **P13**
were read in the original, along with that repository's `docs/09` for the four
coverage buckets, `docs/10` for the personal-data rule, `docs/12` for the
classification of refusals and `docs/06` for the chapter this object confirms;
after the collection's two directory counts were re-derived with `ls`; after
`tools\` was counted; and **before** one byte of any `.lmu` or the `.lmt` past
the sixteen the pre-briefing quotes, before either LCF database was read past
its top-level chunk table, before `ultimate_eb.dll` or `ultimate_rt_eb.dll` was
opened past its version resource, before the `tIME` and `tpNg` chunks were
located, and before the `.psd` was read past its 26-byte header.

Everything in §A is the pre-briefing's work and scores nothing. §B is the
calibration series, re-derived here by command. Everything from C01 on is priced
from the brief and is scored in the last chapter whether it was right or not.

**The three prescriptions that govern this document**, all from
`pc-rpgmaker2000-doc/docs/15`, are followed literally and each is named where it
bites.

> **P11 — test the pricing rule against the clause text rather than against the
> score.** For each open content clause, record whether the object turned out to
> support **more** than the clause asked, exactly what it asked, or less.
> **Falsification: if `lands` and `constructs` have the same over-delivery rate
> on that measure, P8's mechanism is dead and not merely untestable.** The
> previous session's rates were 6 of 10 and 5 of 8 — a tie — and P11 predicts
> the next session will break it.

**Implemented.** Every open content clause below carries a third tag —
`lands`, `constructs` or `nonnumeric` — and the scoring chapter reports, for
each of the first two bands, how many clauses the object **over-delivered**
against. **This object is a hard test of P11 and the reason should be stated
before the result**: a large part of this object's substance is already
documented next door, and a clause that asks for a *confirmation* of something
the predecessor established cannot over-deliver by very much. If the two rates tie again,
that is P11's falsification and it will be reported as one rather than explained
away.

> **P12 — price the floor out.** Write, for at least five open content clauses,
> the strongest claim the object could conceivably support rather than the one
> you are confident of — a specific count, a specific closure, a named second
> witness — and price those five **below 0.60**. **Falsification: if all five
> hit, the pipeline was under-claiming rather than under-pricing.**

**Followed, and the five are named here so the scoring chapter cannot choose
them afterwards: C37, C39, C41, C43 and C45**, priced at **0.45, 0.50, 0.35,
0.40 and 0.55**, which `predbands.py --expect-under 0.60 5` verifies by
command. Each asks for something this document does not believe it will
get: a map format decoded to named dimensions that join against the files the
project ships; a database diff that names a record a human being edited; the
`eb` question settled from the bytes; the `tpNg` chunk decoded and attributed;
and the 13-versus-16 September question decided by a third witness. **No other
open content clause is priced under 0.60**, so the band is exactly five and the
test is clean.

> **P13 — do not write the rule-0 clause; make the failure impossible.** No
> heredoc for any content, ever, with `Write` to a scratch file as the only
> route. **Falsification: if C29's successor still fails under that rule, the
> problem is not the heredoc and the diagnosis has been wrong four times.**

**Followed exactly, and it is why there are five method clauses below and not
six.** The previous five documents each carried a discipline clause about rule-0
violations; this one does not, because P13 says the clause is not the
instrument. Every file this session writes with any content in it — documents,
tools, scratch scripts, notes — is written with `Write` and never with a shell
heredoc, and the scoring chapter reports, as a plain fact and not as a clause,
whether a rule-0 violation occurred. **That report is P13's falsification and it
is worth zero points either way.**

**And the standing rule from `pc-academagia-doc/docs/18` is still in force:**
never quote a percentage inside a clause; state the byte count and the
denominator and let the share be computed. Where a percentage appears below it
is a figure the pre-briefing published and the clause is testing that
publication.

---

## §A — the pre-briefing, which is worth zero points

**The object is a live installation, copied.** `rpgmaker2003-steam\`, **737
files, 33,578,445 bytes, 41 directories of which 19 are empty**, and **731
distinct sha1 over 737 files**. It is **RPG Maker 2003**, Steam app **362870**,
published by **KADOKAWA GAMES**, copied from the owner's own Steam
library on this machine — the path is not reproduced, per rule 7 —
and verified against the source on four axes: **737 of 737 on size, 737 of 737
on mtime to the 100-nanosecond tick, 737 of 737 on sha1, 41 directories of 41
and 19 empty of 19**. `copyverify.py` was retargeted by the same two constants
it has been retargeted by for thirteen objects.

**The fourth axis is load-bearing for the first time since it was written.** The
previous object had 13 directories and zero empty; this one has 41 and
**nineteen**. A file-by-file copy would have lost nineteen directories and every
per-file check would still have said 737 of 737.

**It is the third consecutive object of one product family** — after
`pc-rpgmaker95-doc` (an unauthorised translation, 1999) and
`pc-rpgmaker2000-doc` (bought, 2017) — and **142.78 % of the previous object's
bytes and 154.51 % of its files**.

**The shop closes at residue 0 twice.** `appmanifest_362870.acf` declares
`SizeOnDisk` **33,578,445**; the tree counted is **33,578,445**, residue **0**;
the single depot **362871** declares **33,578,445** against manifest
`837722761356681434`, residue **0**. Build **2173406**, `LastUpdated`
**1788949101** — two seconds before the previous object's 1788949103, because
Steam wrote both trees in the same minute — `LastPlayed` **"0"**, `UserConfig`
language `english`, `BytesToDownload` **22,100,528** against `BytesToStage`
**33,578,445**, a ratio of **1.5194** against the previous object's 1.3355.
**And this manifest has an `InstallScripts` block naming `2k3_install.vdf`,
which the previous object's did not** — `pc-rpgmaker2000-doc/docs/14` left that
discrepancy open and this object is the one that behaves normally.

**Six hashes are used twice**, where the previous object had 477 of 477
distinct: the two 52-byte `.url` files; `rpg_rt.exe.dat` against
`Sample\…\RPG_RT.exe` at 1,032,704; `ultimate_rt_eb.dll.dat` against the
Sample's at 124,928; and three PNG of `RTP\System` against the Sample's, at
2,075, 2,783 and 3,045. **The second and third undo the object's own disguise
with a hash**: the previous session needed a version resource saying
`OriginalFilename RPG_RT.exe`, and here the same bytes ship twice in one tree,
once as `.dat` and once as `.exe`.

**By directory, 22 rows with files over 41 directories**, summing to 737 and
33,578,445: `.` 14 / 13,408,263; `RTP\Sound` 206 / 9,080,352; `RTP\Music` 151 /
4,292,221; `RTP\Backdrop` 34 / 1,687,238; `Sample\ArcheiaPictureTutorial` 9 /
1,544,945; `RTP\Panorama` 13 / 833,538; `RTP\Monster` 115 / 549,449;
`RTP\BattleCharSet` 64 / 465,830; `RTP\Battle` 54 / 342,309; `RTP\Title` 4 /
269,386; `Sample\…\Picture` 24 / 227,622; `Sample\…\ChipSet` 5 / 190,715;
`RTP\ChipSet` 5 / 170,322; `RTP\CharSet` 15 / 159,558; `RTP\FaceSet` 5 /
140,023; `Sample\…\FaceSet` 5 / 134,337; `RTP\GameOver` 1 / 27,367; `RTP` 1 /
23,558; `RTP\System` 4 / 10,921; `Sample\…\System` 4 / 10,259;
`RTP\BattleWeapon` 1 / 5,665; `RTP\System2` 3 / 4,567. **Three subtrees**: `RTP\`
676 files / 18,062,304 bytes, `Sample\` 47 / 2,107,878, the root 14 /
13,408,263. **`RTP\` has twenty subdirectories against the previous object's
twelve, and four of them — `Battle2`, `Frame`, `Movie`, `Picture` — are empty:
the product declares directories for resource kinds it ships none of.**

**By extension, seventeen rows against the previous object's eleven**: `.wav`
216 / 10,426,824; `.chm` 1 / 6,268,124; `.exe` 3 / 5,467,822; `.png` 355 /
5,174,453; `.mid` 141 / 2,945,749; `.dat` 4 / 2,176,990; `.dll` 3 / 637,440;
`.ldb` 1 / 374,229; `.psd` 1 / 54,653; `.ico` 1 / 23,558; `.txt` 2 / 13,870;
`.lmu` 3 / 12,635; `.vdf` 1 / 1,545; `.lmt` 1 / 335; `.url` 2 / 104; `.ini` 1 /
98; `.r3proj` 1 / 16. **`.dat` still lies and now three of its four files do**:
`rpg_rt.exe.dat`, `setup.exe.dat` and `ultimate_rt_eb.dll.dat` are PE32 and only
`rpg_rt.ldb.dat` at 388,574 is data.

**The free coverage the box prints is wrong and the pre-briefing says so.**
`coverage.py tree` reports **specified 729 / 26,479,895 / 78.8598 %, decoded 3 /
7,030,927 / 20.9388 %, derived 0, opaque 5 / 67,623 / 0.2014 %**, residue 0.
**The five opaque files are a gap in the tool and not in the world**: `RPG_RT.lmt`
at 335, three `.lmu` at 2,752 / 7,469 / 2,414, and a `.psd` at 54,653 whose
format **Adobe published**. With three magics — `8BPS`, `LcfMapUnit`,
`LcfMapTree` — the table becomes **specified 730 / 26,534,548 / 79.0225 %,
decoded 7 / 7,043,897 / 20.9775 %, opaque 0**. **79.0225 % is the starting
coverage**; the previous object started at 75.7882 %, and the two before that at
0.8387 % and 2.1516 %.

**Entropy**: `--tree --by-ext` reports 737 files, 33,578,445 bytes, **432 of
1,041 blocks above 7.5**, seventeen extension rows, `.CHM` highest at **7.9980**
and `.R3PROJ` lowest at **3.6250**, with `.PNG` 7.6838, `.WAV` 7.1718, `.DLL`
6.5023, `.DAT` 6.3158, `.TXT` 6.2756, `.EXE` **5.8084 with zero blocks above
7.5**, `.VDF` 5.5108, `.MID` 5.5135, `.PSD` 5.3420, `.LMU` 5.2733, `.LDB`
5.1803, `.INI` 5.0434, `.URL` 4.5560, `.LMT` 4.2901, `.ICO` 4.0597.

**Nine binaries, all PE32, zero NE**, found by magic including the three named
`.dat`: `rpg2003.exe` 4,387,328 linker 2.25 stamp 1992-06-19 22:22:17 stub
`MZP`; `rpg_rt.exe.dat` 1,032,704 the same; `Sample\…\RPG_RT.exe` 1,032,704 the
same bytes; `setup.exe.dat` 630,784 the same; `ultimate_eb.dll` 274,944 linker
2.24 stamp **1970-01-25 06:32:32**; `UNLHA32.DLL` 237,568 linker 3.00 stamp
2000-03-01 02:30:53; `ultimate_rt_eb.dll.dat` 124,928 linker 2.24 stamp
**1970-01-01 18:12:16**; the Sample's copy of it; and
`BaseFlushAppcompatCache.exe` 47,790 linker 6.00 stamp 2009-12-05 22:50:52.
`ne.py` refuses cleanly: `no NE signature at e_lfanew=256 (found b'PE')`.

**Five of the nine stamps are false and `pecensus.py` prints `impossible mtimes
: 0 of 9`.** Four are the 1992 Borland constant and **two are powers of two —
`0x00200000` and `0x00010000`, exactly 2 MiB and 64 KiB as integers**. The
previous session's proposed second test — *do two files of different sizes share
a stamp to the second* — would catch three of these and **miss both powers of
two**. **And `pecensus.py` truncates a long path from the left**, printing
`mple/ArcheiaPictureTutorial/ultimate_rt_eb.dll`.

**Six version resources of nine PE.** `rpg2003.exe`: KADOKAWA GAMES, *RPG Maker
2003 Editor*, **1.1.2.1**, `LegalCopyright` and `OriginalFilename` empty.
`rpg_rt.exe.dat`: *RPG Maker 2003 Runtime*, **1.1.2.1**, `OriginalFilename
RPG_RT.exe`. `ultimate_eb.dll`: **Ultimate DLL (RM2k3 custom version for
Degica)**, 1.1.2.1. `ultimate_rt_eb.dll.dat`: **Ultimate Runtime DLL (RM2k3
custom version for Degica)**, 1.1.2.1. `UNLHA32.DLL`: `CompanyName` **empty**,
*LZH file processing library*, **1.47.1.7-VC**, `(C)Micco 1995-2000`. **The
editor and the runtime agree**, where the previous object's disagreed 1.6.2.0
against 1.6.1.0. **Degica is named twice in a field a compiler wrote**, and it
is a ninth party.

**The LHA library is older than the previous object's.** 237,568 bytes at
1.47.1.7-VC and `(C)Micco 1995-2000` here, against 254,464 at 1.87.0.2 and
1995-2002 there, against 151,552 at 0.71.0.5 and 1995-97 on the 95. **The newer
product ships the older library**, and it is the third consecutive object with
the same author's code that does not cross.

**Fifteen build paths in one binary, and the previous object had none.**
`sift.py --group buildpath` finds **17 drive-letter hits in 3 files** — one NSIS
default in `BaseFlushAppcompatCache.exe`, `C:\TMP\UNLHA32.LOG` in `UNLHA32.DLL`,
and **fifteen occurrences of ten distinct paths in `rpg2003.exe`**:
`D:\ha\02rpg2000\2003\RPG_RT\AuroraSheet.pas` ×2, `…\MapEditUtils.pas` ×4,
`…\LD_Event.pas`, `…\GR_ChipSet.pas`, `D:\ha\02rpg2000\2003\MapEditor.pas`,
`…\ED_Player2.pas` ×2, `…\ED_Player.pas`, `…\ED_Job.pas`, `…\ED_MoveRoute.pas`
and `…\RPG2003.hlp`. **Eight Delphi source units**, where the previous object
had to infer Delphi from a `TPF0` resource; **`02rpg2000\2003` says the 2003 was
built inside a tree named after the 2000**; **`RPG2003.hlp` is WinHelp in a
product that ships a `.chm`** and is not in the object; and `D:\ha\` is a third
party's build root, which the standing rule publishes.

**The container inside a binary, again.** `sigcount.py --hex 4d5a5000`: **4 of
737 files begin with `MZP`, 5 occurrences in 4 files**. `peembed.py
setup.exe.dat`: highest raw end 630,784 against a file length of 630,784,
**residue 0**; an MZ that parses as PE at offset 483,728, inside the outer
image's `.rsrc`, reaching 142,848, at a resource entry
**`RCDATA/GAMEDELETE/9`** declaring 142,848, **residue 0**. The previous object's
was at a different offset, 76,800 bytes, language id `0`.

**`mzcensus.py`, tenth appearance, reports 3 of 9** and misses **2,425,856
bytes**, which is a worse fraction than the previous object's 2 of 5. Its
`e_cblp` section still notices `MZP`: `0 of 3 agree`, `byte2=0x50 ('P')`.

**The `.chm` opens unchanged and closes nine times.** `itsf.py` on
`rpg2003.chm`: version 3, header length 96; 96 + 24 = 120 against a directory
offset of 120; 120 + 16,468 = 16,588 against a content offset of 16,588; header
section 0's three u64 are (510, **6,268,124**, 0) and the second is the file's
own length; chunk count 4 at chunk size 4,096 with 84 + 4 × 4,096 = 16,468;
chunk tags `PMGL PMGL PMGL PMGI`; **530 listing entries, 3 index entries, 0
refusals**; 16,588 + 6,562 + 6,244,974 = 6,268,124; `ResetTable` 40 + 264 × 8 =
2,152; and `SpanInfo`, `ResetTable` and 518 section-1 entries all saying
8,623,119. **Four chunks against five, 264 reset blocks against 252, 530
directory entries against 475** — the fields are fields. `internals` reports
`/#SYSTEM` code 10 at **2017-09-16 19:54:13 UTC**, code 4 at **19:53:55.521294**,
the paired header `u32` at **19:53:55.528845** — **7.551 ms apart, the third
specimen of that derivation** — compiler **HHA Version 4.74.8702**, title **RPG
Maker 2003**, compiled name **rpg2003_en**.

**And the file name disagrees with the container by three days.** The object
ships `RM2003 EN PRELIMINARY 13.09.2017.url` and `RPG Maker 2003.url`, 52 bytes
each and **byte-identical to each other and to the previous object's
shortcut**. **13 September in the name, 16 September in the help file.**

**Two LCF databases, and the reader opens both unchanged.** `lcf.py walk` on
`rpg_rt.ldb.dat` (388,574) and on `Sample\…\RPG_RT.ldb` (374,229): header name
`LcfDataBase`, **22 top-level chunks each**, tags **11..32** strictly ascending,
**residue 0**, shapes `{'LIST': 15, 'RECORD': 3, 'SCALAR': 4}`, and **zero
chunks where both readings close**, where the previous object had one ambiguity
that had to be settled by an invariant. **Twenty-two chunks against sixteen: six
new tags, 27 to 32.** The two files have never been diffed.

**Four LCF files nobody has opened.** `RPG_RT.lmt` 335 bytes, opening `0a
"LcfMapTree"` and running straight into a length-prefixed `Picture Tutorial`
which is also what `RPG_RT.ini` says the game is called; `Map0001.lmu` 2,752,
`Map0002.lmu` 7,469 and `Map0003.lmu` 2,414, each opening `0a "LcfMapUnit"`.
**12,970 bytes, 0.0386 % of the object, and three specimens of one format at
once.**

**One `.psd`.** `[BONUS]_POLAROID_BASE.psd`, 54,653 bytes, `8BPS` version 1, **3
channels, height 0x7B = 123, width 0xC4 = 196, depth 8, colour mode 3**.

**The resource library, censused and closing three times.** `pngcensus.py`:
**355 of 355 parsed, 0 refused, 355 of 355 closing at residue 0, 1,848 chunks
walked, 1,848 of 1,848 CRC-32 verifying**, every file depth 8 colour type 3
non-interlaced, **231 distinct palettes over 355**, 127 distinct dimensions,
**349 distinct IDAT streams over 355**, and fourteen chunk types — `IDAT` 462,
`IHDR` 355, `PLTE` 355, `IEND` 355, `cHRM` 138, `gAMA` 128, `pHYs` 27, `iTXt`
10, `tRNS` 6, `sBIT` 5, `iCCP` 4, **`tIME` 1**, `tEXt` 1, **`tpNg` 1**.
**`tpNg` is in no PNG specification and its CRC verifies like all the others.**
`smfcensus.py`: **141 of 141, residue 0, 1,963 tracks, 797,748 events,
10,435.682 s**, meta types `{'name': 1317, 'copyright': 83, 'marker': 58,
'text': 3}` — **83 copyrights of which 62 read `(C)2000 by ASCII
Corp./Y.Kitagami` and 21 a Shift-JIS line naming Daisuke Shiiba**, and **58
marker events in five spellings** where the previous object's 92 files had none.
`wavcheck.py`: **216 of 216**, the container closing on the file 216 of 216,
**157 × 16-bit and 59 × 8-bit, all mono at 22,050 Hz**, total 263.486349206 s,
chunk orders `fmt+data` 178, `fmt+fact+data` 36, `fmt+cue+LIST+data` 2.
`rtpjoin.py`: **299 of 299** resource references resolve, residue 0, **18 of 299
ambiguous** against the previous object's 45 of 208.

**The crossings, and they break the collection's scale.** `crossall.py
_work/sha1-all.txt --collection .. --skip pc-rpgmaker2003-doc`: **368 of 731 =
50.3420 %**, over **104 repositories, 461 list files and 155,888 hash tokens**,
**all 368 with `pc-rpgmaker2000-doc` and none with anything else**, 12,428,739
bytes. The collection holds **134** `*-doc` directories and **65** `pc-*-doc`,
both including this one. The previous rates were 8.3333 %, 1.0395 % and **0 of
477**. The breakdown: **`.wav` 211 files / 9,661,794 bytes — all 211 of the
previous object's; `.mid` 92 / 1,431,351 — all 92; `.png` 63 / 1,287,752 — 63 of
its 162; `.exe` 1 / 47,790; `.url` 1 / 52.** **Every sound effect and every
piece of music in RPG Maker 2000 is in RPG Maker 2003, byte for byte.**

**And 277 of the 368 carry the same base name while 91 do not**: fifty insert a
space before a trailing number (`Boss1.mid` → `Boss 1.mid`), three add an `SE`
prefix (`Sea.wav` → `SESea.wav`, `Rain1.wav` → `SERain.wav`, `Rain2.wav` →
`SEDownpour.wav`), and **thirty-eight are a different English translation of the
same bytes** — `Devil` → `Demon Lord`, `Anger` → `Wrath`, `Crisis` → `In a
Pinch`, `Peace1..3` → `Repose 1..3`, `Store1..3` → `Shop 1..3`, `Farewell1..2` →
`Parting 1..2`, `Search` → `Exploration`, `Gameover1..3` → `Game Over 1..3`.
**And seventeen confirm a reading the previous session derived**:
`pc-rpgmaker2000-doc/docs/06` established from durations alone that a `J` in a
MIDI file's internal Shift-JIS sequence name marks a jingle — seventeen with the
`J` at at most 15.63 s, seventy-five without at at least 29.57 s — and **here the
`J` is in the file names, on exactly those seventeen**: `JFanfare 1..6`,
`JEnd of Battle 1..4`, `JInn 1..2`, `JJoke 1..2`, `JItem`, `JMystery`, `JDoubt`.

**A sample project, which neither predecessor had.**
`Sample\ArcheiaPictureTutorial\`, **47 files, 2,107,878 bytes, 6.2775 %, 21
directories of which fifteen are empty** — a runtime, a database, three maps, a
title, twenty-four pictures and a `.psd`. `RPG_RT.ini` says `GameTitle=Picture
Tutorial`; `Picture_Tutorial.r3proj` is sixteen bytes reading **`RPG2003
v1.12a`**; `KnownVersion=281479271809025` is `0x0001_0001_0002_0001`, four u16
reading 1, 1, 2, 1, agreeing with the binaries' 1.1.2.1. **Ten of its pictures
are called `Zahl0.png`..`Zahl9.png` — German for *number* — and one is
`RTPHEROES[3, 3].png`.** `pc-rpgmaker95-doc/docs/05` had to argue a sample game
existed from a manifest's group table and never saw a byte of it.

**The install script is twice the size and signed.** `2k3_install.vdf`, **1,545
bytes** against 753, writing `HKEY_CURRENT_USER\Software\KADOKAWA\rpg2003`,
registering **`.r3project` → `RPG2003.Project`** with a `DefaultIcon` and a
`shell\open\command` — **while the file the object ships is `.r3proj`** — the
same DEP shim in both hives, and a **`kvsignatures` block of 256 hexadecimal
digits, which is 128 bytes, the size of an RSA-1024 signature**, which the
previous object's script did not have.

**The clocks.** `mtimes.py --waves`: **one wave, 2026-09-09 12:18:11 ..
12:18:20, 737 files, 33,578,445 bytes, 100.00 %** — nine seconds against the
previous object's fourteen. No original timestamp survives.

**The personal data is the same man and not the same addresses.** `sift.py
--group personal`: **3 e-mail shapes in 1 blob**, all in `UNLHA32.TXT`,
**`GCH03345@nifty.ne.jp` twice and a second address at a different Japanese
provider once** — where the previous object had `micco@mbd.nifty.com` twice and
`GCH03345@nifty.ne.jp` once. `UNLHA32.TXT` is 13,864 bytes here documenting
version 1.47 against 17,649 there documenting 1.87. Positive control fired,
negative control quiet. `utf16sift.py` finds **0** hits a sixteen-bit pass alone
would find. `LastOwner` is redacted by `steamacf.py` by program.

**Nine parties**: KADOKAWA GAMES (4 version resources, 1 registry key),
**Degica** (2 `FileDescription` fields, new and Western), ASCII Corporation and
**Y. Kitagami** (62 MIDI copyrights, inherited bytes), **Daisuke Shiiba** (21, in
Shift-JIS, new), Micco (1 version resource, 1 manual, 2 addresses), Borland (4
`MZP` stubs, ten `.pas` paths), Nullsoft, and Microsoft/Adobe/W3C/MMA/Valve for
the formats and the shop. **`LegalCopyright` is empty on every Kadokawa binary.**

**`protscan.py`, seventeenth appearance**: **9 files of 737 and 7,893,678 bytes
of 33,578,445**, 0 hits on eleven pre-2010 optical markers, control firing on 9.

**Twenty-three tools of 528 were run, which is 4.3561 % of the box** —
`copyverify.py`, `hashall.py`, `steamacf.py`, `entropy.py`, `coverage.py`,
`pecensus.py`, `ne.py`, `verres.py`, `mzcensus.py`, `peembed.py`, `itsf.py`,
`lcf.py`, `pngcensus.py`, `smfcensus.py`, `wavcheck.py`, `rtpjoin.py`,
`sift.py`, `utf16sift.py`, `protscan.py`, `mtimes.py`, `crossall.py`,
`sigcount.py`, `namecensus.py`, `dircensus.py` and `toolscan.py`, which reports
**528 Python files and 0 forbidden bytes** with all three controls firing.
`namecensus.py` crashed with `ZeroDivisionError`, **twenty-first appearance**;
`dircensus.py` printed a complete table over `Director containers found : 0` and
exited 0, **twenty-second**.

**And the position is new.** ITSF, LCF, PNG, MIDI, RIFF WAVE, PE and the
resource join all work **unchanged**, and between them they account for
**33,510,822 of 33,578,445 bytes — 99.7986 %**. What has no reader in the box is
**five files and 67,623 bytes**, and the two halves are different things:
**12,970 bytes in four LCF files no vendor ever specified**, and **54,653 bytes
in a `.psd` whose format Adobe published and nobody here has implemented.**

---

## §B — the calibration series, re-derived

```
python <the thirty-four terms, in order, summed>
+10.50  +7.50  +5.00  +2.00 -14.00  -2.00  +9.00   0.00 +19.75
 +5.25  -4.10  -3.40  +9.30  +1.05  -2.50  -3.57  -2.50  -0.35
 -3.85  -4.95  -4.70  +0.70  -2.40  -2.12  -3.57  -3.88  -3.87
 -2.92  -8.89  -5.93  +0.51  -7.57  -0.42  -1.79

terms    : 34
sum      : -18.7200
mean     : -0.5506
negative : 22   positive : 11   zero : 1
last8    : -30.8800   mean -3.8600
last10   : -38.3300   mean -3.8330
consecutive negatives at the tail : 3
rank of the last term (-1.79) by absolute value : 7 of 34

the brief's own eight claims about the series, checked one by one : 8 OK, 0 wrong
```

**The brief is right in all eight figures it gives** — thirty-four terms,
−18.72, −0.5506, twenty-two negatives, one zero, last ten −38.33 at −3.8330, and
a tail run of three. The last-eight mean, which the brief does not give, is
−3.8600.

**The tail run is three and that is the fact this document has to price
against.** The previous session's run was two and it said so explicitly, because
`+0.51` was three terms back; that `+0.51` is now four back and the run has
lengthened. Three consecutive negatives after a session that priced *upward* on
P6 and a session that priced by *bands* on P8 means neither instrument has
stopped the drift.

**So this document does neither.** It follows P12, which is a different
instrument again: **it does not raise the mean, it raises the claim**. The
twelve `constructs` clauses come to a mean of **0.5867**, which is lower than
anything this pipeline has priced, and that is deliberate — five of them ask for
things this document does not expect to get. **If the open total comes back
strongly positive, P12's falsification has fired and the diagnosis of the last
ten terms was wrong.**

**Where this document deliberately prices high**: the inherited band, at a mean
of **0.9229** over thirty-one clauses, because the pre-briefing has already run
every one of those commands and the only question is whether re-running them
reproduces the figures. **Where it deliberately prices low**: the four map
files, the database diff, the `eb` question, the `tpNg` chunk and the September
question — the five things nobody has looked at.

---

## §C — the clauses

### Inherited — re-testing the pre-briefing's own figures

**C01** `content` `inherited` — `copyverify.py` re-run against the live source
tree closes on **four axes**: **737 source files and 737 copied**, **737 of 737
on size**, **737 of 737 on mtime to the 100-nanosecond tick**, **737 of 737 on
sha1**, **41 directories against 41** and **19 empty against 19**, and it prints
a single final agreement of `True`. *Predicted: 0.96*

**C02** `content` `inherited` — `hashall.py` re-run reports **737 files,
33,578,445 bytes, 731 distinct sha1 and 0 unreadable**; the byte total is
re-derived by a command that is not `hashall.py`; and the **six** hashes that
appear twice are the two 52-byte `.url` files, `rpg_rt.exe.dat` against
`Sample\…\RPG_RT.exe` at **1,032,704**, `ultimate_rt_eb.dll.dat` against the
Sample's at **124,928**, and three `RTP\System` PNG against the Sample's at
**2,075**, **2,783** and **3,045**. *Predicted: 0.95*

**C03** `content` `inherited` — `steamacf.py --check` against
`appmanifest_362870.acf` reports `SizeOnDisk` **33,578,445** against a counted
tree of **33,578,445** at residue **0**, and one installed depot **362871** at
**33,578,445** with manifest `837722761356681434` and residue **0**; build id
**2173406**, `LastUpdated` **1788949101**, `LastPlayed` **"0"**,
`BytesToDownload` **22,100,528**, an `InstallScripts` block naming
**`2k3_install.vdf`**, and `LastOwner` redacted by the program without this
session touching it. *Predicted: 0.94*

**C04** `content` `inherited` — the by-directory census has **22 rows carrying
files over 41 directories of which 19 are empty**, the 22 file counts sum to
**737** and the 22 byte totals to **33,578,445**, `.` holds **14 files and
13,408,263 bytes**, `RTP\Sound` holds **206 and 9,080,352**, and the three
subtrees are `RTP\` at **676 files and 18,062,304 bytes**, `Sample\` at **47 and
2,107,878** and the root at **14 and 13,408,263**. *Predicted: 0.93*

**C05** `content` `inherited` — the by-extension census has **seventeen rows**,
the seventeen counts sum to **737** and the seventeen byte totals to
**33,578,445**, and the four largest rows are `.wav` **216 / 10,426,824**,
`.chm` **1 / 6,268,124**, `.exe` **3 / 5,467,822** and `.png` **355 /
5,174,453**; **three of the four `.dat` files are PE32** and only
`rpg_rt.ldb.dat` at **388,574** is data. *Predicted: 0.93*

**C06** `content` `inherited` — `coverage.py tree` **as it stands** prints
**729 files and 26,479,895 bytes specified, 3 files and 7,030,927 decoded, 0
derived and 5 files and 67,623 bytes opaque**, closing at residue **0**, and the
five opaque files are `RPG_RT.lmt` at **335**, three `.lmu` at **2,752**,
**7,469** and **2,414**, and one `.psd` at **54,653**. *Predicted: 0.94*

**C07** `content` `inherited` — `entropy.py --tree --by-ext` re-run reports
**737 files, 33,578,445 bytes and 432 of 1,041 blocks above 7.5**, with
**seventeen rows**, `.CHM` highest at **7.9980** and `.R3PROJ` lowest at
**3.6250**, and **`.EXE` at 5.8084 with zero blocks above 7.5** against the
previous object's 6.6301 with three. *Predicted: 0.91*

**C08** `content` `inherited` — `pecensus.py --by-magic` re-run reports **9
binaries, PE32 9, NE 0**, finds all nine **by magic including the three named
`.dat`**, gives linker versions **2.25 ×4, 2.24 ×3, 3.00 and 6.00** against byte
counts 4,387,328 / 1,032,704 / 1,032,704 / 630,784 / 274,944 / 237,568 / 124,928
/ 124,928 / 47,790, and `ne.py` refuses cleanly with **`no NE signature at
e_lfanew=256 (found b'PE')`**. *Predicted: 0.93*

**C09** `content` `inherited` — `pecensus.py` prints **`impossible mtimes : 0 of
9`** while **five of the nine COFF stamps are false**: four are the identical
Borland constant **1992-06-19 22:22:17** and two are **`0x00200000` and
`0x00010000`**, which are exactly **2,097,152** and **65,536** as integers, and
the two are on `ultimate_eb.dll` and on both copies of
`ultimate_rt_eb.dll`. *Predicted: 0.93*

**C10** `content` `inherited` — `pecensus.py` **truncates a long path from the
left** and prints `mple/ArcheiaPictureTutorial/ultimate_rt_eb.dll` for a file
whose path begins `Sample/`; the defect is in the display and not in the
census, and it is the first appearance. *Predicted: 0.92*

**C11** `content` `inherited` — `verres.py dump` reports **6 version resources
over 9 PE**, the editor and the runtime **agree at 1.1.2.1** where the previous
object's disagreed by one in the third field, **`Degica` appears in exactly two
`FileDescription` fields** reading *Ultimate DLL (RM2k3 custom version for
Degica)* and *Ultimate Runtime DLL (…)*, `LegalCopyright` is **empty** on every
Kadokawa binary, and `UNLHA32.DLL` reports **1.47.1.7-VC**, `(C)Micco
1995-2000` and an **empty** `CompanyName`. *Predicted: 0.93*

**C12** `content` `inherited` — `mzcensus.py`, **tenth appearance**, reports
**3 of 9** and the six it misses total **2,425,856 bytes**; its `e_cblp` section
reports **0 of 3 agree** and names `byte2=0x50 ('P')`. *Predicted: 0.92*

**C13** `content` `inherited` — `sift.py --group buildpath --show` reports
**17 drive-letter hits in 3 files**, of which **15 are in `rpg2003.exe`** and
resolve to **ten distinct paths**, **eight of them Delphi `.pas` source units**
under `D:\ha\02rpg2000\2003\`, one of them **`RPG2003.hlp`**, and the two
outside `rpg2003.exe` are an NSIS `C:\Program` default and
**`C:\TMP\UNLHA32.LOG`**. *Predicted: 0.92*

**C14** `content` `inherited` — `sift.py --group personal --show` reports
**3 e-mail shapes in 1 blob over 737 blobs and 33,578,445 bytes**, all three in
`UNLHA32.TXT`, **two distinct addresses of which one appears twice**, 0 of every
other shape, with the positive control firing and the negative control quiet;
and `utf16sift.py` reports **0** hits that only a sixteen-bit pass finds.
*Predicted: 0.94*

**C15** `content` `inherited` — `protscan.py`, **seventeenth appearance**,
searches **9 files of 737 and 7,893,678 bytes of 33,578,445**, reports **0 hits**
on eleven pre-2010 optical markers, and its positive control fires on **9**.
*Predicted: 0.94*

**C16** `content` `inherited` — `mtimes.py --waves` reports **exactly one wave**,
**2026-09-09 12:18:11 .. 2026-09-09 12:18:20**, **737 files, 33,578,445 bytes,
100.00 %** — nine seconds — and not one file in the tree carries a date from
before the copy. *Predicted: 0.95*

**C17** `content` `inherited` — `crossall.py _work/sha1-all.txt --collection ..
--skip pc-rpgmaker2003-doc` reports **my distinct sha1 731** and **CROSSINGS 368
of 731**, over **104 repositories, 461 list files and 155,888 hash tokens**, with
**all 368 against `pc-rpgmaker2000-doc` and none against any other repository**;
and the collection's two directory counts, re-derived with `ls`, are **134**
`*-doc` and **65** `pc-*-doc`, both including this one. *Predicted: 0.93*

**C18** `content` `inherited` — the 368 crossings break down by extension as
**`.wav` 211 files / 9,661,794 bytes, `.mid` 92 / 1,431,351, `.png` 63 /
1,287,752, `.exe` 1 / 47,790 and `.url` 1 / 52**, the five counts sum to **368**
and the five byte totals to **12,428,739**; the 211 are **all** of the previous
object's WAV and the 92 are **all** of its MIDI, while the 63 are **63 of its
162 PNG**. *Predicted: 0.90*

**C19** `content` `inherited` — of the 368 crossings, **277 carry the same base
name in both objects and 91 do not**, and the 91 divide into **fifty** that
insert a space before a trailing number, **three** that gain an `SE` prefix, and
**thirty-eight** that are a different English translation of identical bytes;
**50 + 3 + 38 = 91**, checked by command and not by eye. *Predicted: 0.88*

**C20** `content` `inherited` — the seventeen MIDI whose internal Shift-JIS
sequence name carries a leading `J` are **exactly** the seventeen whose 2003
file name carries a leading `J` — `JFanfare 1..6`, `JEnd of Battle 1..4`, `JInn
1..2`, `JJoke 1..2`, `JItem`, `JMystery`, `JDoubt` — **seventeen of seventeen,
with no file gaining a `J` it did not already have inside**, and the duration
split that `pc-rpgmaker2000-doc/docs/06` derived is **re-derived here from these
141 files** rather than quoted. *Predicted: 0.87*

**C21** `content` `inherited` — `sigcount.py --hex 4d5a5000` reports **4 of 737
files beginning with the signature and 5 occurrences in 4 files**, and
`peembed.py setup.exe.dat` reports a highest raw end of **630,784** against a
file length of **630,784** at residue **0**, an inner MZ parsing as PE at offset
**483,728** inside the outer `.rsrc`, reaching **142,848**, at resource entry
**`RCDATA/GAMEDELETE/9`** declaring **142,848**, residue **0** — against the
previous object's **76,800** at language id **0**. *Predicted: 0.91*

**C22** `content` `inherited` — `itsf.py` closes on `rpg2003.chm` **nine times
at residue 0** with the numbers **96 + 24 = 120**, **120 + 16,468 = 16,588**,
**6,268,124** declared against 6,268,124 on disk, **84 + 4 × 4,096 = 16,468**,
**16,588 + 6,562 + 6,244,974 = 6,268,124**, **40 + 264 × 8 = 2,152** and
**8,623,119** stated three ways; the chunk tags are `PMGL PMGL PMGL PMGI`, the
listing has **530 entries and 3 index entries with 0 refusals**, and `internals`
gives **HHA Version 4.74.8702**, title **RPG Maker 2003**, compiled name
**rpg2003_en** and three clocks on **2017-09-16** agreeing within eighteen
seconds, with the header-`u32` pairing landing **7.551 ms** from the `/#SYSTEM`
FILETIME. *Predicted: 0.92*

**C23** `content` `inherited` — `lcf.py walk` opens **both** databases
unchanged: `rpg_rt.ldb.dat` at **388,574** and `Sample\…\RPG_RT.ldb` at
**374,229**, each with header name **`LcfDataBase`**, **22 top-level chunks**,
tags **11..32 strictly ascending**, **residue 0**, shapes **`{'LIST': 15,
'RECORD': 3, 'SCALAR': 4}`** and **zero chunks where both readings close** —
against the previous object's sixteen chunks and one ambiguity that had to be
settled by an invariant. *Predicted: 0.92*

**C24** `content` `inherited` — `pngcensus.py` reports **355 of 355 parsed, 0
refused, 355 of 355 closing at residue 0, 1,848 chunks walked and 1,848 of 1,848
CRC-32 verifying**, every file at depth 8, colour type 3 and non-interlaced,
**231 distinct palettes** and **349 distinct IDAT streams over 355**, and
**fourteen chunk types of which `tIME` occurs once and `tpNg` occurs once**;
`tpNg` is in no PNG specification and its CRC verifies. *Predicted: 0.93*

**C25** `content` `inherited` — `smfcensus.py` reports **141 of 141 parsed and
closing at residue 0, 1,963 tracks, 797,748 events and 10,435.682 s**, with meta
counts **name 1,317, copyright 83, marker 58, text 3**; of the 83 copyrights
**62** read `(C)2000 by ASCII Corp./Y.Kitagami` and **21** carry a Shift-JIS line
naming **Daisuke Shiiba**, **62 + 21 = 83**; and the 58 markers appear in **five
distinct spellings** of one concept. *Predicted: 0.90*

**C26** `content` `inherited` — `wavcheck.py` reports **216 of 216 parsed with
the container closing on the file 216 of 216**, **157 × 16-bit and 59 × 8-bit,
all mono at 22,050 Hz**, a total of **263.486349206 s**, and three chunk orders
— `fmt+data` **178**, `fmt+fact+data` **36**, `fmt+cue+LIST+data` **2** — the
last two being `RTP\Sound\Rain1.wav` and `Rain2.wav`, byte-identical to the
previous object's. *Predicted: 0.91*

**C27** `content` `inherited` — `rtpjoin.py` reports **299 of 299 resource
references in the root database resolving to a file that exists**, residue
**0**, **18 stems appearing in more than one subdirectory** and **18 of 299
joined references ambiguous** — against the previous object's 208 of 208 and 45
of 208. *Predicted: 0.90*

**C28** `content` `inherited` — `toolscan.py` reports **528 Python files and 0
files with a forbidden control byte** with all three positive controls firing,
`ls -1 tools/*.py | wc -l` agrees at **528**, and a file-by-file sha1 comparison
against `../pc-rpgmaker2000-doc/tools/` reports **528 common, 0 only mine, 0
only theirs and 0 differing** before this session writes anything. *Predicted:
0.90*

**C29** `content` `inherited` — `namecensus.py` crashes with a
`ZeroDivisionError`, **twenty-first appearance**, and `dircensus.py` prints a
complete formatted table over **`Director containers found : 0`** and exits
**0**, **twenty-second appearance**. *Predicted: 0.95*

**C30** `content` `inherited` — `2k3_install.vdf` is **1,545 bytes** against the
previous object's 753, writes
`HKEY_CURRENT_USER\Software\KADOKAWA\rpg2003` with `ApplicationPath` and
`RuntimePackagePath`, registers **`.r3project`** to `RPG2003.Project` with a
`DefaultIcon` and a `shell\open\command` **while the object ships a
`.r3proj`**, carries the same DEP shim in both hives against the same
`BaseFlushAppcompatCache.exe`, and ends in a **`kvsignatures` block of 256
hexadecimal digits**. *Predicted: 0.91*

**C31** `content` `inherited` — the calibration series re-derived by summing
gives **34 terms, −18.7200, mean −0.5506, 22 negative, 11 positive, 1 zero, last
ten −38.3300 at −3.8330 and a tail run of 3 consecutive negatives**, and the
last term **−1.79** ranks **seventh of thirty-four** by absolute value; all eight
figures the brief states about the series are checked one by one and **none is
wrong**. *Predicted: 0.94*

---

### Open — method

**C32** `method` `open` — every tool this session writes carries a `selftest`
mode with a stated number of checks, **every selftest is run at least once with
`PYTHONIOENCODING` unset**, every tool that prints recovered text sets its own
output encoding rather than relying on the console, and **the name of every new
tool is checked against `tools/` before it is written**. *Predicted: 0.90*

**C33** `method` `open` — every figure in every chapter carries the command that
remakes it, `docs/02` carries a command on **every** row, every chapter opens
with `*Measure: …*`, and **every percentage names its denominator on the same
line** — of which there are **eight** in this object and the eighth is that 368
of the 731 hashes are already published elsewhere. *Predicted: 0.90*

**C34** `method` `open` — no absolute path of this machine appears in any `.md`
or in any tool default, **including inside any captured traceback or tool output
committed under `notes/`**, and the check is a command with a positive control
that fires. *Predicted: 0.90*

**C35** `method` `open` — the repository goes online on branch **`master`** under
`vs-sr-dev` after `git ls-files | grep -Eiv "^(README|docs/|notes/|tools/|\.gitignore)"`
is verified empty with a positive control that fires, with a description under
350 characters **verified by reading it back from the remote** and topics set;
`rpgmaker2003-steam\`, `_pre\`, `_work\` and `prompt.txt` are not committed; and
`pc-gamelist-doc` is modified and pushed on **`main`** with `rowlen.py` run.
*Predicted: 0.90*

**C36** `method` `open` — this repository is **under twenty documents**, and no
chapter exists in it whose subject is "the same as the previous object": every
chapter carries a measurement made on **this** object, and where a comparison
with `pc-rpgmaker2000-doc` appears, the command is re-run here rather than the
number subtracted. *Predicted: 0.85*

---

### Open — content

**C37** `content` `open` `constructs` — **the four LCF map files are opened.**
`lcf.py walk` closes at residue **0** on all four unchanged; a new reader reports
each `.lmu`'s **width and height** as named integer fields; the three maps'
dimensions are given as three specific pairs; and **at least one map's chipset
or resource reference is joined against a file the Sample actually ships**,
resolving to an existing path. *Predicted: 0.45*

**C38** `content` `open` `lands` — `RPG_RT.lmt`'s first length-prefixed string is
**`Picture Tutorial`**, 16 characters, agreeing byte for byte with the
`GameTitle` in `Sample\…\RPG_RT.ini`; and the tree structure names **exactly
three** map entries besides the root, matching the three `.lmu` files on disk by
number. *Predicted: 0.62*

**C39** `content` `open` `constructs` — **the two databases are diffed**, and of
the **22** top-level chunks a specific number are byte-identical and the rest
differ; the diff is reported chunk by chunk with both byte lengths; and **at
least one record that a human being edited is named** — by chunk tag, index and
field, with the value in the root database and the value in the Sample's beside
it. *Predicted: 0.50*

**C40** `content` `open` `constructs` — the **six LCF chunk tags 27..32** that
the previous object's database did not have are present in **both** databases
here, and this repository says what at least **two** of them hold, with the
evidence being a shape the reader recovers rather than a name assumed from
EasyRPG. *Predicted: 0.62*

**C41** `content` `open` `constructs` — **the `eb` question is settled from the
bytes.** Either `ultimate_eb.dll` or `ultimate_rt_eb.dll` carries a string, a
resource field or an import/export name containing **`Enterbrain`**, named with
its file offset; **or** it does not, in which case the negative is reported as a
measurement — the byte count searched, the encodings searched, and the statement
that two letters in a file name remain undemonstrated. *Predicted: 0.35*

**C42** `content` `open` `lands` — the **one** `tIME` chunk among 1,848 is
located by command, its file is named, and it decodes to a specific UTC
timestamp; and the **one** `tEXt` chunk is named beside it. *Predicted: 0.70*

**C43** `content` `open` `constructs` — **`tpNg` is decoded.** The single
occurrence is located by file and byte offset, its declared length is given, its
CRC-32 is re-verified independently of `pngcensus.py`, its payload is dumped and
read, and this repository states **what wrote it** — with the evidence being
something in the payload or in the surrounding chunk order and not a guess.
*Predicted: 0.40*

**C44** `content` `open` `constructs` — the **363** hashes that do **not** cross
are broken down by extension, the rows sum to **363** and to a byte total that
plus **12,428,739** equals the distinct-hash byte total of the object, and the
chapter about the product uses **that** denominator rather than the tree
wherever the claim is about what is new in the 2003. *Predicted: 0.78*

**C45** `content` `open` `constructs` — **the 13-versus-16 September question is
decided**, and the decision rests on a **third** witness in the bytes named here
— not on the `.url` file name and not on the `/#SYSTEM` clock alone — with the
byte-identity of `RPG Maker 2003.url` to `pc-rpgmaker2000-doc`'s shortcut
re-derived by sha1 on both trees rather than quoted. *Predicted: 0.55*

**C46** `content` `open` `lands` — `coverage.py` learns **three** magics —
`8BPS`, `LcfMapUnit`, `LcfMapTree` — its selftest gains checks for all three,
and `tree` then reports **730 files and 26,534,548 bytes specified, 7 files and
7,043,897 decoded, 0 derived and 0 opaque**, residue **0**; the `.psd` is filed
**SPECIFIED** because Adobe published the format, and the three LCF variants
**DECODED** under the test `pc-rpgmaker2000-doc/docs/09` already defined.
*Predicted: 0.88*

**C47** `content` `open` `nonnumeric` — the repository states, as **two
different sentences and not one**, that **12,970 bytes in four files** are in a
format no vendor ever specified and that **54,653 bytes in one file** are in a
format the vendor published and this box never implemented; and it says which of
the two is a fact about the world and which is a fact about the box.
*Predicted: 0.85*

**C48** `content` `open` `lands` — the `.psd` is read past its 26-byte header:
**3 channels, 196 × 123, depth 8, colour mode 3**, and the file either closes on
its own declared section lengths at residue 0 or the reason it does not is
stated with the offset reached. *Predicted: 0.72*

**C49** `content` `open` `constructs` — a **third** `impossible mtimes` test is
written and it catches a COFF `TimeDateStamp` that is a round power of two; it
fires on `0x00200000` and `0x00010000`, the previous session's proposed
same-stamp-different-size test fires on the **four** Borland files, and the two
tests together report **5 of 9** false stamps on this object where `pecensus.py`
reports **0 of 9**; the new test's positive control fires and its negative
control is quiet on the two genuine stamps. *Predicted: 0.70*

**C50** `content` `open` `nonnumeric` — **the third-party hash list asked for in
`pc-rpgmaker2000-doc/docs/11` is written here** rather than asked for again: a
tool publishes sha1, size and version for every third-party component in this
object — `UNLHA32.DLL` and `BaseFlushAppcompatCache.exe` at minimum — in a form
`crossall.py` can read, and the repository states whether the two neighbours
have done it and, if not, says so **with the command**. *Predicted: 0.80*

**C51** `content` `open` `nonnumeric` — the personal-data rule of
`pc-rpgmaker2000-doc/docs/10` is **applied in one paragraph and not re-argued**:
all **three** occurrences are redacted, `redact.py --expect 3` fires, and Micco's
name, his copyright line, his version number and his manual's own date are
published; and the space is spent on the new fact, which is that **the same
author's manual in two versions three years apart gives two different
addresses**. *Predicted: 0.88*

**C52** `content` `open` `nonnumeric` — `pc-rpgmaker95-doc/tools/redact.py` is
checked for the leak `pc-rpgmaker2000-doc/docs/13` recorded, the result is
stated **either way with the command that establishes it**, and if the address is
still there this repository says so a second time rather than letting it become
a thing the collection has noticed twice and fixed never. *Predicted: 0.88*

**C53** `content` `open` `constructs` — `refusals.py` is re-run **unextended**
and its refusals are classified the way `pc-rpgmaker2000-doc/docs/12` classified
them — argument parsing, an OS error on the path, a format refusal, an uncaught
exception — the four counts sum to the refusal total, and the **argparse share
is compared with that session's 23 of 40** as the second population of a
repeatable measurement. *Predicted: 0.72*

**C54** `content` `open` `lands` — `jstore.py` is pointed at **both** databases
and **all four** map files, its claim is **predicted in writing before it is
run**, and it closes at residue **0** on all six with the arithmetic
`5 × lists + 16 × GUIDs + filler = file size` printed for each — the fifth
through tenth false closures of a tool whose residue cannot be anything but
zero. *Predicted: 0.80*

**C55** `content` `open` `lands` — `kfaccount.py`, **fifth appearance**, exits
**0** having printed its usage, and the **reason** is named — which subcommand it
wants and what the harness hands it instead — rather than the occurrence being
recorded again. *Predicted: 0.82*

**C56** `content` `open` `constructs` — the shop's **22,100,528** declared
`BytesToDownload` is checked against a per-file compression total computed here,
the ratio **1.5194** is re-derived, and the residue between the two is given as
a byte count **and** as a share of 22,100,528 — against the previous object's
0.16 % on the same arithmetic. *Predicted: 0.65*

**C57** `content` `open` `constructs` — `rtpjoin.py` is pointed at the
**Sample's own** database and at the three `.lmu`, and this repository reports
how many of that project's resource references resolve to a file the project
ships, how many resolve into `RTP\` instead, and how many resolve to nothing —
the three counts summing to the total. *Predicted: 0.60*

**C58** `content` `open` `nonnumeric` — the leftovers chapter carries the
expansions — `LMU`, `LMT`, `LDB`, `PSD`, `EB`, `SE`, `J`, `RTP`, `VDF`, `ACF`,
`NSIS`, `DEP`, `NX`, `HHA`, `RSA`, `r3proj`, `2k3` and any other initialism the
session turns up — each labelled **demonstrated from the object**, **derived**,
**attributed to a public source** or **not demonstrated**, with the four counts
summing to the total. *Predicted: 0.80*

**C59** `content` `open` `nonnumeric` — the corrections chapter finds **at least
six** errors, of which **at least one is an arithmetic error in this
pre-briefing** and at least one is this session's own; the pre-briefing reports
none of its own, which is the first time in nine objects, and this repository
does not accept that at face value. *Predicted: 0.65*

**C60** `content` `open` `nonnumeric` — the `pc-gamelist-doc` row is added on
branch `main` with the `Saga` cell reading **`RPG Maker`** like the two rows
already there, the `Year` cell **argued from the four candidate witnesses and
named**, and the "What it is" cell saying it is a **tool** — and that it ships a
playable game; `rowlen.py` reads **77** rows with **0** over budget.
*Predicted: 0.82*

**C61** `content` `open` `constructs` — the **nineteen** empty directories are
named individually, **four** of them under `RTP\` and **fifteen** under
`Sample\`, the two counts summing to 19; and the chapter says what an empty
directory means in each of the two cases, which is not the same thing.
*Predicted: 0.72*

**C62** `content` `open` `lands` — the `.r3proj`/`.r3project` mismatch is stated
with both byte offsets: the extension the install script registers is located
inside `2k3_install.vdf` at a named offset, the extension on disk is the sixteen
bytes of `Picture_Tutorial.r3proj`, and the repository says what it can and
cannot establish about whether the editor accepts both. *Predicted: 0.75*

**C63** `content` `open` `nonnumeric` — where a comparison with
`pc-rpgmaker2000-doc` yields **zero difference** — the audio library
byte-identical, the `.chm` opening the same way, the install script performing
the same three registry actions — this repository writes it **as a measurement
with its command**, and not as an absence of material; and every figure quoted
from that repository is taken from its `docs/` rather than from memory, with a
check for whether its own corrections chapter already amended it. *Predicted:
0.85*
