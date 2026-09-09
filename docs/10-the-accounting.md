# 10 — the accounting: 67,623 bytes in the wrong bucket, and the two halves of them need two different sentences

*Measure: `python tools/coverage.py tree --root rpgmaker2003-steam` before and
after, in `notes/coverage-tree-before.txt` and `notes/coverage-tree.txt`;
`python tools/coverage.py selftest` — **32 checks, 0 failures**, in
`notes/coverage-selftest.txt`. The four buckets are defined in
`pc-rpgmaker2000-doc/docs/09` and are applied here, not redefined.*

---

## The bucket definitions, applied and not re-argued

> **SPECIFIED** — a document describing the format was published by the party
> that created it, or by a standards body that adopted it, and that document is
> what an implementer works from.
>
> **DECODED** — no such document exists, and an independent published
> third-party reverse engineering does — one this repository can name.
>
> **DERIVED** — this session worked it out of the bytes and can name no public
> account of it.
>
> **OPAQUE** — none of the above.

The bucket describes the format's public standing and not this session's route
to it. Both new rows below are DECODED even though every field this repository
uses was derived from the bytes, because the question a bucket answers is *could
a stranger check this against something*, and EasyRPG implements all three LCF
variants.

---

## The tool was wrong, and it was wrong quietly

Before this session, `coverage.py` classified by a magic table that knew
`LcfDataBase` and did not know `LcfMapUnit`, `LcfMapTree` or `8BPS`:

```
specified   729 files   26479895 bytes   78.8598 %
decoded       3 files    7030927 bytes   20.9388 %
derived       0 files          0 bytes    0.0000 %
opaque        5 files      67623 bytes    0.2014 %
SUM         737 files   33578445 bytes  100.0000 %   residue 0
```

**It printed a complete table, closed at residue 0, and put 67,623 bytes in the
wrong bucket.** The residue closing proves the *accounting* and says nothing
about the *classification*, which is the whole reason the tool's own footer
warns that the SUM row is an accounting figure and not a coverage figure. A
classifier that refuses is a nuisance; a classifier that is confidently wrong
and closes is a hazard, and this is that defect's first appearance.

Three magics were added, with the same length-prefixed shape as the existing
`LcfDataBase` probe rather than a substring search, and six selftest checks
including two that must fail:

```
an LcfMapUnit is DECODED                              ok
an LcfMapTree is DECODED                              ok
the two map variants are told apart                   ok
a wrong length prefix on LcfMapUnit is not one        ok
a PSD is SPECIFIED, because Adobe published the format ok
a PSD is named as Adobe's                             ok

32 checks, 0 failures
```

---

## The table, after

```
python tools/coverage.py tree --root rpgmaker2003-steam
denominator : 737 files, 33578445 bytes -- classified BY MAGIC
```

| bucket | files | bytes | share | format |
|---|---:|---:|---:|---|
| specified | 216 | 10,426,824 | 31.0521 % | RIFF WAVE (Microsoft and IBM) |
| specified | 9 | 7,893,678 | 23.5082 % | PE / MZ executable (Microsoft) |
| specified | 355 | 5,174,453 | 15.4100 % | PNG (W3C / ISO 15948) |
| specified | 141 | 2,945,749 | 8.7727 % | Standard MIDI File (MMA RP-001) |
| specified | 1 | **54,653** | 0.1628 % | **Adobe Photoshop PSD (Adobe, published)** |
| specified | 1 | 23,558 | 0.0702 % | Windows icon |
| specified | 1 | 13,864 | 0.0413 % | plain text, Shift-JIS (JIS X 0208; cp932) |
| specified | 6 | 1,769 | 0.0053 % | plain text, ASCII |
| decoded | 1 | 6,268,124 | 18.6671 % | Microsoft ITSF — chmlib, 7-Zip |
| decoded | 2 | 762,803 | 2.2717 % | LCF database — the EasyRPG project |
| decoded | 3 | **12,635** | 0.0376 % | **LCF map unit** |
| decoded | 1 | **335** | 0.0010 % | **LCF map tree** |
| **specified** | **730** | **26,534,548** | **79.0226 %** | |
| **decoded** | **7** | **7,043,897** | **20.9774 %** | |
| derived | 0 | 0 | 0.0000 % | |
| opaque | 0 | 0 | 0.0000 % | |
| **sum** | **737** | **33,578,445** | 100.0000 % | residue **0** |

**79.0226 %, not 79.0225 %.** 26,534,548 ÷ 33,578,445 = 0.79022563…, which to
four decimal places is 79.0226 %. The pre-briefing published 79.0225 % for the
specified share and 20.9775 % for the decoded one — truncating one and rounding
the other, in opposite directions, from the same division
([14](14-corrections.md)).

The previous three objects started from **0.8387 %**, **2.1516 %** and
**75.7882 %**.

---

## The two sentences, which are not one sentence

The 67,623 bytes the tool had in OPAQUE are two different things and each needs
its own statement. Writing one sentence about "what the box cannot read" would
merge a fact about the world with a fact about the box.

> **12,970 bytes in four files are in a format no vendor ever specified.**
> `LcfMapUnit` and `LcfMapTree` have no published description from Kadokawa,
> Enterbrain or ASCII. The only public account of them is the EasyRPG project's,
> which is a reverse engineering. **A reader who wants to check this
> repository's map chapter against something other than this repository has one
> place to go and it is not the vendor.** They are DECODED, and this session
> derived every field it uses from the bytes ([04](04-the-maps.md)).

> **54,653 bytes in one file are in a format the vendor published.** Adobe's
> Photoshop file format specification is a document from the company that made
> the format. **Nothing about that file was ever hard; it was simply never
> read**, because in eight sessions and 528 tools this pipeline had not met a
> `.psd`. It is SPECIFIED, and the 138 lines of `psd.py` that read it are an
> implementation of somebody else's document ([09](09-the-sample-project.md)).

**The first is a statement about the world: a company shipped a format and told
nobody how it works. The second is a statement about this box: a format was
public for thirty years and this collection had no reader for it.** They came to
the same 0.2014 % in the same OPAQUE row and they are not the same finding.

---

## What the coverage figure is worth

The same limit the previous object stated is carried unchanged, because it has
not stopped being true:

**SPECIFIED and DECODED carry warrants of different strength and the SUM of them
is not a coverage figure.** 79.0226 % of this object is in formats somebody
documented and 20.9774 % is in formats somebody reverse-engineered in public,
and the second number is dominated by one 6.2 MB help file. Adding them gives
100 % and means only that the bytes add up.

**And the classification is by magic and not by extension**, which on this object
matters by 1,788,416 bytes: three files named `.dat` are PE32, one named `.dat`
is a database, and an extension table would have put all four in one row.
