#  Security Policy | سياسة الأمان

## Reporting a Vulnerability | الإبلاغ عن ثغرة أمنية

إذا اكتشفت ثغرة أمنية في LOCK-0، **يرجى عدم فتح issue عام**. بدلاً من ذلك:

### طريقة الإبلاغ الآمنة:
1. **أرسل بريد إلكتروني خاص** إلى الفريق الأمني
2. **وصف الثغرة بالتفصيل** مع خطوات إعادة الإنتاج
3. **قدم أي ملفات أو أكواد** ذات صلة (بحذر)
4. **امنح الفريق وقتاً** لإصلاح الثغرة (عادة 90 يوم)

### لا تفعل:
❌ لا تنشر تفاصيل الثغرة علناً قبل الإصلاح  
❌ لا تجرب الثغرة على أنظمة أخرى  
❌ لا تحاول استخدام الثغرة للوصول لبيانات غيرك  

---

## Security Best Practices | أفضل ممارسات الأمان

### كلمة السر القوية
```
❌ ضعيفة:
  - 123456
  - password
  - admin
  - qwerty

✅ قوية:
  - Tr0p1cal!Sunset#2024
  - K9@mPxQr#Yw2vL4dn
  - MyS3cur3P@ssw0rd!
```

**معايير كلمة السر القوية:**
- 12+ حرف على الأقل
- مزيج من: أحرف كبيرة + صغيرة + أرقام + رموز
- لا تستخدم معلومات شخصية
- فريدة لكل استخدام

### إدارة الملفات المشفرة
```
✓ احفظ الملفات المشفرة في مكان آمن
✓ عمل نسخ احتياطية من الملفات المشفرة
✓ احفظ كلمات السر في مدير كلمات سر معروف
✓ لا تشارك كلمات السر عبر البريد أو الدردشة
```

### النسخ الاحتياطية
```
استراتيجية 3-2-1:
- 3 نسخ من البيانات
- 2 وسائط تخزين مختلفة
- 1 نسخة خارج الموقع (خارج المنزل)

مثال:
- نسخة على الجهاز الأساسي
- نسخة على قرص خارجي
- نسخة على السحابة (مشفرة)
```

---

## Known Vulnerabilities | الثغرات المعروفة

### الحالية:
- ❌ لا توجد ثغرات أمنية معروفة حالياً

### السابقة:
```
v1.0:
- Fixed: Key size mismatch with AESGCM
- Fixed: Weak PBKDF2 iterations (200K → 600K)
- Fixed: Unsafe file deletion

```

---

## Security Improvements | التحسينات الأمنية المخططة

### المرحلة القادمة:
- [ ] دعم معايير التشفير المتقدمة (ChaCha20-Poly1305)
- [ ] تطبيق مدير كلمات سر مدمج
- [ ] حماية ضد جرائم الوقت (Timing Attacks)
- [ ] دعم المفاتيح المتعددة (Multi-Key Encryption)
- [ ] تقارير أمنية دورية

---

## Cryptographic Details | تفاصيل التشفير

### خوارزميات المستخدمة:
```
┌─────────────────────────────────────┐
│        LOCK-0 Crypto Stack          │
├─────────────────────────────────────┤
│ Layer 1: Key Derivation             │
│   → PBKDF2-HMAC-SHA256              │
│   → 600,000 iterations              │
│   → 16-byte random salt             │
│                                     │
│ Layer 2: Encryption                 │
│   → AES-256-GCM                     │
│   → 12-byte random nonce            │
│   → 256-bit key                     │
│                                     │
│ Layer 3: Integrity                  │
│   → GCM Authentication Tag          │
│   → SHA-256 File Hash               │
│                                     │
│ Layer 4: Deletion                   │
│   → 3-pass secure overwrite         │
│   → Cryptographically random data   │
└─────────────────────────────────────┘
```

### معايير التشفير:
| المكون | المعيار | الحالة |
|------|--------|--------|
| **الخوارزمية** | AES-256-GCM |  آمنة |
| **مشتقة المفتاح** | PBKDF2-SHA256 | آمنة |
| **عدد التكرارات** | 600,000 | آمنة |
| **حجم المفتاح** | 256 bits | آمنة |
| **طول Nonce** | 12 bytes | آمنة |
| **الحذف الآمن** | 3-pass | آمنة |

---

## Security Testing | اختبار الأمان

### الاختبارات المجراة:
```
 Brute Force Resistance
 Cryptographic Randomness
 Key Derivation Strength
 File Integrity Verification
 Secure Deletion
 Memory Safety
```

### كيفية اختبار الأمان بنفسك:
```bash
echo "test data" > test.txt
# 2. شفر الملف
python LOCK-0.py
# 3. تحقق من حجم الملف المشفر
ls -la test.txt.enc
# 4. جرب كلمة سر خاطئة (يجب أن تفشل)
# 5. فك التشفير بكلمة السر الصحيحة
# 6. قارن الملف الأصلي بالملف المفكك
diff test.txt test_decrypted.txt
```

---

## Dependencies Security | أمان المكتبات الخارجية

### المكتبات المستخدمة:
```
cryptography (v41.0.0+)
├─ Status: معروفة وموثوقة
├─ Audits: متعددة من جهات مستقلة
├─ Updates: منتظمة
└─ CVE: لا توجد ثغرات معروفة

customtkinter (v5.0.0+)
├─ Status: مشروع نشط
├─ Security: لا توجد مشاكل معروفة
└─ Updates: منتظمة

Pillow (v10.0.0+)
├─ Status: معروفة وموثوقة
├─ Audits: متعددة
└─ Updates: منتظمة
```

### فحص المكتبات:
```bash
# للتحقق من الثغرات المعروفة
pip install safety
safety check

# أو استخدم
pip install bandit
bandit -r .
```

---

## Compliance | التوافقية

### معايير الأمان المتبعة:
-  **NIST Guidelines** - معايير المعهد الوطني للمعايير والتكنولوجيا
-  **OWASP Standards** - معايير الأمان على الويب
-  **FIPS 140-2** - معايير التشفير الفيدرالية الأمريكية
-  **CWE Top 25** - أكثر نقاط الضعف شيوعاً

---

## Support & Contact | الدعم والتواصل

### الإبلاغ عن مشاكل أمنية:
 **البريد الإلكتروني**: [00xBassem@gmail.com](mailto:00xBassem@gmail.com)

### الدعم العام:
 **GitHub Issues**: [اضغط هنا](  )

---

## Version History | سجل الإصدارات

### v1.0.0 (الحالي - آمن)
```
 PBKDF2 مع 600,000 iterations
 AES-256-GCM
 حذف آمن للملفات
 التحقق من السلامة الكاملة
 دعم اللغة العربية
```

---

## Additional Resources | موارد إضافية

### قراءة موصى بها:
- [NIST Cryptographic Standards](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38D.pdf)
- [OWASP Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)
- [Password Storage Guide](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

### الأدوات المساعدة:
- [Have I Been Pwned](https://haveibeenpwned.com/) - تحقق من كلمات السر
- [Password Generator](https://bitwarden.com/password-generator/) - مولد كلمات سر قوية
- [Cryptography Libraries](https://en.wikipedia.org/wiki/Comparison_of_cryptography_software)

---

<div align="center">

**Security First - Always** 

Last Updated: 2026  
Security Status:  SECURE

</div>
