#!/usr/bin/env python3
"""coverage.py -- what share of an object is in a format somebody published,
stated over a named denominator.

This repository's coverage figure has always been a share of bytes whose
format has a published specification. On this object that figure is different
at every layer, so the tool takes the layer as an argument and prints the
denominator on the same line as the share. A coverage number without its
denominator is not a measurement.

    members  the twelve files the ZIP holds
    product  the files the four InstallShield containers hold, by the expanded
             size each container's own entry table declares
    tree     every file under a directory, classified BY MAGIC and not by
             extension, into FOUR buckets

THE FOURTH BUCKET, AND WHY IT HAD TO EXIST
------------------------------------------
The three buckets below were written for an object whose unopened remainder was
either vendor-specified or described by nobody at all. They do not fit an object
whose whole unopened remainder is **publicly reverse-engineered and never
specified by its vendor** -- Microsoft's ITSF, and RPG Maker's own LCF. Calling
those `published` would claim a warrant that does not exist; calling them
`neither` would deny work other people did in public and that anybody can check.
So there are four, and each has a membership test somebody who disagrees can
apply:

  SPECIFIED  a document describing the format was published by the party that
             created it, or by a standards body that adopted it, and that
             document is what an implementer works from.
  DECODED    no such document exists, and an independent published third-party
             reverse engineering does -- one this repository can name.
  DERIVED    this session worked it out of the bytes and can name no public
             account of it.
  OPAQUE     none of the above.

**The bucket describes the FORMAT's public standing, not this session's route
to it.** ITSF and LCF are DECODED here even though every field this repository
uses was derived from the bytes, because the question a bucket answers is
"could a stranger check this against something", and for those two the answer
is yes and the something is not this repository.

**And the buckets are never summed into a coverage figure.** They may be summed
into an ACCOUNTING figure -- do the bytes add up to the object -- because that
is a question about bytes. Coverage is a question about warrant, and warrants
of different kinds do not add.

A format counts as PUBLISHED when a specification exists outside this
repository: PKWARE's APPNOTE for ZIP, Microsoft's NE and PE, the MIDI
Manufacturers Association's Standard MIDI File, Microsoft's BMP and RIFF WAVE,
and plain text. It counts as DERIVED when this session worked it out of the
bytes: InstallShield's Z archive, its `_INST32I` container and its `.PKG`
manifest. It counts as NEITHER when nobody here opened it and nobody outside
has written it down: WinHelp 3.x, and RPG Maker's own `.DAT` and `.ATR`.

The three buckets are printed separately and are never merged, because
"derived by this session" is a weaker claim than "published by a vendor" and
folding them together would hide that.

    python tools/coverage.py members --members _work/members
    python tools/coverage.py product --members _work/members
    python tools/coverage.py selftest
"""
import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import is32                                      # noqa: E402
import isz                                       # noqa: E402

PUBLISHED = {
    "MID": "Standard MIDI File (MMA RP-001)",
    "BMP": "Windows bitmap (Microsoft)",
    "WAV": "RIFF WAVE (Microsoft and IBM)",
    "EXE": "NE and PE (Microsoft)",
    "DLL": "NE and PE (Microsoft)",
    "TXT": "plain text",
    "INI": "plain text",
    "DIZ": "plain text; CP437 and CP866 render it identically",
    "ID": "plain text",
}
DERIVED = {
    "1": "InstallShield Z archive, derived here",
    "LIB": "InstallShield Z archive, derived here",
    "INS": "InstallShield Z archive, derived here",
    "EX_": "InstallShield _INST32I container, derived here",
    "PKG": "InstallShield manifest, derived here",
}
NEITHER = {
    "HLP": "WinHelp 3.x, no published specification",
    "DAT": "RPG Maker's own, no published specification",
    "ATR": "RPG Maker's own, no published specification",
    "INS_product": "InstallShield compiled setup script, not opened here",
}


def ext_of(name):
    base = name.rsplit("\\", 1)[-1]
    if "." in base[1:]:
        return base.rsplit(".", 1)[-1].upper()
    return "(none)"


def bucket(ext, mode="members"):
    # `.INS` is a Z archive at the member layer and a compiled setup script
    # at the product layer. Same three letters, two different things, and
    # one table must not silently claim the other was opened.
    if ext == "INS" and mode == "product":
        return "neither", NEITHER["INS_product"]
    if ext in PUBLISHED:
        return "published", PUBLISHED[ext]
    if ext in DERIVED:
        return "derived", DERIVED[ext]
    if ext in NEITHER:
        return "neither", NEITHER[ext]
    return "neither", "not identified in this session"


def population(mode, members):
    rows = []
    if mode == "members":
        for n in sorted(os.listdir(members)):
            rows.append((n, os.path.getsize(os.path.join(members, n))))
        return rows, "the twelve files the ZIP holds"
    for name in ("_SETUP.1", "_SETUP.LIB", "SETUP.INS"):
        p = os.path.join(members, name)
        for e in isz.parse(open(p, "rb").read(), p)["entries"]:
            rows.append((e["name"], e["expanded"]))
    p = os.path.join(members, "_INST32I.EX_")
    for r in is32.parse(open(p, "rb").read())["records"]:
        rows.append((r["name"], r["expanded"]))
    return rows, "the files the four containers hold, at their declared " \
                 "expanded sizes"


def report(rows, label, mode="members"):
    total = sum(s for _, s in rows)
    cnt = collections.Counter()
    byt = collections.Counter()
    for n, s in rows:
        e = ext_of(n)
        cnt[e] += 1
        byt[e] += s
    print("denominator : %d files, %d bytes -- %s" % (len(rows), total, label))
    print()
    print("  %-8s %6s %12s  %-10s %s"
          % ("ext", "files", "bytes", "bucket", "format"))
    for e, c in cnt.most_common():
        b, why = bucket(e, mode)
        print("  %-8s %6d %12d  %-10s %s" % (e, c, byt[e], b, why))
    print()
    sums = collections.Counter()
    counts = collections.Counter()
    for e in cnt:
        b, _ = bucket(e, mode)
        sums[b] += byt[e]
        counts[b] += cnt[e]
    for b in ("published", "derived", "neither"):
        print("  %-10s %4d files %12d bytes   %8.4f %% of %d"
              % (b, counts[b], sums[b], 100.0 * sums[b] / total if total else 0,
                 total))
    print("  %-10s %4d files %12d bytes"
          % ("SUM", sum(counts.values()), sum(sums.values())))
    if sum(sums.values()) != total:
        print("  THE BUCKETS DO NOT SUM TO THE DENOMINATOR", file=sys.stderr)
        return 1
    return 0


# ------------------------------------------------------------------ by magic
#
# The `tree` mode classifies a file by its leading bytes, because this object
# ships two Windows executables named `.dat` and an extension table would put
# 1,498,112 bytes in the wrong row.

def _printable(b):
    if not b:
        return False
    return all(32 <= x < 127 or x in (9, 10, 13) for x in b[:512])


def _is(prefix):
    return lambda b: b.startswith(prefix)


def _cp932_text(b):
    """Text in a multi-byte codepage, and the test is that the codec REFUSES
    other things.

    A single-byte codepage cannot fail, so cp437 or cp866 "decoding" a file is
    no evidence at all. cp932 is a multi-byte codec with illegal sequences: a
    file of 8,899 high bytes that decodes under it with no illegal sequence,
    and whose decoded text is printable, is a Shift-JIS document, and a random
    byte stream is not. That asymmetry is the whole test and it is why this
    probe names cp932 and not the single-byte candidates.
    """
    if not b or not any(x >= 0x80 for x in b):
        return False
    try:
        s = b.decode("cp932")
    except UnicodeDecodeError as e:
        # A probe reads a fixed-size head, so the last sequence may be cut in
        # half. That is the probe's fault and not the file's: retry once
        # without the truncated tail. A failure anywhere earlier is the file's
        # and stands.
        if e.start < len(b) - 2:
            return False
        try:
            s = b[:e.start].decode("cp932")
        except UnicodeDecodeError:
            return False
    return all(c.isprintable() or c in "\t\r\n　" for c in s)


MAGICS = [
    (_is(b"MZ"), "specified", "PE / MZ executable (Microsoft)"),
    (_is(b"\x89PNG\r\n\x1a\n"), "specified", "PNG (W3C / ISO 15948)"),
    (lambda b: b.startswith(b"RIFF") and b[8:12] == b"WAVE",
     "specified", "RIFF WAVE (Microsoft and IBM)"),
    (_is(b"MThd"), "specified", "Standard MIDI File (MMA RP-001)"),
    (_is(b"\x00\x00\x01\x00"), "specified", "Windows icon"),
    (_is(b"ITSF"), "decoded",
     "Microsoft ITSF -- no vendor specification; chmlib and 7-Zip"),
    (lambda b: b[:1] == b"\x0b" and b[1:12] == b"LcfDataBase",
     "decoded", "LCF database -- no vendor specification; the EasyRPG project"),
    # Three magics added on pc-rpgmaker2003-doc, where their absence put
    # 67,623 bytes in the OPAQUE bucket and the tool still closed at residue 0
    # and printed a full table. A classifier that is silently wrong is worse
    # than one that refuses, so these are here with the same length-prefixed
    # shape as LcfDataBase above and not a substring search.
    (lambda b: b[:1] == b"\x0a" and b[1:11] == b"LcfMapUnit",
     "decoded", "LCF map unit -- no vendor specification; the EasyRPG project"),
    (lambda b: b[:1] == b"\x0a" and b[1:11] == b"LcfMapTree",
     "decoded", "LCF map tree -- no vendor specification; the EasyRPG project"),
    (_is(b"8BPS"), "specified", "Adobe Photoshop PSD (Adobe, published)"),
    (_printable, "specified", "plain text, ASCII"),
    (_cp932_text, "specified",
     "plain text, Shift-JIS (JIS X 0208; Microsoft cp932)"),
]


def classify(blob):
    for probe, buck, name in MAGICS:
        try:
            if probe(blob):
                return buck, name
        except (IndexError, TypeError):
            continue
    return "opaque", "not identified by any signature this tool knows"


def tree_rows(root):
    rows = []
    for dp, dn, fn in os.walk(root):
        for f in sorted(fn):
            p = os.path.join(dp, f)
            with open(p, "rb") as fh:
                head = fh.read(512)
            buck, name = classify(head)
            rows.append((os.path.relpath(p, root).replace(os.sep, "/"),
                         os.path.getsize(p), buck, name))
    if not rows:
        sys.exit("coverage: no files under %r -- refusing to report a clean "
                 "table over an empty population" % root)
    return rows


def report_tree(root):
    rows = tree_rows(root)
    total = sum(r[1] for r in rows)
    cnt = collections.Counter()
    byt = collections.Counter()
    for _, size, buck, name in rows:
        cnt[(buck, name)] += 1
        byt[(buck, name)] += size
    print("denominator : %d files, %d bytes -- every file under %s, "
          "classified BY MAGIC" % (len(rows), total, root))
    print()
    print("  %-10s %6s %12s %10s  %s"
          % ("bucket", "files", "bytes", "share", "format"))
    order = {"specified": 0, "decoded": 1, "derived": 2, "opaque": 3}
    for (buck, name), c in sorted(cnt.items(),
                                  key=lambda kv: (order[kv[0][0]],
                                                  -byt[kv[0]])):
        print("  %-10s %6d %12d %9.4f %%  %s"
              % (buck, c, byt[(buck, name)],
                 100.0 * byt[(buck, name)] / total, name))
    print()
    sums = collections.Counter()
    counts = collections.Counter()
    for (buck, name), c in cnt.items():
        sums[buck] += byt[(buck, name)]
        counts[buck] += c
    for b in ("specified", "decoded", "derived", "opaque"):
        print("  %-10s %4d files %12d bytes   %8.4f %% of %d"
              % (b, counts[b], sums[b], 100.0 * sums[b] / total if total else 0,
                 total))
    print("  %-10s %4d files %12d bytes   %8.4f %%"
          % ("SUM", sum(counts.values()), sum(sums.values()),
             100.0 * sum(sums.values()) / total))
    print("  against the denominator %d          RESIDUE %d"
          % (total, sum(sums.values()) - total))
    print()
    print("  The SUM row is an ACCOUNTING figure and not a coverage figure.")
    print("  It answers 'do the bytes add up to the object'. It does not")
    print("  answer 'how much of this can be checked against something outside")
    print("  it', because SPECIFIED and DECODED carry warrants of different")
    print("  strength and DERIVED carries none but this session's.")
    if sum(sums.values()) != total:
        print("  THE BUCKETS DO NOT SUM TO THE DENOMINATOR", file=sys.stderr)
        return 1
    return 0


def selftest():
    checks = []
    checks.append(("every extension falls in exactly one bucket",
                   len(set(PUBLISHED) & set(DERIVED)) == 0
                   and len(set(PUBLISHED) & set(NEITHER)) == 0
                   and len(set(DERIVED) & set(NEITHER)) == 0, ""))
    checks.append(("an unknown extension is not counted as published",
                   bucket("QQQ")[0] == "neither", str(bucket("QQQ"))))
    checks.append(("INS is derived at the member layer and neither at the "
                   "product layer",
                   bucket("INS")[0] == "derived"
                   and bucket("INS", "product")[0] == "neither", ""))
    checks.append(("a name with a path separator takes the last component",
                   ext_of("themes\\global\\a.BMP") == "BMP", ""))
    checks.append(("a dotfile is not given an extension",
                   ext_of(".profile") == "(none)", ext_of(".profile")))
    checks.append(("a name with no dot is not given an extension",
                   ext_of("README") == "(none)", ""))
    checks.append(("HLP is NOT counted as published",
                   bucket("HLP")[0] == "neither", ""))
    checks.append(("the Z archive is derived and not published",
                   bucket("1")[0] == "derived", ""))
    # The four-bucket classifier, which is new and is the point of `tree`.
    checks.append(("a PE is SPECIFIED",
                   classify(b"MZ\x90\x00" + bytes(60))[0] == "specified", ""))
    checks.append(("an MZP stub is SPECIFIED too, because MZ is the signature",
                   classify(b"MZP\x00" + bytes(60))[0] == "specified", ""))
    checks.append(("a PNG is SPECIFIED",
                   classify(b"\x89PNG\r\n\x1a\n" + bytes(20))[0]
                   == "specified", ""))
    checks.append(("a RIFF that is not WAVE is not counted as WAVE",
                   classify(b"RIFF\x00\x00\x00\x00AVI ")[1]
                   != "RIFF WAVE (Microsoft and IBM)", ""))
    checks.append(("a RIFF WAVE is SPECIFIED",
                   classify(b"RIFF\x00\x00\x00\x00WAVEfmt ")[0]
                   == "specified", ""))
    checks.append(("an ITSF container is DECODED, not specified",
                   classify(b"ITSF\x03\x00\x00\x00" + bytes(40))[0]
                   == "decoded", ""))
    checks.append(("an LCF database is DECODED, not specified",
                   classify(b"\x0bLcfDataBase\x0b\xae\x11")[0]
                   == "decoded", ""))
    checks.append(("a file merely CONTAINING LcfDataBase is not one",
                   classify(b"xxxx\x0bLcfDataBase")[0] != "decoded", ""))
    checks.append(("an LcfMapUnit is DECODED",
                   classify(b"\x0aLcfMapUnit\x01\x01\x04")[0]
                   == "decoded", ""))
    checks.append(("an LcfMapTree is DECODED",
                   classify(b"\x0aLcfMapTree\x04\x00\x01")[0]
                   == "decoded", ""))
    checks.append(("the two map variants are told apart",
                   classify(b"\x0aLcfMapUnit\x01")[1]
                   != classify(b"\x0aLcfMapTree\x04")[1], ""))
    checks.append(("a wrong length prefix on LcfMapUnit is not one",
                   classify(b"\x0bLcfMapUnit\x01")[0] != "decoded", ""))
    checks.append(("a PSD is SPECIFIED, because Adobe published the format",
                   classify(b"8BPS\x00\x01" + bytes(20))[0]
                   == "specified", ""))
    checks.append(("a PSD is named as Adobe's",
                   "Adobe" in classify(b"8BPS\x00\x01" + bytes(20))[1], ""))
    checks.append(("plain text is SPECIFIED",
                   classify(b"383730\n")[0] == "specified", ""))
    checks.append(("Shift-JIS text is SPECIFIED, not opaque",
                   classify("Ｍｉｃｃｏ (Feb.3,2003)".encode("cp932"))[0]
                   == "specified", ""))
    checks.append(("and it is named as Shift-JIS rather than as ASCII",
                   "Shift-JIS" in
                   classify("Ｍｉｃｃｏ".encode("cp932"))[1], ""))
    checks.append(("a byte string cp932 REFUSES is not called text",
                   _cp932_text(bytes([0x81, 0x20, 0xFF, 0x81])) is False, ""))
    checks.append(("a head cut mid-sequence is still recognised as text",
                   _cp932_text("Ｍｉｃｃｏ".encode("cp932")[:-1]) is True, ""))
    checks.append(("but a bad sequence in the MIDDLE is not forgiven",
                   _cp932_text("Ｍ".encode("cp932") + b"\xff\xfe"
                               + "ｏｏｏ".encode("cp932")) is False, ""))
    checks.append(("pure ASCII does not reach the Shift-JIS probe",
                   _cp932_text(b"hello") is False, ""))
    checks.append(("a random binary is OPAQUE",
                   classify(bytes([7, 200, 3, 99, 250]))[0] == "opaque", ""))
    checks.append(("an empty file is OPAQUE and does not crash",
                   classify(b"")[0] == "opaque", ""))
    checks.append(("the classifier emits only bucket names the report knows",
                   {m[1] for m in MAGICS} | {"opaque"}
                   <= {"specified", "decoded", "derived", "opaque"}, ""))
    width = max(len(c[0]) for c in checks)
    failed = 0
    for label, ok, note in checks:
        print("  %-*s  %s   %s" % (width, label, "ok  " if ok else "FAIL",
                                   note))
        if not ok:
            failed += 1
    print()
    print("%d checks, %d failures" % (len(checks), failed))
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("mode", choices=("members", "product", "tree", "selftest"))
    ap.add_argument("--members", default="_work/members")
    ap.add_argument("--root")
    args = ap.parse_args()
    if args.mode == "selftest":
        return selftest()
    if args.mode == "tree":
        if not args.root:
            sys.exit("coverage: tree mode needs --root")
        return report_tree(args.root)
    rows, label = population(args.mode, args.members)
    return report(rows, label, args.mode)


if __name__ == "__main__":
    sys.exit(main())
