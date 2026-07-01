#  LOCK-0 v1.0.0 - Encryption Suite

> **Advanced File Encryption Tool** 

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/BassemMohamed44/Lock-0/blob/main/LICENSE)
[![Security](https://img.shields.io/badge/Security-AES--256--GCM-red.svg)](https://github.com/BassemMohamed44/Lock-0/blob/main/SECURITY.md)

---

##  Table of Contents 

- [Program Introduction](#program-introduction)
- [Security features](#security-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to use](#how-to-use)
- [Technical specifications](#technical-specifications)
- [Practical examples](#practical-examples)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contribution](#contribution)
- [Licensing](#licensing)

---

##  Program Introduction

**LOCK-0** It is an advanced and secure encryption tool developed using the latest global encryption standards. 

### What makes a  LOCK-0 special?

 **Very strong encryption** - AES-256-GCM
 **Full protection** - Automatically encrypt/decrypt multiple files 
 **Secure Delete** - Permanent deletion of original files with no possibility of recovery
 **Easy interface** - Beautiful and easy-to-use graphical interface
 **Comprehensive support** - Supports all file and folder types 

---

##  Security features

### Encryption Algorithm
```
- AES-256-GCM (Advanced Encryption Standard)
- 256-bit key length
- Galois/Counter Mode (GCM) for authentication
```

### Key Derivation 
```
PBKDF2-HMAC-SHA256
- 600,000 iterations
- 16-byte random salt
- Resistant to Brute Force attacks
```

### Additional Security
```
✓ Cryptographic Hash Verification (SHA-256)
✓ Secure File Deletion (3-pass overwrite)
✓ Magic Header Validation
✓ File Size Integrity Check
✓ Nonce Randomization (12-byte random per file)
```

### The encrypted file contains:
```
[Magic Header 10 bytes] + [Version 4 bytes] + [File Size 8 bytes] 
+ [Salt 16 bytes] + [Nonce 12 bytes] + [Encrypted Data]
```

---

## Requirements

### Required system:
- **Python**: 3.8 or later
- **OS**: Windows, macOS, Linux
- **Memory**: 512 MB minimum
- **Storage**: Depending on the size of the files to be encrypted

### Required libraries:
```bash
- cryptography >= 41.0.0
- customtkinter >= 5.0.0
- Pillow >= 10.0.0
```

---

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/BassemMohamed44/LOCK-0.git
cd LOCK-0
```

### Step 2: Install the libraries
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install cryptography customtkinter pillow
```

### Step 3: Run the program
```bash
python LOCK-0.py
```

### (Optional) Create an executable .exe file
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=L0.ico LOCK-0.py
```

---

##  How to use

### GUI:

#### **To encrypt files:**

1. **Select the folder** - Click on "Browse" and select the folder you want to encrypt.
2. **Enter the password** - Enter a strong password (8+ characters)
   - Make sure you remember your password! Without it, you won't be able to decrypt the encryption.
3. **Select "File Encryption"**
4. **Click "Start Process"**
5. The original files will be securely deleted after successful encryption.

####  **To decrypt files:**

1. **Select the folder** - Select the folder containing the `.enc` files.
2. **Enter the password** - Enter the same password used for encryption.
3. **Select "Decrypt"**
4. **Click "Start Process"**
5. The original files will be visible once the `.enc` files are removed.

---

## Technical specifications

### Release Information:
| Feature | Description |
|-------|-------|
| **Version** | 1.0.0 (Stable) |
| **Release date** | 2026 |
| **Programming language** | Python 3.8+ |
| **Program size** | ~50 MB (With libraries) |

### security algorithms:
```
┌─────────────────────────────────────┐
│   LOCK-0 Security Architecture      │
├─────────────────────────────────────┤
│                                     │
│  User Password                      │
│       ↓                             │
│  PBKDF2 (SHA-256, 600K iterations)  │
│       ↓                             │
│  256-bit Key                        │
│       ↓                             │
│  AES-256-GCM                        │
│       ↓                             │
│  Encrypted File + Metadata          │
│                                     │
└─────────────────────────────────────┘
```

### Performance:
- **Encryption speed**: ~50-100 MB/s (According to the processor)
- **Memory consumption**: Variable depending on file size
- **Compression**: No compression (maintains original size)

---

##  Practical examples

### Example 1: Encrypting an entire folder
```bash
# Folder: E:/my_documents/
# Password: MySecurePassword123
# Result: All files become *.enc
```

### Example 2: Decrypting files
```bash
# Folder: E:/my_documents/
# Password: MySecurePassword123
# Result: The original files reappear
```

### Example 3: The encrypted file
```
Before encryption:
  document.pdf          (2.5 MB)
  photo.jpg             (5.2 MB)
  video.mp4             (250 MB)

After encryption:
  document.pdf.enc      (2.5 MB)
  photo.jpg.enc         (5.2 MB)
  video.mp4.enc         (250 MB)
  
Original files: Safely deleted
```

---

## Frequently Asked Questions

### Q: Is the program really safe?
**A:** Yes! LOCK-0 uses encryption standards:
- AES-256 (the same one used by the US government)
- PBKDF2 with 600,000 replicates (safe against Brute Force attacks)
- GCM Authentication (Data Integrity Verification)

### Q: What if I forget my password?
**A:** There is no way to decrypt the data without the correct password. This is intentional for security reasons!
- Make sure to save your password in a safe place

### Q: Can files be decrypted from another server?
**A:** Yes! As long as you have:
1. Encrypted files (`.enc`)
2. Correct password
3. LOCK-0 installed on the device

### Q: Does the program compress files?
**A:** No. The program retains the original file size (it may increase slightly due to metadata security).

### Q: Can operating system files be encrypted?
**A:** We do not recommend encrypting critical operating system files! Use it for personal files only.

### Q: How long does the encryption process take?
**A:** It depends on:
- File size (larger = slower) 
- Processor speed 
- Hard drive speed 
- Average time: 50-100 MB/s

### Q: Does the program work without internet?
**A:** Yes, absolutely! The program works completely independently without the internet.

### Q: Can the same password be used for multiple files?
**A:** Yes, but it is preferable to use different strong passwords for very sensitive files.

---

## Contribution

We welcome your contributions! If you want to improve LOCK-0:

### steps Contribution:
1. **Fork** repo
2. **A branch was established** new:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make changes** and add improvements
4. **Test** the changes thoroughly
5. **Submit** Pull Request

### Areas of welcome development:
- Improved graphical interface
- Additional security features
- Improved performance
- Improved documentation
- Bug fixes
- Support for new languages

---

##  Licensing

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

### In short:
 You can use the program freely.
 You can modify it.
 You can distribute it.
 No warranty or liability from the developers.
---

## Important security warnings

### Before using LOCK-0:

1. **Keep your password** in a very secure place.
- Without it, you won't be able to decrypt the data!
- There is no "forgot password" option.

2. **Make a Backup** Before Encrypting
- Make sure you have a backup of your important files
- In case something goes wrong

3. **Use strong passwords**
- Don't use easy passwords (e.g., 123456)
- Use a combination of: uppercase letters + lowercase letters + numbers + symbols

4. **Do not encrypt system files**
- Avoid encrypting critical operating system files
- This may cause the system to fail to boot

5. **Test First**
- Test on unimportant files first.
- Make sure you understand the tool before using it on sensitive files.

---

## Support and assistance

### Found a bug?
-  Open [Issue New](https://github.com/BassemMohamed44/LOCK-0/issues/new)
- Explain the problem in detail. 
- Add screenshots if possible.

### Questions?
- Use the Discussions forum
- Or send an email

---

## Roadmap

### Planned features: 

- [ ] Night and light mode support
- [ ] Individual file encryption support
- [ ] Advanced settings options
- [ ] Command-line interface (CLI) version
- [ ] Mobile app
- [ ] Additional language support
- [ ] Encryption statistics display
- [ ] Advanced progress notifications

---

##  Educational resources

### About encryption:
- [AES Encryption Explained](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [PBKDF2 Key Derivation](https://en.wikipedia.org/wiki/PBKDF2)
- [GCM Authentication Mode](https://en.wikipedia.org/wiki/Galois/Counter_Mode)

### About safety:
- [OWASP Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)
- [Password Security Best Practices](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---

##  Thanks and appreciation

Thank you for using LOCK-0! If you liked the project: 
- Add a star to the repository
- Share the project with others
- Share your feedback and suggestions

---

## legal texts

### Disclaimer:
```
LOCK-0 is provided "as is" without any warranty of any kind.
Use of this software is at your own risk.
The developers accept no responsibility for data loss or other damages.
```

---

<div align="center">

** LOCK-0 - Keep Your Files Safe **

[Back to Top](#-lock-0-v1.0.0---encryption-suite)

</div>
