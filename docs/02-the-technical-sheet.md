# 02 — the technical sheet: every figure this repository states, with the command that remakes it

*Measure: this chapter is the index of measurements. Every row carries the
command that produces it and the file under `notes/` that holds that command's
output. Nothing here is argued; the arguments are in the chapters the last
column names.*

Run everything from the repository root with `rpgmaker2003-steam\` in place.
That directory is **not** committed: it is the owner's installation, copied.

---

## The object

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| files | 737 | `python tools/hashall.py rpgmaker2003-steam` | `hashall.txt` | [01](01-the-object.md) |
| bytes | 33,578,445 | `find rpgmaker2003-steam -type f -printf "%s\n" \| awk '{s+=$1} END {print s}'` | — | [01](01-the-object.md) |
| distinct sha1 | 731 | `python tools/hashall.py rpgmaker2003-steam` | `hashall.txt` | [01](01-the-object.md) |
| directories | 41, 19 empty | `python _work/copyverify.py` | `copyverify.txt` | [01](01-the-object.md) |
| copy verified | 737/737 × 3 axes, 41/41, 19/19 | `python _work/copyverify.py` | `copyverify.txt` | [01](01-the-object.md) |
| empty directories, named | 4 in `RTP\`, 15 in `Sample\` | `find rpgmaker2003-steam -type d -empty` | `empty-dirs.txt` | [09](09-the-sample-project.md) |

## The shop

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| `SizeOnDisk` residue | 0 | `python tools/steamacf.py --path <steamapps>/appmanifest_362870.acf --root rpgmaker2003-steam --check` | `steamacf.txt` | [03](03-the-shop.md) |
| depot residue | 0 | the same | `steamacf.txt` | [03](03-the-shop.md) |
| app / depot / build | 362870 / 362871 / 2173406 | `python tools/steamacf.py --path <…>/appmanifest_362870.acf` | `steamacf-dump.txt` | [03](03-the-shop.md) |
| `BytesToDownload` | 22,100,528 | the same | `steamacf-dump.txt` | [03](03-the-shop.md) |
| per-file LZMA total | 22,422,597 | `python tools/compratio.py rpgmaker2003-steam --declared 22100528 --by-ext` | `compratio.txt` | [03](03-the-shop.md) |
| the same, deduplicated | 21,968,501 | see `notes/compratio-dedup.txt` | `compratio-dedup.txt` | [03](03-the-shop.md) |
| install script | 1,545 bytes | `python tools/cptext.py census rpgmaker2003-steam/2k3_install.vdf` | — | [03](03-the-shop.md) |
| registry keys in the tree | 11 distinct | see `notes/registry-keys.txt` | `registry-keys.txt` | [08](08-the-programs.md) |

## The coverage

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| specified | 730 files, 26,534,548 bytes, 79.0226 % | `python tools/coverage.py tree --root rpgmaker2003-steam` | `coverage-tree.txt` | [10](10-the-accounting.md) |
| decoded | 7 files, 7,043,897 bytes, 20.9774 % | the same | `coverage-tree.txt` | [10](10-the-accounting.md) |
| derived / opaque | 0 / 0 | the same | `coverage-tree.txt` | [10](10-the-accounting.md) |
| what the tool printed before | 78.8598 % / 20.9388 % / 0.2014 % | `notes/coverage-tree-before.txt` | `coverage-tree-before.txt` | [10](10-the-accounting.md) |
| coverage selftest | 32 checks, 0 failures | `python tools/coverage.py selftest` | `coverage-selftest.txt` | [10](10-the-accounting.md) |
| entropy | 432 of 1,041 blocks above 7.5, 17 rows | `python tools/entropy.py rpgmaker2003-steam --tree --by-ext` | `entropy.txt` | [01](01-the-object.md) |

## The map files, opened here

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| `.lmu` walks | 3 of 3 at residue 0 | `python tools/lcfmap.py walk rpgmaker2003-steam/Sample/ArcheiaPictureTutorial/Map0001.lmu --expect-residue 0` | `lcfmap-walk.txt` | [04](04-the-maps.md) |
| `.lmt` walk | residue 0, 4 entries | `python tools/lcfmap.py walk rpgmaker2003-steam/Sample/ArcheiaPictureTutorial/RPG_RT.lmt --expect-residue 0` | `lcfmap-walk.txt` | [04](04-the-maps.md) |
| map tree | `Picture Tutorial`, `Basement`, `Brian's House`, `World Map` | `python tools/lcfmap.py tree <…>/RPG_RT.lmt` | `lcfmap-tree.txt` | [04](04-the-maps.md) |
| map order | `[0, 3, 2, 1]` | the same | `lcfmap-tree.txt` | [04](04-the-maps.md) |
| geometry | forced to **20 × 15** | `python tools/lcfmap.py geometry <…>/Map000{1,2,3}.lmu --expect 20x15` | `lcfmap-geometry.txt` | [04](04-the-maps.md) |
| events | 10 + 19 + 6 = 35, all lists closing | `python tools/lcfmap.py events <…>/Map0002.lmu` | — | [04](04-the-maps.md) |
| `lcfmap.py` selftest | 19 checks, 0 failures | `python tools/lcfmap.py selftest` | — | [13](13-the-tools.md) |

## The two databases

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| both walk | 22 chunks each, tags 11..32, residue 0 | `python tools/lcf.py walk rpgmaker2003-steam/rpg_rt.ldb.dat --level 1` | `lcf-walk-root.txt` | [05](05-the-two-databases.md) |
| byte-identical chunks | **17 of 22**, 369,226 bytes each side | `python tools/lcfdiff.py rpgmaker2003-steam/rpg_rt.ldb.dat rpgmaker2003-steam/Sample/ArcheiaPictureTutorial/RPG_RT.ldb --only-text --verbose --expect-identical 17 --expect-differing 5` | `lcfdiff.txt` | [05](05-the-two-databases.md) |
| differing chunks | 5 — 11, 22, 24, 25, 29 | the same | `lcfdiff.txt` | [05](05-the-two-databases.md) |
| heroes | 14 → 1, `Zack`/`None` → `Brian`/`Survivor` | the same | `lcfdiff.txt` | [05](05-the-two-databases.md) |
| system sounds | `Decision1`→`2`, `Cancel1`→`2`, `Buzzer1`→`3` | the same, chunk 22 | `lcfdiff.txt` | [05](05-the-two-databases.md) |
| `lcfdiff.py` selftest | 17 checks, 0 failures | `python tools/lcfdiff.py --selftest` | — | [13](13-the-tools.md) |

## Against the collection

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| repositories in the collection | 134 `*-doc`, 65 `pc-*-doc` | `ls -1d ../*-doc/ \| wc -l` ; `ls -1d ../pc-*-doc/ \| wc -l` | — | [06](06-the-crossings.md) |
| crossings | **368 of 731** | `python tools/crossall.py notes/sha1-all.txt --collection .. --skip pc-rpgmaker2003-doc` | `crossall.txt` | [06](06-the-crossings.md) |
| swept | 104 repositories, 461 list files, 155,888 tokens | the same | `crossall.txt` | [06](06-the-crossings.md) |
| crossing bytes | 12,428,739 | `python tools/crossnames.py notes/sha1-all.txt ../pc-rpgmaker2000-doc/notes/sha1-all.txt --expect-crossing 368` | `crossnames.txt` | [06](06-the-crossings.md) |
| not crossing | **363**, 19,984,119 bytes | the same | `crossnames.txt` | [07](07-what-does-not-cross.md) |
| same name / renamed | 277 / 91 | the same | `crossnames.txt` | [06](06-the-crossings.md) |
| rename classes | **47 spaced + 3 prefixed + 41 retranslated** | the same | `crossnames.txt` | [06](06-the-crossings.md) |
| the `J` split, inherited 92 | **DISJOINT**, 17 at 4.245..15.634 s vs 75 at 29.565..174.993 s | `python tools/jingles.py rpgmaker2003-steam --tsv notes/smfcensus.tsv --crossing ../pc-rpgmaker2000-doc/notes/sha1-all.txt` | `jingles.txt` | [06](06-the-crossings.md) |
| the same over all 141 | **OVERLAPPING**, 18 J files | the same | `jingles.txt` | [06](06-the-crossings.md) |
| `crossnames.py` selftest | 14 checks, 0 failures | `python tools/crossnames.py --selftest` | — | [13](13-the-tools.md) |

## The programs

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| binaries | 9, PE32 9, NE 0 | `python tools/pecensus.py rpgmaker2003-steam --by-magic` | `pecensus.txt` | [08](08-the-programs.md) |
| NE refusal, per file | `no NE signature at e_lfanew=256 (found b'PE')` | `python tools/ne.py rpgmaker2003-steam/rpg2003.exe` | `ne.txt` | [08](08-the-programs.md) |
| the same tool on the tree | an uncaught `PermissionError`, **not** a refusal | `python tools/ne.py rpgmaker2003-steam` | `ne.txt` | [13](13-the-tools.md) |
| version resources | 6 of 9, editor and runtime both **1.1.2.1** | `python tools/verres.py dump rpgmaker2003-steam` | `verres.txt` | [08](08-the-programs.md) |
| false COFF stamps | **7 of 9 files, 5 of 7 distinct binaries** | `python tools/stampcheck.py rpgmaker2003-steam --expect-false 7` | `stampcheck.txt` | [11](11-the-clocks.md) |
| what `pecensus.py` says | `impossible mtimes : 0 of 9` | `python tools/pecensus.py rpgmaker2003-steam --by-magic` | `pecensus.txt` | [11](11-the-clocks.md) |
| build paths | 58 drive-letter paths, 39 distinct; **15 under `d:\ha\`, 10 distinct** | `python tools/buildroot.py --root rpgmaker2003-steam --file rpg2003.exe --needle "d:\ha\"` | `buildpaths.txt` | [08](08-the-programs.md) |
| the same by the generic tool | 17 hits in 3 files | `python tools/sift.py rpgmaker2003-steam --group buildpath --show` | `sift-buildpath.txt` | [08](08-the-programs.md) |
| Delphi version | **6.0**, from `Software\Borland\Delphi\6.0\FileFormat` | see `notes/registry-keys.txt` | `registry-keys.txt` | [08](08-the-programs.md) |
| `Enterbrain` in the bytes | 7 occurrences in 6 files | see `notes/enterbrain.txt` | `enterbrain.txt` | [08](08-the-programs.md) |
| exports, `ultimate_eb.dll` | 24 by name, incl. `Hook_WinHelpA` | `python tools/peimpexp.py rpgmaker2003-steam/ultimate_eb.dll --exports` | `peimpexp.txt` | [08](08-the-programs.md) |
| exports, `ultimate_rt_eb.dll` | 10 by name, incl. `ATBHandlerMain` | `python tools/peimpexp.py rpgmaker2003-steam/ultimate_rt_eb.dll.dat --exports` | `peimpexp.txt` | [08](08-the-programs.md) |
| embedded PE | `RCDATA/GAMEDELETE/9`, 142,848 = 142,848, residue 0 | `python tools/peembed.py rpgmaker2003-steam/setup.exe.dat` | `peembed-setup.txt` | [08](08-the-programs.md) |
| `MZP` | 4 of 737 begin with it, 5 occurrences in 4 files | `python tools/sigcount.py rpgmaker2003-steam --hex 4d5a5000` | `sigcount.txt` | [08](08-the-programs.md) |
| third-party components | **2 components, 7 carriers** | `python tools/vendorhash.py rpgmaker2003-steam --publisher KADOKAWA` | `vendorhash.txt` | [12](12-whose-bytes.md) |

## The help file

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| closures | 9, all residue 0 | `python tools/itsf.py header rpgmaker2003-steam/rpg2003.chm` | `itsf-header.txt` | [07](07-what-does-not-cross.md) |
| directory | 4 chunks `PMGL PMGL PMGL PMGI`, 530 entries, 3 index, 0 refusals | `python tools/itsf.py list rpgmaker2003-steam/rpg2003.chm` | `itsf-list.txt` | [07](07-what-does-not-cross.md) |
| inside | 523 project files + 7 `::` entries | the same | `itsf-list.txt` | [07](07-what-does-not-cross.md) |
| compiler / title | `HHA Version 4.74.8702` / `RPG Maker 2003` | `python tools/itsf.py internals rpgmaker2003-steam/rpg2003.chm` | `itsf-internals.txt` | [11](11-the-clocks.md) |
| compile clock | 2017-09-16 19:54:13 UTC | the same | `itsf-internals.txt` | [11](11-the-clocks.md) |
| the paired derivation | 7.551 ms apart, third specimen | the same | `itsf-internals.txt` | [11](11-the-clocks.md) |
| header LCID | 0x0C07, German (Austria) — same as the 2000's | `python tools/itsf.py header rpgmaker2003-steam/rpg2003.chm` | `itsf-header.txt` | [11](11-the-clocks.md) |

## The resource library

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| PNG | 355 of 355, residue 0, **1,848 of 1,848 CRCs verify** | `python tools/pngcensus.py rpgmaker2003-steam --by-dir --tsv notes/pngcensus.tsv` | `pngcensus.txt` | [07](07-what-does-not-cross.md) |
| palettes / IDAT streams | 231 distinct / 349 distinct over 355 | the same | `pngcensus.txt` | [07](07-what-does-not-cross.md) |
| the one `tIME` | `Sample\…\Picture\INPUTDISPLAY.png`, **2017-09-13 18:22:56 UTC** | `python tools/pngchunk.py rpgmaker2003-steam --type tIME --expect 1` | `pngchunk-time.txt` | [11](11-the-clocks.md) |
| the one `tpNg` | the same file, payload `GLD3\0\0\0\0`, CRC verifies | `python tools/pngchunk.py rpgmaker2003-steam --type tpNg --expect 1 --dump` | `pngchunk-tpng.txt` | [09](09-the-sample-project.md) |
| MIDI | 141 of 141, residue 0, 1,963 tracks, 797,748 events, 10,435.682 s | `python tools/smfcensus.py rpgmaker2003-steam --tsv notes/smfcensus.tsv` | `smfcensus.txt` | [07](07-what-does-not-cross.md) |
| copyright events | 83 = **62 Kitagami + 21 Shiiba** | `python tools/jingles.py rpgmaker2003-steam --tsv notes/smfcensus.tsv` | `jingles.txt`, `composers.txt` | [07](07-what-does-not-cross.md) |
| marker events | 58, in five spellings | `python tools/smfcensus.py rpgmaker2003-steam --text` | `smfcensus-text.txt` | [07](07-what-does-not-cross.md) |
| WAV | 216 of 216, 157 × 16-bit and 59 × 8-bit, all mono 22,050 Hz | `python tools/wavcheck.py rpgmaker2003-steam --by-dir` | `wavcheck.txt` | [07](07-what-does-not-cross.md) |
| the join | 299 of 299 resolve, 18 of 299 ambiguous | `python tools/rtpjoin.py rpgmaker2003-steam` | `rtpjoin.txt` | [07](07-what-does-not-cross.md) |

## The sample project

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| shape | 47 files, 2,107,878 bytes, 19 directories of which 15 empty | `find rpgmaker2003-steam/Sample -type d` | `empty-dirs.txt` | [09](09-the-sample-project.md) |
| touched vs copied | **11 of 14** shared names differ, 3 identical | `python tools/projdiff.py rpgmaker2003-steam/Sample/ArcheiaPictureTutorial --against rpgmaker2003-steam/RTP` | `projdiff.txt` | [09](09-the-sample-project.md) |
| its own files | 33 | the same | `projdiff.txt` | [09](09-the-sample-project.md) |
| references | 406 — **14 inside, 385 in the RTP, 7 nowhere** | `python tools/projjoin.py rpgmaker2003-steam/Sample/ArcheiaPictureTutorial --rtp rpgmaker2003-steam/RTP` | `projjoin.txt` | [09](09-the-sample-project.md) |
| the chipset chain | 3 of 3 resolve into the project's own `ChipSet\` | the same | `projjoin.txt` | [09](09-the-sample-project.md) |
| empty dirs whose RTP twin is used | 10 of 15 | see `notes/empty-dirs-analysis.txt` | `empty-dirs-analysis.txt` | [09](09-the-sample-project.md) |
| the PSD | 196 × 123, 3 channels, depth 8, colour mode **3 = RGB**, residue 0 | `python tools/psd.py "rpgmaker2003-steam/Sample/ArcheiaPictureTutorial/Picture/[BONUS]_POLAROID_BASE.psd" --resources` | `psd.txt` | [09](09-the-sample-project.md) |
| version-1 UUIDs | 19 in 10 files, 6 distinct node fields | `python tools/uuidscan.py rpgmaker2003-steam --expect 19` | `uuidscan.txt` | [11](11-the-clocks.md) |

## The personal data

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| address shapes | 3 in 1 blob, all in `UNLHA32.TXT` | `python tools/sift.py rpgmaker2003-steam --group personal --show` | `sift-personal.txt` | [12](12-whose-bytes.md) |
| redaction | 3 replaced | `python tools/redact.py rpgmaker2003-steam/UNLHA32.TXT --check --expect 3` | `redact.txt` | [12](12-whose-bytes.md) |
| sixteen-bit pass | 0 extra hits | `python tools/utf16sift.py rpgmaker2003-steam` | `utf16sift.txt` | [12](12-whose-bytes.md) |
| `redact.py` selftest | 14 checks, 0 failures | `python tools/redact.py selftest` | `redact-selftest.txt` | [12](12-whose-bytes.md) |
| the neighbour's leak | **still present**, 2 occurrences in a committed file | `grep -c -E "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}" ../pc-rpgmaker95-doc/tools/redact.py` | — | [12](12-whose-bytes.md) |

## The harness

| figure | value | command | note | chapter |
|---|---:|---|---|---|
| the box, as it arrived | 528 `.py`, 0 differing against the predecessor | `python tools/toolsdiff.py ../pc-rpgmaker2000-doc/tools --ignore predbands.py --ignore toolsdiff.py --expect-differing 0 --expect-common 528` | `toolsdiff.txt` | [13](13-the-tools.md) |
| forbidden bytes | 0, three controls firing | `python tools/toolscan.py` | `toolscan.txt` | [13](13-the-tools.md) |
| refusals, unextended | 67 readers, 42 refused, 25 exit 0 | `python tools/refusals.py rpgmaker2003-steam` | `refusals.txt` | [13](13-the-tools.md) |
| classified | **23 argparse + 9 oserror + 9 format + 1 exception** | `python tools/refusalclass.py notes/refusals.txt` | `refusalclass.txt` | [13](13-the-tools.md) |
| refusals, extended | 76 readers, 41 refused, 35 exit 0 | `python tools/refusals.py rpgmaker2003-steam` after the extension | `refusals-extended.txt` | [13](13-the-tools.md) |
| `jstore.py` | residue 0 on all six LCF files, four of them with zero terms | `python tools/jstore.py <file>` | `jstore.txt` | [13](13-the-tools.md) |
| `kfaccount.py` | exit 0 printing its usage, fifth | `python tools/kfaccount.py --root rpgmaker2003-steam` | `kfaccount.txt` | [13](13-the-tools.md) |
| `namecensus.py` | `ZeroDivisionError`, twenty-first | `python tools/namecensus.py rpgmaker2003-steam` | `namecensus.txt` | [13](13-the-tools.md) |
| `dircensus.py` | a full table over zero, exit 0, twenty-second | `python tools/dircensus.py rpgmaker2003-steam` | `dircensus.txt` | [13](13-the-tools.md) |
| `mzcensus.py` | 3 of 9, missing 2,425,856 bytes, tenth | `python tools/mzcensus.py rpgmaker2003-steam` | `mzcensus.txt` | [13](13-the-tools.md) |
| `protscan.py` | 9 of 737 files, 0 hits, control fires on 9, seventeenth | `python tools/protscan.py rpgmaker2003-steam` | `protscan.txt` | [13](13-the-tools.md) |
| `pdbpaths.py` | 6 binaries examined, 0 paths, on a binary with 58 | `python tools/pdbpaths.py --root rpgmaker2003-steam` | `buildpaths.txt` | [13](13-the-tools.md) |
| clause count | 63 | `python tools/predcount.py` | — | [16](16-prediction-scoring.md) |
| the P11 bands | lands 7, constructs 12, nonnumeric 8 | `python tools/predbands.py --expect-under 0.60 5` | — | [16](16-prediction-scoring.md) |
