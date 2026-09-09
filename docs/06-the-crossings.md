# 06 — the crossings: 368 of 731, which is a measurement of a publishing decision and not of RPG Maker

*Measure: `python tools/crossall.py notes/sha1-all.txt --collection .. --skip
pc-rpgmaker2003-doc`, in `notes/crossall.txt`; `python tools/crossnames.py
notes/sha1-all.txt ../pc-rpgmaker2000-doc/notes/sha1-all.txt
--expect-crossing 368`, in `notes/crossnames.txt`; `python tools/jingles.py
rpgmaker2003-steam --tsv notes/smfcensus.tsv --crossing
../pc-rpgmaker2000-doc/notes/sha1-all.txt`, in `notes/jingles.txt`. The two
selftests are 14 and 10 checks, 0 failures.*

---

## The denominators, published before the result

```
ls -1d ../*-doc/    | wc -l     134      including this one
ls -1d ../pc-*-doc/ | wc -l      65      including this one
```

The sweep's own three figures, from its own report: **104 repositories, 461 list
files, 155,888 hash tokens.** All three moved against the previous run — 103,
457, 155,245 — because `pc-rpgmaker2000-doc` was published between them and
publishes four files under `notes\` ending `.txt` or `.tsv`.

**134 does not move after this session.**

---

## The result

```
python tools/crossall.py notes/sha1-all.txt --collection .. \
    --skip pc-rpgmaker2003-doc

my distinct sha1 : 731
CROSSINGS        : 368 of 731 = 50.3420 %

   min bytes    my hashes    crossings         rate
           0          731          368     50.3420 %
        1024          709          361     50.9168 %
        4096          591          328     55.4992 %
       65536           72           46     63.8889 %
```

**All 368 are with `pc-rpgmaker2000-doc` and none is with anything else**, over
103 other repositories. 12,428,739 bytes of distinct crossing content.

The collection's previous rates were **1 of 12 = 8.3333 %**, **10 of 962 =
1.0395 %**, and — on the object immediately before this one — **0 of 477**.

| ext | files | bytes | what it is |
|---|---:|---:|---|
| `.wav` | 211 | 9,661,794 | **all 211 of the previous object's** |
| `.mid` | 92 | 1,431,351 | **all 92** |
| `.png` | 63 | 1,287,752 | 63 of its 162 |
| `.exe` | 1 | 47,790 | `BaseFlushAppcompatCache.exe` |
| `.url` | 1 | 52 | the shortcut |
| | **368** | **12,428,739** | |

**Every sound effect and every piece of music in RPG Maker 2000 is inside RPG
Maker 2003, byte for byte. The graphics were half redone and the audio was not
touched at all.**

---

## And the sentence that matters is about us

Fifty per cent is six times the collection's previous record and it would be
easy to write as a fact about RPG Maker. It is not one.

`pc-rpgmaker95-doc` published **twelve** hashes — of ZIP members — and
deliberately withheld the 256 files it recovered from inside the archive.
`pc-rpgmaker2000-doc` published **477** hashes of a live tree.

**The first decision made a crossing impossible and the second made 368 of them
inevitable.** The two products' relationship did not change between those two
sessions; what changed is what one of them wrote down. A crossing rate is a
measurement of a publishing decision, and this is the first object in this
collection on which that is visible, because it is the first one whose
predecessor published a tree.

The corollary is a cost, and it is paid in this object too:
`pc-rpgmaker95-doc`'s 256 withheld files include a 1999 build of the same audio
library. **Whether the 2000's WAV cross backwards into the 95 is unknowable from
what the collection has published**, and no session can fix it by measuring
harder.

---

## Two names over one set of bytes, 91 times

Of the 368, **277 carry the same base name in both objects and 91 do not.**
The 91 are a policy, and `crossnames.py` sorts them by a stated rule rather than
by eye:

```
same          the two base names are equal
spaced        one space before a trailing run of digits    Boss1  -> Boss 1
prefixed      an SE prefix, after the spacing rule         Sea    -> SESea
retranslated  everything else
```

```
same base name in both objects : 277
renamed                        : 91
   spaced           47
   prefixed          3
   retranslated     41
the three classes sum to the renamed total : True  (47 + 3 + 41 = 91)
same + renamed = crossing : True
```

**The pre-briefing gave this split as 50 + 3 + 38 and it is 47 + 3 + 41**
([14](14-corrections.md)). The total is right; the boundary is not, and it moves
because three of the renames both insert a space *and* change a word —
`Gameover1` → `Game Over 1`, `GhostTown1` → `Ghost Town 1`,
`BlackMarket` → `Black Market` — which a rule about trailing digits does not
catch and an eye does.

**The three `SE` renames are also not the three the pre-briefing named.**

```
Clock       -> SEClock
Earthquake  -> SEEarthquake
Sea         -> SESea
```

`Rain1` → `SERain` and `Rain2` → `SEDownpour` gained the prefix *and* a new word,
so they are retranslations. `pc-rpgmaker2000-doc/docs/06` observed that five WAV
sit in `RTP\Music` and called them "the ambiences … filed with the music because
they play like music". **The 2003 kept them there and labelled them `SE`.**

### Thirty-eight of the forty-one are one Japanese word translated twice

The bytes are identical, so the internal Shift-JIS sequence names are identical.
The English file names are not.

| the 2000 | the 2003 | | the 2000 | the 2003 |
|---|---|---|---|---|
| `Devil` | `Demon Lord` | | `Anger` | `Wrath` |
| `Crisis` | `In a Pinch` | | `Marketplace` | `Lively Market` |
| `Energy` | `Liveliness` | | `Search` | `Exploration` |
| `Peace1..3` | `Repose 1..3` | | `Store1..3` | `Shop 1..3` |
| `Farewell1..2` | `Parting 1..2` | | `Treasure` | `Secret Treasure` |
| `Gameover1..3` | `Game Over 1..3` | | `Items` | `JItem` |

`pc-rpgmaker2000-doc/docs/06` showed that the 2000's English file names are
translations of the internal Japanese names. **This object shows the translation
was done a second time, by somebody who did not have the first one in front of
them, over the same bytes.** Two English readings of one Japanese word, shipped
by one publisher three days apart.

The forty-first is not a translation at all:

```
RM2000 EN PRELIMINARY 13.09.2017.url  ->  RM2003 EN PRELIMINARY 13.09.2017.url
```

**Byte-identical, sha1 `e1f501ef97c6b9e5f34ce78b814733c4468b75df`, 52 bytes,
verified on both trees** — the same `[InternetShortcut]` pointing at
`http://www.rpgmakerweb.com`, with a different product number and the same date
in its name. That date is the subject of [11](11-the-clocks.md).

---

## The `J`, re-derived here rather than cited

`pc-rpgmaker2000-doc/docs/06` established, **from durations alone**, that a `J`
in a MIDI file's internal Shift-JIS sequence name marks a jingle: seventeen
files with it, seventy-five without, two disjoint duration ranges over a
one-character field. **The `J` was in no file name there.**

Here it is in the file names. Re-derived on this object's 141 files, on both
axes, over three populations:

```
python tools/jingles.py rpgmaker2003-steam --tsv notes/smfcensus.tsv \
    --crossing ../pc-rpgmaker2000-doc/notes/sha1-all.txt

the two axes agree on 140 of 141 files

-- INHERITED (its sha1 is in the other object) : 92 files
   a leading J in the FILE NAME       with 17 (4.245..15.634)  without 75 (29.565..174.993)  -> DISJOINT
   a J in the SEQUENCE NAME           with 17 (4.245..15.634)  without 75 (29.565..174.993)  -> DISJOINT

-- ALL : 141 files
   a leading J in the FILE NAME       with 18 (3.750..15.634)  without 123 (12.625..174.993) -> OVERLAPPING
         on the wrong side : 2003Panic.mid   12.625 s

-- NEW (its sha1 is not) : 49 files
   a leading J in the FILE NAME       with  1 (3.750..3.750)   without 48 (12.625..171.855)  -> DISJOINT
```

**On the ninety-two inherited files the derivation reproduces exactly**, on an
axis the previous session did not have, from a different starting point:
seventeen files, a maximum of 15.634 s, and a minimum of 29.565 s for the other
seventy-five. **Seventeen of seventeen, and the two axes agree on every one of
them.**

**And the pre-briefing's claim that nothing else took the `J` is wrong.** There
are **eighteen** files with a leading `J`, and the eighteenth is
`J2003Horn.mid`, one of the 2003's own new pieces:

```
J2003Horn.mid   3.750 s   sequence name 'Seq-1'
```

It is the one file of 141 where the two axes disagree. **The publisher promoted
the convention into the file name; the composer of the new music did not carry
it into the internal name**, and `2003Panic.mid` at 12.625 s is a new piece,
shorter than the longest inherited jingle, carrying no `J` at all.

So the rule holds where it was derived and breaks where it was extended, and
that is a fact about two music libraries by two people ([07](07-what-does-not-cross.md)):

```
-- the J files, by composer
     15  (C)2000 by ASCII Corp./Y.Kitagami
      3  (no copyright event)
      0  作曲：椎葉 大翼 【Daisuke Shiiba】
```

---

## Who made the measurement

The question this object poses is whether the session that *derived* the `J`
from a duration statistic made the measurement, or the session that found the
list of file names confirming it.

**Neither, on its own.** The derivation was a hypothesis with one specimen and
no second axis; it could have been a coincidence over seventeen files. The file
names are a second axis and confirm it at no cost — the crossing sweep produced
them as a by-product of a hash comparison, and this chapter's re-derivation took
one command. **What made it a measurement is that two independent axes agree on
140 of 141 files and that the one disagreement is explicable.**

And the confirmation cost nothing only because somebody published 477 hashes of
a tree instead of twelve hashes of an archive. The measurement is jointly owned
and the second half of the credit belongs to a decision about publishing.

---

## What the crossings do not include

* **`UNLHA32.DLL`.** Three objects in a row ship Micco's library and the bytes
  differ every time, so it has never crossed. That is now addressed, by
  publishing the component rather than the tree ([12](12-whose-bytes.md));
* **anything inside a container.** Neither object publishes the hashes of the
  523 files inside its `.chm`;
* **near-matches of any kind.** `crossall.py` compares sha1 and nothing else,
  and the five differing `ChipSet` PNG of [09](09-the-sample-project.md) are
  invisible to it by design.
