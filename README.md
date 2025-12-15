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
  --json-out audit_results.json
```

## Command-Line Options

| Option | Description |
|--------|-------------|
| `--lint` | File with plaintext passwords to analyze (one per line) |
| `--hashes` | File with hashes to crack (SHA256/SHA1/MD5) |
| `--wordlist` | Wordlist file for hash cracking |
| `--json-out` | Save results to JSON file |

## Password Strength Criteria

Passwords are checked for:

- **Length**: Minimum 12 characters
- **Uppercase**: Contains uppercase letters
- **Lowercase**: Contains lowercase letters
- **Digits**: Contains numbers
- **Symbols**: Contains special characters

## Supported Hash Algorithms

- **SHA256**: Secure Hash Algorithm 256-bit
- **SHA1**: Secure Hash Algorithm 1 (deprecated)
- **MD5**: Message Digest 5 (deprecated)

## File Formats

### Passwords File (`passwords.txt`)

```
password123
MySecurePass123!
weakpass
```

### Hashes File (`hashes.txt`)

```
5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
356a192b7913b04c54574d18c28d46e6395428ab
5f4dcc3b5aa765d61d8327deb882cf99
```

### Wordlist File (`wordlist.txt`)

```
password
123456
admin
letmein
password123
```

## Output Format

### Password Analysis

```json
{
  "lint": [
    {
      "password": "password123",
      "status": "weak",
      "findings": [
        "too short (<12)",
        "no uppercase",
        "no symbol"
      ]
    },
    {
      "password": "MySecurePass123!",
      "status": "ok",
      "findings": []
    }
  ]
}
```

### Hash Cracking Results

```json
{
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
python password_audit.py \
  --lint user_passwords.txt \
  --json-out password_analysis.json
```

### Example 2: Hash Cracking

```bash
# Crack hashes
python password_audit.py \
  --hashes leaked_hashes.txt \
  --wordlist rockyou.txt \
  --json-out cracked_hashes.json
```

### Example 3: Complete Audit

```bash
# Full password audit
python password_audit.py \
  --lint passwords.txt \
  --hashes hashes.txt \
  --wordlist wordlist.txt \
  --json-out complete_audit.json
```

## Password Security Best Practices

1. **Length**: Use at least 12 characters (preferably 16+)
2. **Complexity**: Include uppercase, lowercase, numbers, and symbols
3. **Uniqueness**: Don't reuse passwords across accounts
4. **Avoid Common Patterns**: Don't use dictionary words or common patterns
5. **Password Managers**: Use password managers for secure storage

## Use Cases

- **Security Audits**: Analyze password policies
- **Penetration Testing**: Authorized security assessments
- **Educational Purposes**: Learn about password security
- **Compliance**: Check password compliance requirements

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is for authorized security testing and educational purposes only.

- Only analyze passwords/hashes you own or have explicit written authorization to test
- Never use on passwords/hashes you don't own
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

**Remember**: Only use on passwords/hashes you own or have explicit authorization to test!
