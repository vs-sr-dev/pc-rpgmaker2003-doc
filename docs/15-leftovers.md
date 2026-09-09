# 15 — leftovers: what this object still holds, and thirty-two initialisms sorted by how well the object supports them

*Measure: nothing in this chapter is a finding. Each entry names what would
settle it and what it would cost, so that a later session can pick the cheap
ones. The expansions table is counted and the four counts sum.*

---

## Inside the formats

**What the other seven `.lmu` fields hold.** Tags 11, 42, 50, 60, 61, 62 and 90
are read here as lengths and offsets and not as meanings. Tags 60, 61 and 62 are
36 bytes each in all three maps and 62's contents read as 18 `u16`, which is a
table of eighteen somethings. **Three specimens is enough to see which fields
vary and which do not, and that comparison was not made.**

**Which of database chunks 24 and 25 is switches and which is variables.** One
went 100 → 200 records with nine names, the other 10 → 20 with none, and chunk
25's records carry `{11: 5, 21: 4, 22: 0}` identically in all thirty. **What
would settle it is a reference from an event command list to a numbered switch
or variable**, which is inside the `.lmu` event pages this session walked but
did not decode ([05](05-the-two-databases.md)).

**What the six new chunks 27..32 hold.** Three of the six — 27, 28 and 31 — are
declared with a size of **zero in both databases**, which is itself the finding
that they are reserved and unused. Chunk 29 is 162 and 159 bytes and differs
between the two; chunks 30 and 32 are 23,487 and 19,069 bytes and are
byte-identical, holding 18 and 32 named records.

**Whether any RPG Maker 2003 map that is not 20 × 15 declares its size.** All
three here omit the field and all three are 20 × 15 by a forced factorisation.
**One map of any other size would turn a derivation into a demonstration**, and
this object has none ([04](04-the-maps.md)).

**What the four zero bytes after `GLD3` would hold** in the `tpNg` chunk. One
occurrence in 1,848 chunks, eight bytes, four of them zero.

**Whether the 523 files inside `rpg2003.chm` overlap the 2000's 475.** Neither
object publishes the hashes of what is inside its help file. **This is the same
blindness `pc-rpgmaker95-doc`'s twelve-hash decision created, one level further
in**, and the fix is the same shape: publish a hash list of the container's
contents ([06](06-the-crossings.md)).

---

## Inside the programs

**What `ha` is.** `D:\ha\02rpg2000\2003\` is a third party's build root and the
two letters are not expanded anywhere in 33,578,445 bytes.

**Why `setup.exe.dat` carries the Delphi registry keys twice.** At 128,844 and
595,296, a difference of 466,452 — which is **not** the embedding offset of the
inner PE at 483,728. Two copies of a Delphi runtime at a delta that does not
match the container boundary is a small puzzle with a definite answer.

**Whether `ultimate_eb.dll`'s 24 exports are all called.** An export table is
what a DLL offers, not what a program uses, and `rpg2003.exe`'s import table was
not read against it.

**Whether the editor accepts `.r3project`.** The installer registers it, the
hook DLL's file mask says `.r3proj`, the editor executable contains neither
string, and the only way to find out is to run the thing ([03](03-the-shop.md)).

**Whether the German-Austrian compile locale and the German developer are the
same machine.** `rpg2000.chm` and `rpg2003.chm` both carry LCID 0x0C07 in their
ITSF headers, and the editor carries a licence and form classes belonging to a
developer whose credited work is the localisation. **This repository states the
coincidence and refuses the inference**, because a locale identifies a setting
and not a person ([11](11-the-clocks.md)).

---

## Inside the sample project

**Who `Inti` and `Lenne` are.** Two event names in `Map0001.lmu`, in neither
database, in no other file. `ALEX` beside them is the 2000's default hero.

**Why `RTPHERO_5.png` carries no XMP** when the other eight do. It is 1,720
bytes against their 16,652 to 17,277, so it is a different kind of image, and
eight of nine files from one afternoon carrying metadata while the ninth does
not is a small anomaly with a cheap answer.

**Whether the 289 new PNG are redrawn or resized versions of the 2000's.** The
palettes differ (231 distinct over 355), the dimensions differ (127 distinct
pairs), and `crossall.py` compares sha1 and nothing else. **A perceptual or
palette-level comparison is a different tool and would answer a real question**:
whether *re-authored* means redrawn or re-encoded ([07](07-what-does-not-cross.md)).

**What the event pages' remaining eleven fields are.** They walk; they are
almost certainly a command list; nothing here decoded one.

---

## Against the collection

**The remaining 0.60 % of the download figure.** Deduplicated per-file LZMA
comes to 21,968,501 against a declared 22,100,528. The 132,027-byte gap is chunk
framing and a packer that is not LZMA-9-extreme, and a third Steam object would
say whether the gap is a constant ([03](03-the-shop.md)).

**Whether `pc-rpgmaker95-doc`'s 256 withheld files would cross.** They include a
1999 build of the same audio library. **The decision not to publish them is not
reopened and the cost of it is now measurable**: this object's 211 WAV cross
into the 2000 and cannot be checked against the 95 at all.

**Whether the two neighbours will publish third-party hash lists.** This one
does ([12](12-whose-bytes.md)). The request has now been made three times and
answered once.

---

## The expansions, sorted by what the object supports

**Thirty-two initialisms**, each in exactly one of four buckets. The buckets are
about *this object's* evidence and not about whether the expansion is common
knowledge.

### Demonstrated from the object — 6

| | expansion | where the object says so |
|---|---|---|
| `LMU` | `LcfMapUnit` | the file's own eleven-byte header |
| `LMT` | `LcfMapTree` | the same |
| `LDB` | `LcfDataBase` | the same |
| `RTP` | Run Time Package | `2k3_install.vdf` writes `RuntimePackagePath` = `%INSTALLDIR%\RTP` |
| `r3proj` | RPG Maker 2003 project | `HKEY_CLASSES_ROOT\.r3project` → `RPG2003.Project` → `"RPG Maker 2003 Project File"` |
| `2k3` | 2003 | `RM2k3 custom version for Degica` in a file whose `ProductName` is `RPG Maker 2003`, and `…\Steam\Apps\RM2k3 Flush DEP again` for app 362870 |

### Derived here from the bytes — 3

| | expansion | the derivation |
|---|---|---|
| `EB` | Enterbrain | the only file in 737 carrying `Software\Enterbrain\RPG2003` is `ultimate_eb.dll`, one of the two whose names carry the letters; `Enterbrain Inc` is named in six files ([08](08-the-programs.md)) |
| `SE` | sound effect | the three files that gained the prefix are the three `.wav` filed among the `.mid`, and no `.mid` gained it ([06](06-the-crossings.md)) |
| `J` | jingle | seventeen inherited files with it at 4.245–15.634 s against seventy-five without at 29.565–174.993 s, on two independent axes agreeing on 140 of 141 files |

### Attributed to a public source, not demonstrated here — 10

`PSD` (Photoshop Document — Adobe), `NSIS` (Nullsoft Scriptable Install System),
`DEP` (Data Execution Prevention — Microsoft), `XMP` (Extensible Metadata
Platform — Adobe), `UUID` (Universally Unique Identifier — RFC 4122), `MAC`
(Media Access Control — RFC 4122 names the field), `DLL` (Dynamic-Link Library —
Microsoft), `PNG` (Portable Network Graphics — W3C / ISO 15948), `MIDI` (Musical
Instrument Digital Interface — MMA RP-001), `cp932` (a Microsoft code page for
Shift-JIS).

**The object contains evidence for the party in every one of these** —
`8BPS`, `NullsoftInst`, `DisableNXShowUI`, the Adobe XMP namespace URLs, the PNG
signature, `MThd` — **and expands none of the letters.**

### Not demonstrated — 13

`LCF` (the three file headers begin `Lcf` and nothing expands it), `VDF`, `ACF`,
`NX` (from `DisableNXShowUI`), `HHA` (from `HHA Version 4.74.8702`), `RSA`
(inferred from a 128-byte signature block the object calls only `kvsignatures`),
`ATB` (from `ATBHandlerMain`), `ITSF`, `LZX` (from the `LZXC` tag), `GLD` (from
`GLDPNG ver 3.3` and the `tpNg` payload `GLD3`), `PMGL`, `PMGI`, `CHM`.

```
6 demonstrated + 3 derived + 10 attributed + 13 not demonstrated = 32
```

The previous object's four counts were 12, 4, 6 and 5 over twenty-seven.
**The demonstrated share fell from 12 of 27 to 6 of 32**, and the reason is not
that this object says less: it is that this session went looking for more
initialisms, and the ones a hunt turns up are by construction the ones nothing
expands.

---

## The question this object was set, answered

> When half an object is already documented by another repository, and your
> readers open 99.7986 % of what is left without a change, and what nobody has
> ever opened is twelve thousand nine hundred and seventy bytes in four files —
> what is a discovery?

**Four things were discovered here and none of them is a format.**

1. **A geometry nothing declares.** 20 × 15, forced by a layer length, a cell
   width and two event coordinates, out of files that carry no width or height
   field at all.
2. **A person's afternoon.** Nineteen minutes on 13 September 2017, eight files
   saved in sequence, read out of UUID node fields and XMP timestamps that agree
   with each other to within half a minute — in an object every one of whose
   filesystem dates was destroyed by Steam.
3. **What a person changes.** Seventeen database chunks identical, five not:
   thirteen heroes deleted, one renamed, a party of four cut to one, three
   system sounds swapped, and the one window skin of four that they redrew is
   the one they selected.
4. **A name.** `Jasmin "Archeia" Toral`, in the About box, twice, which turns
   `Sample\ArcheiaPictureTutorial\` from an anonymous leftover into signed work.

> And when a rename in a list of file names confirms a reading the previous
> session had to derive from a distribution of durations, who made the
> measurement?

**Neither session alone.** The derivation was one axis over seventeen files and
could have been coincidence; the file names are a second axis and cost nothing.
What made it a measurement is that two independent axes agree on 140 of 141
files **and that the one disagreement has an explanation** — `J2003Horn.mid`,
whose file name took the convention and whose internal sequence name did not,
because the publisher applied it and the new composer did not.

And the confirmation was free only because somebody published 477 hashes of a
tree instead of twelve hashes of an archive. **Half the credit belongs to a
decision about publishing, which is the least glamorous half and the one this
collection controls.**
