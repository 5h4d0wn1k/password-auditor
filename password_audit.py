"""
Password strength & hash audit (lab/owned data only).

- Lints passwords for length/charset diversity.
- Optional offline hash audit using a small provided wordlist (supports sha256/sha1/md5).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from typing import Dict, List, Tuple


def lint_password(pwd: str) -> Dict[str, str]:
    findings = []
    if len(pwd) < 12:
        findings.append("too short (<12)")
    if not re.search(r"[A-Z]", pwd):
        findings.append("no uppercase")
    if not re.search(r"[a-z]", pwd):
        findings.append("no lowercase")
    if not re.search(r"[0-9]", pwd):
        findings.append("no digit")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        findings.append("no symbol")
    return {"password": pwd, "status": "weak" if findings else "ok", "findings": findings}


def load_passwords(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]


def load_hashes(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip().lower() for line in f if line.strip()]


def crack_hashes(hashes: List[str], wordlist: List[str]) -> List[Tuple[str, str]]:
    hits: List[Tuple[str, str]] = []
    for word in wordlist:
        for algo in ("sha256", "sha1", "md5"):
            h = getattr(hashlib, algo)(word.encode()).hexdigest()
            if h in hashes:
                hits.append((h, word))
    return hits


def main() -> None:
    parser = argparse.ArgumentParser(description="Password and hash audit (lab/owned data only).")
    parser.add_argument("--lint", help="File with plaintext passwords to lint (one per line).")
    parser.add_argument("--hashes", help="File with hashes (sha256/sha1/md5) to audit.")
    parser.add_argument("--wordlist", help="Wordlist for hash audit (small, lab-only).")
    parser.add_argument("--json-out", help="Write JSON results to file.")
    args = parser.parse_args()

    print("⚠️  Authorized use only. Audit only data you own/control.")
    results: Dict[str, object] = {}

    if args.lint:
        pwds = load_passwords(args.lint)
        results["lint"] = [lint_password(p) for p in pwds]

    if args.hashes and args.wordlist:
        hashes = load_hashes(args.hashes)
        words = load_passwords(args.wordlist)
        hits = crack_hashes(hashes, words)
        results["hash_audit"] = [{"hash": h, "plaintext": w} for h, w in hits]

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
    else:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
