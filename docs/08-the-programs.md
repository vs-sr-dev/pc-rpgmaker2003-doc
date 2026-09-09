# 08 — the programs: nine binaries that name their own source files, a German developer's licence, and Enterbrain in a registry key

*Measure: `python tools/pecensus.py rpgmaker2003-steam --by-magic`, in
`notes/pecensus.txt`; `python tools/verres.py dump rpgmaker2003-steam`, in
`notes/verres.txt`; `python tools/peimpexp.py <file> --exports|--imports`, in
`notes/peimpexp.txt`; `python tools/buildroot.py --root rpgmaker2003-steam
--file rpg2003.exe --needle "d:\ha\"`, in `notes/buildpaths.txt`; the string
sweeps in `notes/enterbrain.txt` and `notes/registry-keys.txt`; `python
tools/vendorhash.py rpgmaker2003-steam --publisher KADOKAWA`, in
`notes/vendorhash.txt`.*

---

## The census

```
python tools/pecensus.py rpgmaker2003-steam --by-magic
binaries examined : 9     by format : PE32 9     NE : 0
```

| file | bytes | linker | COFF stamp (UTC) | stub |
|---|---:|---:|---|---|
| `rpg2003.exe` | 4,387,328 | 2.25 | 1992-06-19 22:22:17 | `MZP` |
| `rpg_rt.exe.dat` | 1,032,704 | 2.25 | 1992-06-19 22:22:17 | `MZP` |
| `Sample\…\RPG_RT.exe` | 1,032,704 | 2.25 | 1992-06-19 22:22:17 | `MZP` |
| `setup.exe.dat` | 630,784 | 2.25 | 1992-06-19 22:22:17 | `MZP` |
| `ultimate_eb.dll` | 274,944 | 2.24 | 1970-01-25 06:32:32 | `MZ 90` |
| `UNLHA32.DLL` | 237,568 | 3.00 | 2000-03-01 02:30:53 | `MZ 90` |
| `ultimate_rt_eb.dll.dat` | 124,928 | 2.24 | 1970-01-01 18:12:16 | `MZ 90` |
| `Sample\…\ultimate_rt_eb.dll` | 124,928 | 2.24 | 1970-01-01 18:12:16 | `MZ 90` |
| `BaseFlushAppcompatCache.exe` | 47,790 | 6.00 | 2009-12-05 22:50:52 | `MZ 90` |

All nine found **by magic**, including the three named `.dat`. `ne.py` refuses
cleanly and says why: `no NE signature at e_lfanew=256 (found b'PE')`. Seven of
the nine stamps are false and that is [11](11-the-clocks.md).

**`mzcensus.py`, tenth appearance, finds three of nine** and misses 2,425,856
bytes, because it filters on the `.EXE` extension. **`pecensus.py` truncates a
long path from the left** and prints
`mple/ArcheiaPictureTutorial/ultimate_rt_eb.dll`, which is a display defect in
its first appearance and is discussed in [13](13-the-tools.md).

---

## Fifteen source paths, and the previous object had none

```
python tools/sift.py rpgmaker2003-steam --group buildpath --show
drive-letter path   17 hits in 3 files
   BaseFlushAppcompatCache.exe   x1   C:\Program        (an NSIS default)
   UNLHA32.DLL                   x1   C:\TMP\UNLHA32.LOG
   rpg2003.exe                  x15
```

| offset(s) | path |
|---|---|
| 617784, 618024 | `D:\ha\02rpg2000\2003\RPG_RT\AuroraSheet.pas` |
| 715188, 715364, 716624, 717772 | `D:\ha\02rpg2000\2003\RPG_RT\MapEditUtils.pas` |
| 667936 | `D:\ha\02rpg2000\2003\RPG_RT\LD_Event.pas` |
| 712596 | `D:\ha\02rpg2000\2003\RPG_RT\GR_ChipSet.pas` |
| 945468 | `D:\ha\02rpg2000\2003\MapEditor.pas` |
| 966652, 968864 | `D:\ha\02rpg2000\2003\ED_Player2.pas` |
| 986668 | `D:\ha\02rpg2000\2003\ED_Player.pas` |
| 1351244 | `D:\ha\02rpg2000\2003\ED_Job.pas` |
| 1602012 | `D:\ha\02rpg2000\2003\ED_MoveRoute.pas` |
| 1607252 | `D:\ha\02rpg2000\2003\RPG2003.hlp` |

**Eight Delphi source units and one help file, from the machine of whoever wrote
the editor.** The previous object had to infer Delphi from a `TPF0` form
resource and a `TFileOperationOption` string; this one names its own `.pas`
files. Three things follow and each is separate:

* **`02rpg2000\2003`.** The 2003 was compiled inside a directory tree named
  after the 2000. Neither product's documentation says the two share a source
  tree and the build path does;
* **`RPG2003.hlp`** is WinHelp, referenced by a runtime error string, in a
  product that ships a `.chm` and no `.hlp`. **That is resolved below and it is
  resolved by an export table**;
* **`D:\ha\`** is a third party's build root. The standing rule publishes it;
  rule 7 is about *this* machine's paths and does not touch it.

**And the specialised tool for build roots was blind to all of it.** Pointed at
the same binary with its own defaults, `buildroot.py` fails on a path
hard-coded from `pc-karmaflow-doc`; given a root, a file and a needle it works
and finds more than `sift.py` did:

```
python tools/buildroot.py --root rpgmaker2003-steam --file rpg2003.exe \
    --needle "d:\ha\"

drive-letter paths, NUL-terminated : 58, distinct 39
of those under d:\ha\              : 15, distinct 10
```

**Fifty-eight drive-letter paths, thirty-nine distinct**, of which the ten under
`d:\ha\` are the ones that name source. And `pdbpaths.py --root` reports
**6 binaries examined, 0 carrying a CodeView RSDS path, `drive letters : {}`** —
correct, and useless here, because Borland does not emit CodeView records. A
generic string sweep found fifteen paths in one line and the specialised reader
found none ([13](13-the-tools.md)).

---

## The compiler names its own version

```
grep -a "Software\\\\Borland" over the tree

Software\Borland\Delphi\6.0\FileFormat   rpg2003.exe @135748
                                         rpg_rt.exe.dat @129408
                                         setup.exe.dat @128844 and @595296
Software\Borland\Delphi\Locales          the same four
Software\Borland\Locales                 the same four
```

**Delphi 6**, in a registry key the runtime library reads, in the editor, the
runtime and the installer. The pre-briefing had *Delphi* from a file extension;
the object gives the version. `setup.exe.dat` carries each key twice, at 128,844
and 595,296, because it contains a second copy of itself
([the embedded PE](#the-container-inside-a-binary)).

---

## Six version resources, and a ninth party in a field a compiler wrote

```
python tools/verres.py dump rpgmaker2003-steam        6 of 9 PE
```

| file | CompanyName | FileDescription | version |
|---|---|---|---|
| `rpg2003.exe` | KADOKAWA GAMES | RPG Maker 2003 Editor | **1.1.2.1** |
| `rpg_rt.exe.dat` | KADOKAWA GAMES | RPG Maker 2003 Runtime | **1.1.2.1** |
| `Sample\…\RPG_RT.exe` | the same bytes | | |
| `ultimate_eb.dll` | KADOKAWA GAMES | **Ultimate DLL (RM2k3 custom version for Degica)** | 1.1.2.1 |
| `ultimate_rt_eb.dll.dat` | KADOKAWA GAMES | **Ultimate Runtime DLL (RM2k3 custom version for Degica)** | 1.1.2.1 |
| `UNLHA32.DLL` | *(empty)* | LZH file processing library | **1.47.1.7-VC** |

**The editor and the runtime agree at 1.1.2.1**, where the previous object's
disagreed 1.6.2.0 against 1.6.1.0 and `pc-rpgmaker2000-doc/docs/14` left it
open. **It is not a property of this product line.**

**`Degica` is named twice**, in a field a compiler wrote, and it is the first
Western publisher named in the bytes of any of the three objects. `LegalCopyright`
is empty on every Kadokawa binary, exactly as it was on the 2000's.

**And `UNLHA32.DLL` is older than the previous object's**:

| | bytes | version | copyright | linker |
|---|---:|---|---|---:|
| here | 237,568 | 1.47.1.7-VC | (C)Micco 1995-2000 | 3.00 |
| the 2000 | 254,464 | 1.87.0.2 | (C)Micco 1995-2002 | 5.02 |
| the 95 | 151,552 | 0.71.0.5 | (C)Micco 1995-97 | — |

**The newer product ships the older library**, from a different toolchain —
`-VC` and linker 3.00 against the 2000's 5.02 — and `CompanyName` is empty here
where the 2000's said `MicSoft`. It does not cross, for the third time
([12](12-whose-bytes.md)).

---

## Enterbrain is in the bytes, and `eb` is answered as far as it can be

`pc-rpgmaker2000-doc/docs/03` put the chain ASCII → Enterbrain → Kadokawa
outside the bytes. It is inside them here.

```
Enterbrain, ASCII and UTF-16, over all 737 files
files carrying the string : 6      occurrences : 7
```

Six of the seven are one 490-character licence paragraph, in `rpg2003.exe`,
`rpg_rt.exe.dat`, `Sample\…\RPG_RT.exe`, `ultimate_eb.dll` and both copies of
`ultimate_rt_eb.dll`:

> *…Since aforementioned software is directly integrated into code owned by a
> third-party company (**Enterbrain Inc**), paragraph 3.1 of the license
> applies. Therefore, for information regarding rights to modify and/or
> redistribute this software, please refer to the End-User License Agreement of
> the product (**RPG Maker 2003**) by the third-party company which encapsulates
> this software…*

**The seventh is a registry key and it is the one that decides anything:**

```
Software\Enterbrain\RPG2003          1 hit   ultimate_eb.dll @150944
Software\KADOKAWA\RPG2003            6 hits  rpg2003.exe, rpg_rt.exe.dat,
                                             setup.exe.dat (×2), …
```

and the value name under it is `ApplicationPath`, which is exactly the value
name `2k3_install.vdf` writes under `Software\KADOKAWA\rpg2003`
([03](03-the-shop.md)).

**So the object contains, in one product, the same setting under two vendors'
keys**: Kadokawa's binaries use the Kadokawa key; the third-party hook DLL still
reads the Enterbrain one. That is the corporate succession, fossilised in a
registry path, and it is the first time this collection has it in bytes rather
than in a claim.

**What it does not prove is the expansion of `eb`.** Two letters in a file name
are still two letters in a file name. What the object now supports is stronger
than the pre-briefing's hypothesis and weaker than a demonstration: **the only
file in 737 that carries `Software\Enterbrain\…` is `ultimate_eb.dll`**, one of
the two whose names carry the letters, and the string was searched for in ASCII
and UTF-16 over every byte of the tree.

---

## A tenth party, and he is a person

The licence paragraph above is the tail of a longer block, and its head names
its author:

> *This product contains software developed by **David "Cherry" Trapp** which is
> subject to the following license: {{Copyright (C) **2006-2017**, David
> "Cherry" Trapp / All rights reserved. …}}*

A four-clause BSD-shaped licence with an advertising clause, in `rpg2003.exe`,
`rpg_rt.exe.dat`, `ultimate_eb.dll` and `ultimate_rt_eb.dll`. **`vendorhash.py`
splits the nine binaries by a stated test** — is a third party named in the file
and the publisher not —

```
python tools/vendorhash.py rpgmaker2003-steam --publisher KADOKAWA
components : 2    carriers : 7    total files : 9
```

**Two components** — `UNLHA32.DLL` and `BaseFlushAppcompatCache.exe`, whose
whole selves are somebody else's — and **seven carriers**, Kadokawa builds
holding third-party code. The list, with sha1 and evidence offsets, is
`notes/vendorhash.txt` and is [12](12-whose-bytes.md)'s answer to a request this
collection has now made three times.

---

## What the Ultimate DLLs are for, and it settles the `.hlp`

```
python tools/peimpexp.py rpgmaker2003-steam/ultimate_eb.dll --exports
EXPORTS : 24 functions, 24 by name, 0 forwarded

CherryInitialize            Hook_ExtTextOutA          Hook_OnCreateProject
FindClassHInstanceEx        Hook_GetEventCommandString Hook_OnFreeProject
GetPicEventText             Hook_GetTempPathA         Hook_OnLoadProject
GetScriptListBGColor        Hook_WinHelpA             OnControlResize
GetSpritesheetDashBoxText   HandleShutdown            OnCustomFormDoShow
HOOK_GETEVENTCOMMANDSTRING@12                         OnCustomFormUpdateShowing
MaterialBaseGetRealFolderName  OnRenameProject        ShowInExplorer
ShowPicMagicNameHandler     ShowScriptPasteWarning
TFormCherrySpritesheet_AnimationAreaPaint
TFormEDSystem2_ButtonExpertClick
```

**Eight of the twenty-four are named `Hook_…`**, counted by command
(`grep -ciE "^   hook_"` over the export list)**.** This is a run-time patch
library: it replaces Windows API calls and editor callbacks in a program it did
not compile. `TFormCherrySpritesheet_…` and `TFormEDSystem2_…` are Delphi form
class names, which is the third independent witness for Delphi after the `.pas`
paths and the registry key.

**And `Hook_WinHelpA` answers the `.hlp`.** The editor's build path names
`RPG2003.hlp`; the object ships `rpg2003.chm` and no `.hlp`; the hook DLL
carries, within three hundred bytes of each other, the strings `hhctrl.ocx`,
`HtmlHelpA` and `\RPG Maker 2003\`, and imports `LoadLibraryA` and
`GetProcAddress` while importing nothing from `hhctrl.ocx` directly.

**A Delphi program written in 2002 to call `WinHelpA` ships in 2017 with an HTML
Help file, because a third party's DLL intercepts the call and loads
`hhctrl.ocx` at run time.** That is a whole mechanism recovered from an export
table, an import table and three strings.

The runtime DLL's ten exports say what it adds to the *game* rather than the
editor:

```
ATBHandlerMain   CustomGameWndProc   CustomStretchBlt   DataInitialized
F5Handler        GetFullscreenRect   HandleNameRepl     SetMoviePosition
StartupFullscreenDecision            CherryInitialize
```

`ultimate_eb.dll` imports **7 DLLs and 207 names** — `ADVAPI32` 10 (the
registry, and `CryptGenRandom`), `GDI32` 7 (`AddFontMemResourceEx`,
`ExtTextOutA`), `KERNEL32` 64, `msvcrt` 78, `SHELL32` 2, `USER32` 43,
`VERSION` 3. The runtime imports **8 DLLs and 183 names**: the same seven minus
`SHELL32`, plus **`ole32.dll` 3 and `WINMM.DLL` 6** — COM and multimedia, which
is what a game runtime needs and an editor patch does not.

---

## The container inside a binary

```
python tools/sigcount.py rpgmaker2003-steam --hex 4d5a5000
files BEGINNING with the signature : 4 of 737
occurrences ANYWHERE               : 5, in 4 files

python tools/peembed.py rpgmaker2003-steam/setup.exe.dat
highest raw end : 630784   file length : 630784   RESIDUE : 0
an MZ that parses as PE at file offset 483728
   it falls inside the outer image's .rsrc section
   its own section table reaches : 142848 bytes
   a resource entry begins exactly here:
      RCDATA/GAMEDELETE/9
      declared size 142848 against the inner image's reach 142848  RESIDUE 0
```

The same structure the previous session found, at a different offset, with a
different size — **142,848 against 76,800** — and a different language id:
**9 (English) where the 2000 had 0 (neutral)**. `peembed.py` produces it with no
change, so the interesting part is not that the file divides — it does not, and
that is settled — but that the uninstaller of a version which registers a file
type is 86 % larger than the one that does not.

---

## What the programs still do not say

* what any of it actually does. Nothing here disassembles a single
  instruction; every claim above is a string, a table entry or an offset;
* whether `ultimate_eb.dll`'s 24 exports are all called. An export table is what
  a DLL offers, not what a program uses;
* what `ha` is in `D:\ha\`. It is a directory name on somebody's machine;
* why `setup.exe.dat` carries the Delphi registry keys twice and
  `rpg2003.exe` once — the second copy is inside the embedded image and the two
  offsets are 466,452 apart, which is not the embedding offset of 483,728.
