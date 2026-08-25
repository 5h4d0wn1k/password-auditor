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

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⚠️ Legal Disclaimer

### Educational Purpose Only
This tool is provided strictly for **educational purposes** and **authorized security testing** only. It is intended to help security professionals and students learn about security concepts in controlled environments.

### Authorized Use Only
- You must have **explicit written authorization** before testing any system you do not own
- Unauthorized access to computer systems is **illegal** and punishable under laws including but not limited to the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and similar legislation worldwide
- Only use this tool on systems you own, have permission to test, or in isolated lab environments

### No Warranty
This software is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The author makes no representations or warranties regarding the accuracy, completeness, or reliability of this software.

### Limitation of Liability
**In no event shall the author (Nikhil Nagpure) be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.**

### User Responsibility
- The user assumes **full responsibility** for any consequences resulting from the use of this tool
- The author is **not responsible** for any misuse, damage, or illegal activities performed with this software
- Users are solely responsible for ensuring compliance with all applicable local, state, national, and international laws and regulations

### Indemnification
By using this software, you agree to **indemnify, defend, and hold harmless** the author from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys fees) arising from or related to your use of this software.

### Responsible Disclosure
If you discover vulnerabilities using this tool, please follow responsible disclosure practices and report them to the affected parties through appropriate channels.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by this disclaimer.**
## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always get explicit authorization before auditing any passwords or hashes!
