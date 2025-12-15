# Password & Hash Auditor

⚠️ **EDUCATIONAL PURPOSE ONLY** - This tool is designed for authorized security testing and educational purposes. Only use on passwords/hashes you own or have explicit written authorization to test.

## Overview

A password strength analyzer and hash auditor that checks password strength and optionally performs offline hash cracking using wordlists. Designed for security audits and educational purposes.

## Features

- **Password Strength Analysis**: Checks password length, complexity, and common patterns
- **Hash Cracking**: Offline hash cracking (SHA256, SHA1, MD5)
- **Wordlist Support**: Use custom wordlists for hash cracking
- **JSON Output**: Machine-readable results
- **Educational**: Learn about password security

## Installation

### Requirements

- Python 3.8+
- Standard library only (no external dependencies!)

### Setup

```bash
# Clone the repository
git clone https://github.com/5h4d0wn1k/password-auditor.git
cd password-auditor

# No installation needed!
python password_audit.py --help
```

## Usage

### Password Strength Analysis

```bash
# Analyze passwords from file
python password_audit.py --lint passwords.txt
```

### Hash Cracking

```bash
# Crack hashes using wordlist
python password_audit.py \
  --hashes hashes.txt \
  --wordlist wordlist.txt
```

### Combined Analysis

```bash
# Analyze passwords and crack hashes
python password_audit.py \
  --lint passwords.txt \
  --hashes hashes.txt \
  --wordlist wordlist.txt \
  --json-out results.json
```

## Command-Line Options

| Option | Description |
|--------|-------------|
| `--lint` | File with plaintext passwords to analyze (one per line) |
| `--hashes` | File with hashes to crack (SHA256, SHA1, MD5) |
| `--wordlist` | Wordlist file for hash cracking |
| `--json-out` | Save results to JSON file |

## Password Strength Criteria

Passwords are checked for:

- **Minimum Length**: 12 characters
- **Uppercase Letters**: At least one A-Z
- **Lowercase Letters**: At least one a-z
- **Digits**: At least one 0-9
- **Special Characters**: At least one symbol

## Hash Algorithms Supported

- **SHA256**: Secure hash algorithm
- **SHA1**: Legacy hash algorithm
- **MD5**: Legacy hash algorithm (weak)

## Output Format

### Console Output

```json
{
  "lint": [
    {
      "password": "weakpass",
      "status": "weak",
      "findings": ["too short (<12)", "no uppercase", "no digit", "no symbol"]
    },
    {
      "password": "StrongPass123!",
      "status": "ok",
      "findings": []
    }
  ],
  "hash_audit": [
    {
      "hash": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
      "plaintext": "password"
    }
  ]
}
```

## Examples

### Example 1: Password Strength Check

```bash
# Check password strength
python password_audit.py --lint passwords.txt
```

### Example 2: Hash Cracking

```bash
# Crack hashes
python password_audit.py \
  --hashes hashes.txt \
  --wordlist rockyou.txt
```

### Example 3: Save Results

```bash
# Save results to JSON
python password_audit.py \
  --lint passwords.txt \
  --hashes hashes.txt \
  --wordlist wordlist.txt \
  --json-out audit_results.json
```

## Use Cases

- **Security Audits**: Check password policies
- **Penetration Testing**: Authorized security assessments
- **Educational Purposes**: Learn about password security

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is for authorized security testing and educational purposes only.

- Only audit passwords/hashes you own or have explicit written authorization to test
- Follow responsible disclosure practices
- Comply with all applicable laws and regulations

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always get explicit authorization before auditing any passwords or hashes!
