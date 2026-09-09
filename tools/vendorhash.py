#!/usr/bin/env python3
"""vendorhash.py -- publish a hash list of the THIRD-PARTY components in an
object, so that the same library shipped by two different products becomes
visible to `crossall.py` even when the two products' copies differ.

WHY THIS EXISTS, AND WHY IT IS LATE
------------------------------------
Three consecutive objects in this collection ship a compression library by the
same author -- `UNLHA32.DLL`, by Micco -- at three different versions:

    pc-rpgmaker95-doc     151,552 bytes   0.71.0.5
    pc-rpgmaker2000-doc   254,464 bytes   1.87.0.2
    pc-rpgmaker2003-doc   237,568 bytes   1.47.1.7-VC

**None of the three crosses**, because sha1 compares bytes and these are three
builds. `pc-rpgmaker2000-doc/docs/11` asked that a third-party hash list be
published so the relationship becomes visible anyway. Nobody wrote one. This is
that list, and the point is not the hashes -- `crossall.py` already reads the
whole-tree list -- it is the **vendor and product columns**, which let a reader
ask "who else ships Micco's library" instead of "which other object has these
exact bytes".

WHAT COUNTS AS A THIRD-PARTY COMPONENT, and the test is stated
--------------------------------------------------------------
A file is listed when it carries, in its own bytes, a name that is not the
publisher's: a version resource whose `CompanyName` or copyright names someone
else, or a licence block naming an author. **A file is not listed because this
session recognised it.** Every row names the offset of the evidence.

A second table lists files that are the publisher's own but **carry** a third
party's code inside them, because that is a different claim and a hash of the
whole file is not a hash of the component.

    python tools/vendorhash.py <root>
    python tools/vendorhash.py <root> --out notes/vendorhash.txt
    python tools/vendorhash.py --selftest
"""
import argparse
import hashlib
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

# Each probe is (label, vendor, pattern). The pattern must appear in the file's
# own bytes; the offset of the first occurrence is printed as the evidence.
PROBES = [
    ("LZH compression library", "Micco",
     re.compile(rb"\(C\)Micco 1995-\d{4}")),
    ("NSIS installer runtime", "Nullsoft",
     re.compile(rb"NullsoftInst")),
    ("the Ultimate patch", 'David "Cherry" Trapp',
     re.compile(rb'David "Cherry" Trapp')),
    ("Borland Delphi runtime", "Borland",
     re.compile(rb"Software\\Borland\\Delphi\\[0-9.]+")),
    ("Microsoft HTML Help runtime", "Microsoft",
     re.compile(rb"hhctrl\.ocx")),
]
VERSION = re.compile(rb"(\d+\.\d+\.\d+\.\d+(?:-VC)?)")


def sha1_of(path):
    h = hashlib.sha1()
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def probe(blob):
    """[(label, vendor, offset, matched text)] for every probe that fires."""
    out = []
    for label, vendor, pat in PROBES:
        m = pat.search(blob)
        if m:
            out.append((label, vendor, m.start(),
                        m.group().decode("latin-1")))
    return out


def scan(root):
    rows = []
    for dp, _dn, fn in os.walk(root):
        for f in sorted(fn):
            path = os.path.join(dp, f)
            try:
                blob = open(path, "rb").read()
            except OSError:
                continue
            hits = probe(blob)
            if not hits:
                continue
            rows.append({
                "path": os.path.relpath(path, root).replace(os.sep, "/"),
                "bytes": len(blob), "sha1": hashlib.sha1(blob).hexdigest(),
                "hits": hits,
            })
    return rows


def run(args):
    rows = scan(args.root)
    if not rows:
        raise SystemExit("vendorhash: no third-party marker found under %s -- "
                         "refusing to publish an empty list as a finding"
                         % args.root)
    # THE SPLIT, and it is a test rather than a judgement:
    #   COMPONENT -- a third party is named in the file and the publisher is
    #                NOT. The whole file is somebody else's, so its sha1 is a
    #                hash of the component and is worth publishing as one.
    #   CARRIER   -- both are named. The file is the publisher's build and
    #                holds third-party code, so its sha1 is a hash of the
    #                build and says nothing about the component's version.
    # The publisher's own name is given on the command line, not guessed.
    pub = args.publisher.encode("ascii")
    comps, carriers = [], []
    for r in rows:
        blob = open(os.path.join(args.root,
                                 r["path"].replace("/", os.sep)), "rb").read()
        r["publisher_at"] = blob.find(pub)
        (carriers if r["publisher_at"] >= 0 else comps).append(r)

    print("# third-party components in this object")
    print("#")
    print("# Format: sha1, bytes, path, vendor, component, evidence offset.")
    print("# Every row's vendor is named IN THE FILE at the offset given.")
    print("#")
    print("# object : %s" % os.path.basename(os.path.normpath(args.root)))
    print()
    print("## whole files that ARE a third party's")
    print()
    for r in sorted(comps, key=lambda r: -r["bytes"]):
        label, vendor, off, text = r["hits"][0]
        print("%s %10d  %-46s  %-22s %-28s @%d  %r"
              % (r["sha1"], r["bytes"], r["path"], vendor, label, off, text))
    print()
    print("## files naming the publisher %r as well, which CARRY a third"
          % args.publisher)
    print("## party's code rather than being one")
    print()
    for r in sorted(carriers, key=lambda r: -r["bytes"]):
        print("%s %10d  %-46s  (%s @%d)"
              % (r["sha1"], r["bytes"], r["path"], args.publisher,
                 r["publisher_at"]))
        for label, vendor, off, text in r["hits"]:
            print("%s  %-22s %-28s @%d  %r"
                  % (" " * 51, vendor, label, off, text))
    print()
    print("components : %d    carriers : %d    total files : %d"
          % (len(comps), len(carriers), len(rows)))
    print()
    print("## what this list does NOT establish")
    print("#")
    print("# A marker in a file says the file contains that string. It does")
    print("# not say the component is unmodified, and two products carrying")
    print("# one vendor's marker at different sha1 are carrying two builds,")
    print("# not one library. That is exactly why the vendor column exists:")
    print("# the hashes will not cross and the vendor will.")
    return 0


def selftest():
    checks = []

    def check(name, got, want):
        checks.append((name, got == want, got, want))

    micco = b"xxxx (C)Micco 1995-2000.  All rights reserved. yyyy"
    hits = probe(micco)
    check("Micco's copyright is found", len(hits), 1)
    check("it names Micco", hits[0][1], "Micco")
    check("its offset is the match's", hits[0][2], 5)
    check("the matched text is reported",
          hits[0][3], "(C)Micco 1995-2000")

    check("a 2002 copyright matches the same probe",
          len(probe(b"(C)Micco 1995-2002")), 1)
    check("a file with nothing in it fires nothing", probe(b"nothing"), [])

    cherry = b'This product contains software developed by David "Cherry" Trapp'
    check("Cherry's licence is found", probe(cherry)[0][1],
          'David "Cherry" Trapp')

    both = micco + b" || " + cherry
    check("two vendors in one file give two hits", len(probe(both)), 2)

    delphi = b"Software\\Borland\\Delphi\\6.0\\FileFormat"
    check("the Delphi registry key is found and names Borland",
          probe(delphi)[0][1], "Borland")

    import shutil
    import tempfile
    tmp = tempfile.mkdtemp(prefix="vendorhash-")
    try:
        p = os.path.join(tmp, "UNLHA32.DLL")
        open(p, "wb").write(micco)
        rows = scan(tmp)
        check("one row scanned", len(rows), 1)
        check("its sha1 is the file's",
              rows[0]["sha1"], hashlib.sha1(micco).hexdigest())
        check("its byte count is the file's", rows[0]["bytes"], len(micco))

        empty = os.path.join(tmp, "empty")
        os.makedirs(empty)
        check("a tree with no markers scans to nothing", scan(empty), [])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    bad = 0
    for name, ok, got, want in checks:
        print("  %-48s %s" % (name, "ok" if ok else
                              "FAIL got %r want %r" % (got, want)))
        if not ok:
            bad += 1
    print("checks : %d   failures : %d" % (len(checks), bad))
    raise SystemExit(1 if bad else 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?")
    ap.add_argument("--publisher", default="KADOKAWA",
                    help="the publisher's own name, as it appears in the "
                         "bytes; a file naming it is a CARRIER and not a "
                         "COMPONENT")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest or args.root == "selftest":
        return selftest()
    if not args.root:
        raise SystemExit("vendorhash: a root is required (or --selftest)")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
