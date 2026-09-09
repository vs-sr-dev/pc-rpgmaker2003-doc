# 12 — whose bytes: the same man's manual gives two different addresses three years apart, a tutorial leaks its author's machine, and a leak this collection has now noticed twice is still there

*Measure: `python tools/sift.py rpgmaker2003-steam --group personal --show`, in
`notes/sift-personal.txt`; `python tools/utf16sift.py rpgmaker2003-steam`, in
`notes/utf16sift.txt`; `python tools/redact.py rpgmaker2003-steam/UNLHA32.TXT
--check --expect 3`, in `notes/redact.txt`; `python tools/redact.py selftest` —
14 checks, 0 failures; `python tools/uuidscan.py rpgmaker2003-steam --expect
19`, in `notes/uuidscan.txt`; `python tools/vendorhash.py rpgmaker2003-steam
--publisher KADOKAWA`, in `notes/vendorhash.txt`.*

---

## The parties, and there are eleven

| party | where it is named | new here |
|---|---|---|
| KADOKAWA GAMES | 4 version resources, 6 registry-key strings | |
| **Degica** | 2 `FileDescription` fields | **yes** |
| **Enterbrain Inc** | 6 licence blocks, 1 registry key | **yes** |
| ASCII Corporation | 62 MIDI copyright events (inherited bytes) | |
| Y. Kitagami | the same 62 | |
| **椎葉 大翼 / Daisuke Shiiba** | 21 MIDI copyright events | **yes** |
| **David "Cherry" Trapp** | a licence in 4 binaries, credits, form names, exports | **yes** |
| **Jasmin "Archeia" Toral** | the About box, twice | **yes** |
| **Jie Xin "Cy" Tan** | the About box, once | **yes** |
| Micco | 1 version resource, 1 manual, 2 addresses | |
| Borland, Nullsoft, Microsoft, Adobe, the W3C, the MMA, Valve | the toolchain, the formats and the shop | |

**Six new parties and four of them are named human beings.** The previous object
had Micco and Y. Kitagami and no Western publisher at all. `LegalCopyright` is
still empty on every Kadokawa binary, so the credit is still in the music, the
licences and one dialogue box — and not in the programs' own copyright fields.

---

## Micco, and the rule is applied rather than re-argued

```
python tools/sift.py rpgmaker2003-steam --group personal --show
blobs searched : 737   bytes : 33,578,445
e-mail shape        3        1     all three in UNLHA32.TXT
telephone shape     0        0
everything else     0        0
positive control fired : YES   negative control quiet : YES

python tools/utf16sift.py rpgmaker2003-steam        0
```

Three occurrences, two distinct addresses, one file, one man — and the file is
`UNLHA32.TXT`, the manual of a compression library, shipped unmodified inside
somebody else's product.

The rule and its amendment are already written in
`pc-rpgmaker2000-doc/docs/10` and produce the answer without new reasoning:
**publish what claims credit and redact what routes a message; where it cannot
be established that an address has stopped routing, redact.** All three
occurrences are redacted by program —

```
python tools/redact.py rpgmaker2003-steam/UNLHA32.TXT --check --expect 3
addresses : 3 replaced
```

— and Micco's name, his copyright line `(C)Micco 1995-2000`, his version
`1.47.1.7-VC` and his manual's own date are published. That is the whole
argument and it is not reopened.

**What is new is a fact about how long a contact detail lasts.**

| | the manual | the addresses |
|---|---|---|
| here | `UNLHA32.TXT`, 13,864 bytes, documenting version **1.47** (2000) | a Nifty-Serve member id, twice; **a second address at a different Japanese provider**, once |
| the 2000 | `unlha32.txt`, 17,649 bytes, documenting version **1.87** (2003) | a Nifty address, twice; the same member id, once |

**One man, one library, two manuals three years apart, and the older one gives a
provider the newer one does not mention at all.** The identifier that survives
both is the member id. This repository publishes neither, and publishes the
shape of the change, because the shape is the finding: a person's routable
address changed inside three years and their handle did not.

---

## The tutorial's author, and this is the case the rule was not written for

The rule was written for a signature block an author typed in order to be
credited. **The metadata in `Sample\ArcheiaPictureTutorial\` is not that.**
Nobody typed it; an image editor wrote it, and it says more about the person
than they wrote about themselves.

```
python tools/uuidscan.py rpgmaker2003-steam --expect 19
version-1 UUIDs : 19 in 10 file(s)
distinct node fields : 6
carrying a plausible date : 13 of 19
```

A version-1 UUID is two things at once. **The timestamp is an artefact and is
published in full** ([11](11-the-clocks.md)). **The node field is the position
RFC 4122 fills with the generating interface's MAC address, and it is not
printed anywhere in this repository.**

The rule extends by one sentence, and the extension is stated rather than
assumed:

> **A device identifier is neither credit nor routing, and it is redacted
> anyway.** It does not claim authorship and it does not carry a message. What
> it does is let a stranger join one person's files to their other files
> wherever those files went. The rule's own reason — that the cost of being
> wrong is not symmetric — applies unchanged: publishing it harms a person and
> withholding it costs a reader twelve hex digits that carry no information
> about the object.

**The redaction is by program**, so a document quoting `uuidscan.py` cannot leak
what the tool removed. In place of the node the tool prints a four-character
hash of it, which is enough to say *these nine identifiers came from one
machine* — which is the finding — without saying which machine.

Published, from the same metadata, because it is about the artefact and not
about routing: the timestamps, **the `+08:00` offset** in the XMP, the tool
(`Adobe Photoshop CC 2017 (Windows)`, `GLDPNG ver 3.3`), and the counts.

**And the author's name is published in full**, because it is in the product's
About box, under the heading `Translated by:` and again under `Localized and
Improved by:` ([09](09-the-sample-project.md)). A credits list is credit. The
same rule that redacts twelve hex digits publishes `Jasmin "Archeia" Toral`,
and there is no tension between those two: one is what a person put their name
to, the other is what a program wrote down about their hardware.

---

## The owner is almost absent, and the little there is stays out

`LastPlayed` is `"0"`. There is no save, no configuration, no project of the
owner's in the tree. Two things about this machine exist and neither is
reproduced:

* **`LastOwner`** in the manifest is a SteamID64 identifying the purchaser, and
  `steamacf.py` has redacted it by program for several objects;
* **`LauncherPath`** names a directory on this machine. It is not reproduced in
  any `.md` or in any file under `notes/`.

Rule 7 was checked over the whole repository and not only over the documents,
because the previous session's check found a violation inside a captured
traceback in `notes/` ([13](13-the-tools.md)).

---

## The third-party hash list, which has been asked for three times

`pc-rpgmaker2000-doc/docs/11` asked that a third-party component hash list be
published, because three consecutive objects ship Micco's library at three
different builds and **none of them crosses**:

```
pc-rpgmaker95-doc     151,552 bytes   0.71.0.5     (C)Micco 1995-97
pc-rpgmaker2000-doc   254,464 bytes   1.87.0.2     (C)Micco 1995-2002
pc-rpgmaker2003-doc   237,568 bytes   1.47.1.7-VC  (C)Micco 1995-2000
```

Nobody wrote one. **It is written here**, and the point is not the hashes —
`crossall.py` already reads the whole-tree list — it is the vendor column, which
lets a reader ask *who else ships Micco's library* instead of *which other object
has these exact bytes*.

The split is a stated test and not a judgement: **a third party is named in the
file and the publisher is not** makes it a component; both named makes it a
carrier.

```
python tools/vendorhash.py rpgmaker2003-steam --publisher KADOKAWA
components : 2    carriers : 7    total files : 9

## whole files that ARE a third party's
e1f338ef…  237568  UNLHA32.DLL                  Micco     LZH library   @103321
9ba229d3…   47790  BaseFlushAppcompatCache.exe  Nullsoft  NSIS runtime  @33800
```

Seven carriers follow, with their offsets: `rpg2003.exe`, `rpg_rt.exe.dat` and
its twin, `setup.exe.dat`, `ultimate_eb.dll`, `ultimate_rt_eb.dll.dat` and its
twin — every one of them naming Kadokawa **and** at least one of Borland, Cherry
or Microsoft.

The list's own limit is printed with it: **a marker in a file says the file
contains that string.** Two products carrying one vendor's marker at different
sha1 are carrying two builds, not one library — which is exactly why the vendor
column exists, because the hashes will not cross and the vendor will.

---

## And the leak in a published neighbour is still there

`pc-rpgmaker2000-doc/docs/13`, correction 1, recorded that
`pc-rpgmaker95-doc/tools/redact.py` — **the tool whose purpose is to remove
addresses** — carries a real one twice in its own selftest fixtures, in a
committed file.

```
grep -c  -E "<address shape>" ../pc-rpgmaker95-doc/tools/redact.py    3   lines
grep -o  -E "<address shape>" ../pc-rpgmaker95-doc/tools/redact.py | wc -l
                                                                     5   occurrences
… | grep -civ -E "(invalid|example|\.io$|\.co\.uk$|\.zz$)"           2   at a real domain

cd ../pc-rpgmaker95-doc && git ls-files tools/redact.py
tools/redact.py
```

**Five address shapes, three of them at reserved or obviously fictional domains
and two at a real one — the same real address, twice.**

**It had not been fixed.** The file was still tracked, the address was still in
it twice, and this was the second repository in a row to say so.

This session's copy of `redact.py` is the repaired one and carries the check
that would have caught it:

```
python tools/redact.py selftest
no address in this tool's own source is routable   ok   5 specimens, all reserved
14 checks, 0 failures
```

### And then it was fixed

The paragraph above was written to say that the fix is one commit in a
repository this session does not own, that the standing instruction is not to
modify a published neighbour, and that it would be recorded a third time if it
were still there. **The owner read that and authorised the commit**, so this
section reports what happened instead of what would have.

The repair is minimal and its scope is stated: **three fixtures and one
check**. The two that held the real address, plus the high-byte fixture whose
`.zz` is fictional but not reserved, now use `.invalid` and `.example` — the
two top-level domains RFC 2606 reserves so that they can never resolve — and
the check that this repository's own copy carries was added there too.

**The check is its own positive control, because it fails on the commit it
replaces:**

```
address shapes in the OLD tools/redact.py   : 5
of those, NOT at a reserved domain          : 5
distinct routable addresses among them      : 4
the real one appeared                       : 2 times

address shapes now                          : 5
of those, NOT at a reserved domain          : 0

over all 576 tracked files in that repository :
   address shapes 5, of those routable 0
```

`pc-rpgmaker95-doc/notes/redact-leak-repaired.txt` carries both controls and
**does not itself reproduce the address**, which is a trap this session walked
into once already: the first draft of that note printed the first character of
each redacted string and used `grep -oc`, which counts lines and not
occurrences, and reported "5 of 3".

**What was deliberately not changed is the module docstring.** The rule it
argues belongs to `pc-rpgmaker95-doc` and to the object it was written for; the
amendment `pc-rpgmaker2000-doc` added and the second amendment
[this chapter](#the-tutorials-author-and-this-is-the-case-the-rule-was-not-written-for)
adds belong to their own documents. **A repaired tool is not a licence to
rewrite a neighbour's argument.**

**Two repositories noticed it and the third one fixed it**, which is one more
than "a collection keeping a diary about not being careful" — and the thing
that closed it was not a better rule. It was somebody reading the sentence and
saying yes.
