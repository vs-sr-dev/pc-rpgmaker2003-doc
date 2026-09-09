# 03 — the shop: a manifest that closes twice, a signed install script that registers an extension the object does not use, and a download figure that turns out to be the deduplicated one

*Measure: `python tools/steamacf.py --path <steamapps>/appmanifest_362870.acf
--root rpgmaker2003-steam --check`, in `notes/steamacf.txt`; the full key dump
in `notes/steamacf-dump.txt`; `python tools/compratio.py rpgmaker2003-steam
--declared 22100528 --by-ext`, in `notes/compratio.txt`; the deduplicated
arithmetic in `notes/compratio-dedup.txt`.*

---

## The manifest, and the discrepancy the previous object left open

```
"appid"        "362870"          "name"        "RPG Maker 2003"
"installdir"   "RPG Maker 2003"  "StateFlags"  "4"
"LastUpdated"  "1788949101"      "LastPlayed"  "0"
"SizeOnDisk"   "33578445"        "buildid"     "2173406"
"BytesToDownload" "22100528"     "BytesToStage" "33578445"
"InstalledDepots" { "362871" { "manifest" "837722761356681434"
                               "size" "33578445" } }
"InstallScripts" { "362871" "2k3_install.vdf" }
"UserConfig"   { "language" "english" }
```

Twenty-seven keys printed, one redacted: `LastOwner`, a SteamID64, removed by
the program. `LauncherPath` names a directory on this machine and is not
reproduced.

**`pc-rpgmaker2000-doc/docs/14` recorded a disagreement and could not settle
it**: that object shipped `2k_install.vdf` and its own manifest did not
reference it. This one ships `2k3_install.vdf` and its manifest **does**. With
two specimens the reading is that the 2003 is normal and the 2000's manifest is
missing a block — which is a reading about two files and not a proof about
Steam, and a third specimen would settle it. The owner has RPG Maker XP.

**`LastUpdated` is 1788949101 against the previous object's 1788949103.** Two
seconds. Steam wrote both trees inside one minute, which is why every mtime in
both objects is 2026 ([11](11-the-clocks.md)).

---

## The install script does four things and one of them is new

`2k3_install.vdf` is **1,545 bytes** against the previous object's 753. Read in
full it does four things, and the third and fourth are what grew.

**One — the publisher's key, in the same shape as the 2000's:**

```
HKEY_CURRENT_USER\Software\KADOKAWA\rpg2003
    ApplicationPath      %INSTALLDIR%
    RuntimePackagePath   %INSTALLDIR%\RTP
```

**Two — the DEP shim, unchanged, in both hives**, writing `DisableNXShowUI`
against `rpg2003.exe` under `AppCompatFlags\Layers` and then running
`BaseFlushAppcompatCache.exe` under a `Run Process` block keyed
`…\Valve\Steam\Apps\RM2k3 Flush DEP again`. The helper is **byte-identical to
the previous object's** — sha1 `9ba229d3…`, 47,790 bytes — and it is one of the
368 crossings ([06](06-the-crossings.md)). **That is a difference of zero,
measured**: the same shim, the same bytes, a different product.

**Three — a registered file type, which the 2000 had none of:**

```
HKEY_CLASSES_ROOT\RPG2003.Project              "RPG Maker 2003 Project File"
HKEY_CLASSES_ROOT\RPG2003.Project\DefaultIcon  "%INSTALLDIR%\rpg2003.exe",0
HKEY_CLASSES_ROOT\RPG2003.Project\shell\open\command
                                               "%INSTALLDIR%\rpg2003.exe" "%1"
HKEY_CLASSES_ROOT\.r3project                   "RPG2003.Project"
```

**And the extension it registers is not the extension the object ships.**

```
grep -aob "r3proj\|r3project" rpgmaker2003-steam/2k3_install.vdf
617:r3project

xxd rpgmaker2003-steam/Sample/ArcheiaPictureTutorial/Picture_Tutorial.r3proj
00000000: 5250 4732 3030 3320 7631 2e31 3261 0d0a  RPG2003 v1.12a..
```

`.r3project` appears once in the script, at byte offset **617**, and nowhere
else in 737 files. `.r3proj` is the extension of the only project file in the
object, sixteen bytes long. **The installer teaches Windows to open one
extension and the product ships the other**, and a sweep of all 737 files says
which binary believes which:

```
grep -rlab "r3project" rpgmaker2003-steam/   ->  2k3_install.vdf
grep -rlab "r3proj"    rpgmaker2003-steam/   ->  2k3_install.vdf
                                                 ultimate_eb.dll
```

Inside `ultimate_eb.dll`, at offsets **149,405** and **149,417**, are the
strings `\*.r3proj` and `.r3proj` — **a file mask and an extension**. `rpg2003.exe`,
4,387,328 bytes, contains neither string.

**So the extension the product actually uses is named by a third party's hook
library and not by the publisher's editor**, which is what
[08](08-the-programs.md) shows that library is for. The installer registers a
string that nothing in the object reads. This does not establish that the editor
would refuse a file named `.r3project` — that would need the editor running, and
rule 4 forbids it — but it does establish that the mask presented to a user
comes from `ultimate_eb.dll` and says `r3proj`.

**Four — a signature block the previous object's script did not have:**

```
"kvsignatures" { "InstallScript" "21707de5…f0ddb0f02f330" }
```

**256 hexadecimal digits, which is 128 bytes** — the size of an RSA-1024
signature. Valve signs install scripts. The 2000's script carried no such block
*and* was not referenced by its own manifest; two absences pointing the same
way is a weak argument and it is offered as one.

---

## The download figure, checked, and it is the deduplicated total

The manifest states 22,100,528 downloaded against 33,578,445 staged, a ratio of
**1.5194** against the previous object's 1.3355. `pc-rpgmaker2000-doc/docs/03`
checked that ratio against a per-file compression total and closed to within
**0.16 %**. The same arithmetic here does not.

```
python tools/compratio.py rpgmaker2003-steam --declared 22100528 --by-ext

bytes on disk    : 33578445
LZMA, per file   : 22422597
declared         : 22100528
difference       : +322069 bytes = +1.4573 % of the declared
```

**1.4573 % is nine times the previous object's gap, and the reason is in
[01](01-the-object.md): this object ships six files twice.** Paying for each
distinct hash once instead of once per file:

```
distinct sha1                      : 731
per-file LZMA total                : 22,422,597    +322,069 = +1.4573 %
LZMA counting each hash once       : 21,968,501    −132,027 = −0.5974 %
saved by not paying twice          :    454,096
```

**The declared figure sits between the two and much nearer the deduplicated
one.** 454,096 compressed bytes of duplication, of which 398,135 is one 1 MB
executable shipped as both `rpg_rt.exe.dat` and `Sample\…\RPG_RT.exe`, and
48,425 is the runtime DLL shipped twice.

That is as far as this measurement goes and the limit is stated: Steam chunks,
deduplicates across a whole depot and can send a delta against what a client
already holds, so a per-file LZMA total is an upper bound on a smart packer and
a lower bound on nothing. **What the two figures do establish is that the
remaining 0.60 % is chunk framing and packer choice, not a missing 322 KB.**

By format, and the row that matters is the first:

| ext | files | on disk | LZMA | ratio |
|---|---:|---:|---:|---:|
| `.wav` | 216 | 10,426,824 | 8,491,936 | 1.2279 |
| `.chm` | 1 | 6,268,124 | 6,251,785 | **1.0026** |
| `.exe` | 3 | 5,467,822 | 1,330,631 | 4.1092 |
| `.png` | 355 | 5,174,453 | 4,848,936 | 1.0671 |
| `.mid` | 141 | 2,945,749 | 378,319 | **7.7864** |
| `.dat` | 4 | 2,176,990 | 742,107 | 2.9335 |
| `.ldb` | 1 | 374,229 | 61,214 | 6.1135 |
| `.psd` | 1 | 54,653 | 13,714 | 3.9852 |
| `.lmu` | 3 | 12,635 | 3,817 | 3.3102 |
| `.url` | 2 | 104 | 112 | **0.9286** |
| `.r3proj` | 1 | 16 | 20 | **0.8000** |

**The `.chm` at 1.0026 is a container that is already compressed inside itself**
— LZX, 6,244,974 compressed against 8,623,119 uncompressed, stated three ways by
its own reset table ([07](07-what-does-not-cross.md)). **The two rows below 1
are files smaller than an LZMA header**, which is the honest floor of this
method and is left in the table rather than hidden.

---

## What the shop cannot say

* **when the product was made.** `LastUpdated` is when Steam wrote this
  machine's copy. The build id is Valve's counter. Neither is an authoring date,
  and the authoring dates that do exist are in [11](11-the-clocks.md);
* **whether the tree is intact.** The residue-0 closure is a weight, not a
  checksum. The 731 hashes are the checksum, and they are published in
  `notes/sha1-all.txt`;
* **why the script registers `.r3project`.** Both strings are in the object; the
  reason one of them is unused is not.
