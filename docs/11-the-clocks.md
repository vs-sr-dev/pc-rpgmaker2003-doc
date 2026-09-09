# 11 — the clocks: seven false stamps that a tool reports as none, and a September question whose answer is neither of the two dates offered

*Measure: `python tools/mtimes.py rpgmaker2003-steam --waves`, in
`notes/mtimes.txt`; `python tools/stampcheck.py rpgmaker2003-steam
--expect-false 7`, in `notes/stampcheck.txt`; `python tools/itsf.py internals
rpgmaker2003-steam/rpg2003.chm`, in `notes/itsf-internals.txt`; `python
tools/pngchunk.py rpgmaker2003-steam --type tIME --expect 1`, in
`notes/pngchunk-time.txt`; `python tools/uuidscan.py rpgmaker2003-steam
--expect 19`, in `notes/uuidscan.txt`; the XMP extraction in `notes/psd.txt`.
The three selftests are 19, 10 and 14 checks, 0 failures.*

---

## One wave, nine seconds, and it is 2026

```
python tools/mtimes.py rpgmaker2003-steam --waves
wave 1  2026-09-09 12:18:11 .. 2026-09-09 12:18:20
        737 files   33,578,445 bytes   100.00 %
```

Nine seconds for 737 files, against the previous object's fourteen for 477.
Steam wrote both trees in the same minute — the manifests' `LastUpdated` are
1788949101 and 1788949103 — and **not one original timestamp survives in either
object.**

`pc-rpgmaker2000-doc/docs/08` already said what that means: *a delivery
mechanism that verifies the bytes destroys the dates, and one that preserves the
dates cannot verify the bytes.* **The new thing is only that the same delivery
destroyed two objects' dates two seconds apart and both are now documented, so
the sentence has two witnesses.** That is the whole finding and it gets this
paragraph.

---

## Seven false stamps of nine, and the tool that reports none

```
python tools/pecensus.py rpgmaker2003-steam --by-magic
impossible mtimes : 0 of 9 datable binaries
```

**Its test is *is the file's mtime earlier than its link time***, and a 1992
stamp on a 2026 file passes comfortably. Third object running, third `0 of N`.

`pc-rpgmaker2000-doc/docs/08` proposed a second test — *do two files of
different sizes share a stamp to the second* — and noted it would not be enough.
It is not. `stampcheck.py` runs three, reports them separately, and says what
each catches:

```
python tools/stampcheck.py rpgmaker2003-steam --expect-false 7

  T1 IMPOSSIBLE (mtime precedes link time)      : 0 of 9
  T2 COLLIDING  (a stamp shared across sizes)   : 4 of 9
  T3 ROUND      (a round binary quantity)       : 3 of 9
  FALSE by at least one test                    : 7 of 9
  the same, counted by DISTINCT BINARY          : 5 of 7
```

**T3 is new and it is the one that was needed.**

```
ROUND : ultimate_eb.dll              stamp 0x00200000 = 2097152,
                                     a power of two (2^22) and before 1980
ROUND : ultimate_rt_eb.dll.dat       stamp 0x00010000 = 65536,
                                     a power of two (2^17) and before 1980
ROUND : Sample/…/ultimate_rt_eb.dll  the same bytes
```

**Exactly 2 MiB and exactly 64 KiB.** A `TimeDateStamp` holding a round binary
size is a field somebody wrote something else into. The test is deliberately
narrow — a power of two **and** before 1980 — because real timestamps are
numbers too, and both halves of the condition are printed so a reader can
disagree with either. The 1992 Borland constant, 708,992,537, is not caught by
T3 and does not need to be: T2 catches it on four files.

**And the two denominators are printed because the pre-briefing conflated
them.** Seven *files* carry a false stamp; five *distinct binaries* do, because
this object ships two of them twice. The pre-briefing wrote "five of nine" over
a table showing seven rows ([14](14-corrections.md)).

What the three tests do **not** say is in the tool's own footer and is repeated
here: a stamp that passes all three is not thereby true. They catch three ways
of being obviously false and no way of being quietly false.

---

## The help file's clock, read three ways, for the third time

```
python tools/itsf.py internals rpgmaker2003-steam/rpg2003.chm

/#SYSTEM code 10, a u32 Unix time        2017-09-16 19:54:13 UTC
/#SYSTEM code  4, a FILETIME at +20      2017-09-16 19:53:55.521294 UTC
the ITSF header's u32 at +0x10, paired   2017-09-16 19:53:55.528845 UTC
/#SYSTEM code  9, compiler               HHA Version 4.74.8702
/#SYSTEM code  3, title                  RPG Maker 2003
/#SYSTEM code  6, compiled file name     rpg2003_en
```

The pairing of the header's truncated `u32` with the high half of the `/#SYSTEM`
FILETIME — derived on the 2000 and checked on `SLPEI.chm` — lands **7.551
milliseconds** away here, against 7.6 ms on the 2000 and 187.5 ms on `SLPEI.chm`.
**Third specimen, and the tightest.**

**And the header's LCID is the same on both RPG Maker help files:**

| | ITSF header `+0x14` | ITSP `+0x30` |
|---|---|---|
| `rpg2000.chm` | 0x0C07 — German (Austria) | 0x0409 |
| `rpg2003.chm` | **0x0C07 — German (Austria)** | 0x0409 |
| `SLPEI.chm` | 0x0407 — German (Germany) | 0x0409 |

`pc-rpgmaker2000-doc/docs/11` narrowed that field to *the compiling machine's
locale*. **Two English help files for a Japanese product, compiled three days
apart, carry the same German-Austrian locale**, which narrows it once more: not
merely a compiling machine, but the same locale setting across two compiles of
one product line. The object also carries a licence for a developer whose
credits and form class names are all over the editor ([08](08-the-programs.md));
this repository notes the coincidence and does not turn it into an attribution.

---

## The September question, and the answer is neither 13 nor 16

The object ships two shortcut files, byte-identical to each other **and to the
previous object's**:

```
sha1 e1f501ef97c6b9e5f34ce78b814733c4468b75df   52 bytes

rpgmaker2003-steam/RM2003 EN PRELIMINARY 13.09.2017.url
rpgmaker2003-steam/RPG Maker 2003.url
../pc-rpgmaker2000-doc/notes/sha1-all.txt :
    RM2000 EN PRELIMINARY 13.09.2017.url
```

**A file name is not a byte the product wrote about itself**, and this one is
demonstrably inherited: the same 52 bytes, the same date in the name, a
different product number, in two objects. On the 2000 the shortcut's 13.09.2017
and the help file's 2017-09-13 agreed to the day, and that agreement was that
session's strongest clock finding. **Here the help file says 16 September and
the shortcut still says 13**, which looks like a contradiction and is instead a
shortcut that was copied and renamed.

So the shortcut is out. What is left is four independent readings, and three of
them nobody had taken.

| when (UTC) | what | where |
|---|---|---|
| 2015-08-03 02:28:57 | `xmp:CreateDate` | the `.psd`'s XMP |
| **2017-09-13 18:22:56** | a PNG `tIME` chunk | `Picture\INPUTDISPLAY.png` |
| **2017-09-13 18:35:07 … 18:41:15** | nine version-1 UUID timestamps | `Picture\RTPHERO_*.png`, the `.psd` |
| **2017-09-16 19:53:55 … 19:54:13** | three ITSF clocks | `rpg2003.chm` |
| **2017-09-28 03:26:58** | a version-1 UUID timestamp | the `.psd` |
| 2017-09-28 03:30:00 | `xmp:ModifyDate`, and an EXIF block | the `.psd` |

**The tree cannot predate 28 September 2017**, because it contains a file whose
own metadata says it was modified then — twelve days after the help file was
compiled. **Neither 13 nor 16 September is this build's date. The 13th is when
the tutorial's pictures were drawn, the 16th is when the help file was compiled,
and the tree was assembled on or after the 28th.**

### The three witnesses on 13 September, and they agree with each other

```
python tools/pngchunk.py rpgmaker2003-steam --type tIME --expect 1
file    : Sample/ArcheiaPictureTutorial/Picture/INPUTDISPLAY.png
chunk   : tIME at byte offset 33, length 7   CRC VERIFIES
decoded : 2017-09-13 18:22:56 UTC

python tools/uuidscan.py rpgmaker2003-steam --expect 19
Picture/RTPHERO_1.png  1293  2017-09-13 18:35:07.128936   M5c84
Picture/RTPHERO_2.png  1293  2017-09-13 18:36:06.621970   M5c84
Picture/RTPHERO_3.png  1293  2017-09-13 18:36:40.635060   M5c84
Picture/RTPHERO_4.png  1293  2017-09-13 18:37:18.536536   M5c84
Picture/RTPHERO_6.png  1293  2017-09-13 18:39:30.993840   M5c84
Picture/RTPHERO_7.png  1293  2017-09-13 18:40:06.428658   M5c84
Picture/RTPHERO_8.png  1293  2017-09-13 18:40:53.609472   M5c84
Picture/RTPHERO_9.png  1290  2017-09-13 18:41:15.713974   M5c84
[BONUS]_POLAROID_BASE.psd 1248 2017-09-13 18:35:07.128936  M5c84
```

**Nineteen minutes of one person's afternoon**, eight files saved in sequence at
thirty-to-sixty-second intervals, from one machine, and the `.psd`'s document id
is the same identifier as `RTPHERO_1.png`'s to the microsecond — the same
document lineage across two files.

**And the third witness is the XMP**, which states the same instants in local
time with an offset:

```
stEvt:when  2017-09-14T02:35:20+08:00   =  2017-09-13 18:35:20 UTC
UUID in RTPHERO_1                          2017-09-13 18:35:07.129 UTC
                                           12.871 s apart

stEvt:when  2017-09-28T11:27:21+08:00   =  2017-09-28 03:27:21 UTC
UUID in the .psd                           2017-09-28 03:26:58.580 UTC
                                           22.420 s apart
```

**Two clock formats, written by one program, agreeing to within half a minute,
twice, fifteen days apart.** That is the same shape of derivation as the ITSF
`u32`/FILETIME pairing, on a completely different file format, and it is the
second one this collection has.

The `+08:00` is a time zone and it is published as one: the machine that drew
the tutorial's pictures was set eight hours ahead of UTC. **What is not
published is the node field of those UUIDs**, which is where RFC 4122 puts a MAC
address ([12](12-whose-bytes.md)).

### The two witnesses that are not the author's

`rpg2003.chm` also carries two version-1 UUIDs, both reading **1997-03-15
12:41:51.615828 UTC** and both from one node. They are at offsets 11,939 and
12,038 and they are one string twice:

```
::DataSpace/Storage/MSCompressed/Transform/
    {7FC28940-9D31-11D0-9B27-00A0C91E9C7C}/InstanceData/…
```

**That is the LZX transform's identifier, a constant of the format**, and
`rpg2000.chm` carries the identical GUID at its own offsets 12,653 and 12,752.
**They date Microsoft generating a constant in 1997, not anybody compiling
anything in 2017**, and `uuidscan.py` prints them anyway because a tool that
silently filtered them would be choosing which timestamps count.

---

## The one clock that is neither product's

```
xmp:CreateDate  2015-08-03T10:28:57+08:00  =  2015-08-03 02:28:57 UTC
```

The `.psd` was **created two years before it was last modified**, on the same
machine's clock and in the same time zone. A source file older than the product
it ships inside, carried through an edit fifteen days after the help file was
compiled, into a tutorial project shipped by a publisher. It is the oldest true
date in the object that belongs to anybody who worked on it.

The only other pre-2017 dates that are real belong to third parties:
**2000-03-01** on Micco's library, **2009-12-05** on Nullsoft's helper, and
**2000** in sixty-two MIDI copyright lines that are the previous product's
([07](07-what-does-not-cross.md)).

---

## What the clocks still cannot say

* **when RPG Maker 2003 was made.** No date from 2002 or 2003 exists anywhere in
  the object. The product is called 2003 and nothing in it is dated then;
* **when Kadokawa built these binaries.** Every Borland stamp is a 1992
  constant and the two Ultimate DLLs' stamps are memory sizes;
* **when the tree was packaged.** 28 September 2017 is a floor, not a date;
* **any time zone for the mtimes**, which are this machine's local time and
  belong to the copy and not to the object.
