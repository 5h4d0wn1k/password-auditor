> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.

# Password Auditor

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub Stars](https://img.shields.io/github/stars/5h4d0wn1k/password-auditor)
![Last Commit](https://img.shields.io/github/last-commit/5h4d0wn1k/password-auditor)
![GitHub Issues](https://img.shields.io/github/issues/5h4d0wn1k/password-auditor)

> **Password strength analyzer and hash auditor** — a CLI that lints plaintext
> passwords against policy and runs offline wordlist attacks on SHA-256, SHA-1
> and MD5 hashes, for authorized security testing and security education.

## Why

Weak and reused passwords remain the leading entry point for account takeover.
This auditor closes the loop for defenders and educators: `--lint` scores
own-lab password lists against a 12-character, all-charset policy, while
`--hashes` + `--wordlist` demonstrates how fast unsalted legacy hashes
(SHA-1/MD5) fall to a wordlist offline. Everything stays on files you own —
passwords and hashes never leave the machine, and no network is touched. Use it
to prove why password managers, MFA, and modern KDF hashing matter.

## Features

- **Policy linting** — flags passwords shorter than 12 chars or missing
  uppercase, lowercase, digit, or symbol classes; returns `ok`/`weak` per entry.
- **Offline hash auditing** — tests wordlist candidates against SHA-256, SHA-1
  and MD5 hashes with no network access.
- **Wordlist support** — bring your own list; one password or hash per line.
- **JSON export** — `--json-out` writes machine-readable findings for reports.

## Quickstart

```bash
# Python 3.8+; stdlib only, nothing to install
python password_audit.py --help

# Lint a password list (one password per line)
python password_audit.py --lint passwords.txt

# Audit hashes with a wordlist (sha256/sha1/md5)
python password_audit.py --hashes hashes.txt --wordlist wordlist.txt

# Combined run with JSON results
python password_audit.py \
  --lint passwords.txt \
  --hashes hashes.txt \
  --wordlist wordlist.txt \
  --json-out audit_results.json
```

## Command-line options

| Option | Description |
|---|---|
| `--lint FILE` | plaintext password file (one per line) to policy-lint |
| `--hashes FILE` | hash file (sha256/sha1/md5, one per line) to audit |
| `--wordlist FILE` | candidate wordlist for the offline hash audit |
| `--json-out FILE` | write JSON results instead of printing to stdout |

## Project structure

```
password_audit.py   # CLI + lint/hash-audit engine (stdlib)
requirements.txt    # no external deps; stdlib only
ETHICS.md           # ethics/authorized-use policy (read first)
SCOPE.md            # defined assessment scope
```

## Documentation

- [ETHICS.md](ETHICS.md) — ethical-use policy, read first
- [SCOPE.md](SCOPE.md) — authorized-scope definition
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to contribute
- [SECURITY.md](SECURITY.md) — vulnerability reporting
- [CHANGELOG.md](CHANGELOG.md) — version history

## Contributing

Improvements to policy rules, additional hash algorithms, and audit reporting
are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md); keep it offline-first and
authorized-only.

## License

MIT — see [LICENSE](LICENSE).