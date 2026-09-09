# 07 — what does not cross: 363 hashes, and every one of the 54 new pieces of audio is stamped with the year

*Measure: `python tools/crossnames.py notes/sha1-all.txt
../pc-rpgmaker2000-doc/notes/sha1-all.txt`, in `notes/crossnames.txt`; the
by-directory split in `notes/notcrossing.txt`; `python tools/smfcensus.py
rpgmaker2003-steam --tsv notes/smfcensus.tsv`, in `notes/smfcensus.txt`; `python
tools/pngcensus.py rpgmaker2003-steam --by-dir`, in `notes/pngcensus.txt`;
`python tools/itsf.py list rpgmaker2003-steam/rpg2003.chm`, in
`notes/itsf-list.txt`. **The denominator in this chapter is 363 distinct hashes
and 19,984,119 bytes, not 737 files and not 33,578,445 bytes**, and it says so
on every line where it matters.*

---

## The denominator

[06](06-the-crossings.md) is about the collection. This chapter is about the
product, and the product is what is left when the shared library is taken out.

```
crossing     : 368 of 731    12,428,739 bytes
NOT crossing : 363 of 731    19,984,119 bytes
the two sum to my distinct hashes : True
```

The two byte totals sum to 32,412,858 and the object is 33,578,445. **The
1,165,587-byte difference is the six files shipped twice** ([01](01-the-object.md)),
counted once here because this is a comparison of hashes.

| ext | files | bytes | share of 19,984,119 |
|---|---:|---:|---:|
| `.png` | 289 | 3,878,798 | 19.4094 % |
| `.mid` | 49 | 1,514,398 | 7.5780 % |
| `.wav` | 5 | 765,030 | 3.8282 % |
| `.dat` | 4 | 2,176,990 | 10.8936 % |
| `.chm` | 1 | 6,268,124 | 31.3655 % |
| `.exe` | 1 | 4,387,328 | 21.9541 % |
| `.dll` | 2 | 512,512 | 2.5646 % |
| `.ldb` | 1 | 374,229 | 1.8726 % |
| `.psd` | 1 | 54,653 | 0.2735 % |
| `.ico` | 1 | 23,558 | 0.1179 % |
| `.txt` | 2 | 13,870 | 0.0694 % |
| `.lmu` | 3 | 12,635 | 0.0632 % |
| `.vdf`, `.lmt`, `.ini`, `.r3proj` | 4 | 1,994 | 0.0100 % |
| | **363** | **19,984,119** | 100 % |

---

## By directory, and two rows are the whole story

| directory | not crossing | bytes | crossing |
|---|---:|---:|---:|
| `.` | 11 | 13,360,369 | 2 |
| `RTP\Music` | **54** | 2,279,428 | **97** |
| `RTP\Backdrop` | **34** | 1,687,238 | **0** |
| `RTP\Monster` | **115** | 549,449 | **0** |
| `RTP\BattleCharSet` | **64** | 465,830 | **0** |
| `Sample\…` (all) | 37 | 808,006 | 5 |
| `RTP\Title` | 4 | 269,386 | 0 |
| `RTP\Battle` | 26 | 211,432 | **28** |
| `RTP\ChipSet` | 5 | 170,322 | 0 |
| `RTP\FaceSet` | 5 | 140,023 | 0 |
| `RTP` (the icon) | 1 | 23,558 | 0 |
| `RTP\System` | 3 | 8,846 | 1 |
| `RTP\BattleWeapon` | 1 | 5,665 | 0 |
| `RTP\System2` | 3 | 4,567 | 0 |
| `RTP\Sound` | **0** | 0 | **206** |
| `RTP\Panorama` | 0 | 0 | 13 |
| `RTP\CharSet` | 0 | 0 | 15 |
| `RTP\GameOver` | 0 | 0 | 1 |
| | **363** | **19,984,119** | **368** |

**`RTP\Sound` is 206 files and every one of them is inherited.** Not one sound
effect in RPG Maker 2003 is new. `RTP\Panorama`, `RTP\CharSet` and
`RTP\GameOver` are the same: 29 more files, all of them the 2000's.

**`RTP\Backdrop`, `RTP\Monster`, `RTP\ChipSet`, `RTP\FaceSet` and `RTP\Title`
are the reverse: 163 files, not one of them inherited**, on directories the 2000
also had. Those five categories were re-authored from nothing while the sound
effects were not touched at all.

---

## Seven new resource kinds, four of which ship nothing

```
ls -d rpgmaker2003-steam/RTP/*/  | wc -l              19
ls -d ../pc-rpgmaker2000-doc/rpgmaker2000-steam/RTP/*/ | wc -l   12
```

**Nineteen against twelve, so seven are new**, and they are `Battle2`,
`BattleCharSet`, `BattleWeapon`, `Frame`, `Movie`, `Picture` and `System2`.
(The pre-briefing said twenty and eight while listing seven —
[14](14-corrections.md).)

**Three of the seven carry files** — `BattleCharSet` 64, `System2` 3,
`BattleWeapon` 1 — **and four are empty**: `Battle2`, `Frame`, `Movie`,
`Picture`. The product declares a directory for a resource kind and ships none
of it.

`Movie` is not an idle declaration. The runtime DLL exports a function for it:

```
python tools/peimpexp.py rpgmaker2003-steam/ultimate_rt_eb.dll.dat --exports
   SetMoviePosition          @9
```

**The code can play a movie and the library has none to play**, which is a
better account of an empty directory than "somebody forgot".

---

## The music is two people's and it says so

```
python tools/jingles.py rpgmaker2003-steam --tsv notes/smfcensus.tsv

-- the composers, counted
     62  (C)2000 by ASCII Corp./Y.Kitagami
     58  (no copyright event)
     21  作曲：椎葉 大翼 【Daisuke Shiiba】
```

62 + 21 = 83, which is the copyright-event count `smfcensus.py` reports.
**Sixty-two are the previous object's line on the previous object's bytes**, and
they cross. Twenty-one carry a Shift-JIS line reading *composition: Shiiba
Daisuke*, romanised in the same string, and **not one of them carries a year**.

The kanji are read from the bytes and not from a transcription:

```
8d ec  8b c8  81 46  92 c5  97 74  20  91 e5  97 83  20  81 79 ...
作     曲     ：     椎     葉         大     翼         【Daisuke Shiiba】
```

**`97 83` is `翼` (U+7FFC). `輔`, which the pre-briefing printed, is `95 e3` and
is not in the file** ([14](14-corrections.md)). The object gives both the kanji
and the romanisation in one string, so nothing here has to be guessed.

### And every new piece is stamped

```
new files in RTP/Music                     : 54
beginning 2003, SE2003 or J2003            : 54
the others                                 : []
```

**All fifty-four.** `2003Adventurers.mid`, `2003Casino Indulgence.mid`,
`2003Ice Labyrinth.mid`, `SE2003Wind.wav`, `J2003Horn.mid`. The publisher put
the product year on the front of everything it added, in a directory where the
inherited files carry no prefix at all — which is the same instinct that renamed
`Sea.wav` to `SESea.wav` ([06](06-the-crossings.md)), and it means the two
libraries can be told apart by name as well as by hash.

**Fifty-eight MIDI carry no copyright event.** That is not 141 − 83 by
accident: 141 − 62 − 21 = 58, and `jingles.py` counts them directly.

### Marker events, which the 2000's ninety-two had none of

```
python tools/smfcensus.py rpgmaker2003-steam --text
by meta type : {'name': 1317, 'copyright': 83, 'marker': 58, 'text': 3}
```

Fifty-eight markers in **five spellings of one concept** — `Loopstart`,
`LoopStart`, `Loop-Start`, `loopend`, `Marker-1`. A loop point is a thing a
sequencer writes and a runtime reads; five spellings in one publisher's library
is what happens when several people write the files and nothing checks them.

---

## The graphics: 289 new PNG of 352 distinct

```
python tools/pngcensus.py rpgmaker2003-steam --by-dir
parsed as PNG 355 of 355   refused 0
files closing at residue 0 : 355 of 355
chunks walked 1848   CRC-32 verifies : 1848 of 1848
every file : depth 8, colour type 3, non-interlaced
DISTINCT palettes by sha1 : 231 over 355
distinct (width, height)  : 127
distinct IDAT streams     : 349 over 355
```

355 files, 352 distinct hashes, **289 of which are not in the 2000**. Every one
of the 355 is depth 8, colour type 3, non-interlaced — the same discipline the
2000's 162 kept — and the closure and CRC totals are a confirmation and not a
finding.

**Six files share a compressed pixel stream where the 2000 had 162 of 162
distinct**, and all six are the `RTP\`-to-`Sample\` duplicates of
[01](01-the-object.md). The one `tIME`, the one `tEXt` and the one `tpNg` are
all in one file and that file is somebody's ([09](09-the-sample-project.md)).

---

## The help file is entirely new, and it is a third of what does not cross

`rpg2003.chm`, **6,268,124 bytes — 31.3655 % of the 19,984,119 that do not
cross**, and the single largest thing Kadokawa authored for this release.

```
python tools/itsf.py list rpgmaker2003-steam/rpg2003.chm

chunk tags in order      : PMGL PMGL PMGL PMGI
listing entries          : 530     index entries : 3     refusals : 0
   names beginning '::'  : 7        the container's own machinery
   names beginning '/'   : 523      the help project's own files
   section 0      12 entries    6,251,536 declared bytes
   section 1     518 entries    8,564,596 declared bytes
```

Against the previous object's 5 chunks, 252 reset blocks and 475 entries. **The
reader opens it with no change and closes on nine quantities**, which is the
fourth specimen of that and is worth this sentence and no chapter.

**Neither object publishes the hashes of the 523 files inside**, so whether the
2003's help text is a rewrite or an edit of the 2000's is not answerable from
what the collection has published — the same shape of blindness that
[06](06-the-crossings.md) describes about the 95, one level further in.

---

## The programs are all new, and the feature they add is in an export table

Nine binaries, 7,893,678 bytes, and only `BaseFlushAppcompatCache.exe` crosses.
The details are [08](08-the-programs.md); the one that belongs here is what
distinguishes the product:

```
python tools/peimpexp.py rpgmaker2003-steam/ultimate_rt_eb.dll.dat --exports
EXPORTS : 10 functions, 10 by name
   ATBHandlerMain            @1
   CherryInitialize          @2
   CustomGameWndProc         @3
   CustomStretchBlt          @4
   DataInitialized           @5
   F5Handler                 @6
   GetFullscreenRect         @7
   HandleNameRepl            @8
   SetMoviePosition          @9
   StartupFullscreenDecision @10
```

**`ATBHandlerMain`** — the active-time battle system is the headline difference
between RPG Maker 2000 and 2003, and it is named in an export table in this
object, in a third party's DLL, alongside a fullscreen decision and a movie
position.

---

## What is new and is not measured here

* whether the 523 files inside the `.chm` overlap the 2000's 475;
* whether the 289 new PNG are redrawn or resized versions of the 2000's — the
  palettes differ, the dimensions differ, and `crossall.py` compares sha1 and
  nothing else;
* what the six new database chunks 27..32 hold, beyond three of them being
  declared with a size of zero ([05](05-the-two-databases.md));
* what `Battle2`, `Frame` and `Picture` would have contained.
