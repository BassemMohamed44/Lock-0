# Contributing to LOCK-0 | المساهمة في LOCK-0

شكراً لك على اهتمامك بالمساهمة في LOCK-0!

هذا الملف يحتوي على إرشادات لمساعدتك على المساهمة بشكل فعال.

---

## جدول المحتويات

- [الدليل السلوكي](#الدليل-السلوكي)
- [طريقة البدء](#طريقة-البدء)
- [عملية المساهمة](#عملية-المساهمة)
- [معايير الكود](#معايير-الكود)
- [الاختبار](#الاختبار)
- [كتابة التوثيق](#كتابة-التوثيق)
- [أنواع المساهمات](#أنواع-المساهمات)

---

## الدليل السلوكي

### التزامنا

نحن ملتزمون بتوفير بيئة مرحبة وشاملة للجميع.

### السلوك المتوقع

✅ **افعل**:
- استخدم لغة احترافية ومحترمة
- كن صبوراً مع الآخرين
- قبل الاختلافات في الآراء
- ركز على ما هو أفضل للمجتمع
- دعم أعضاء المجتمع الآخرين

❌ **لا تفعل**:
- تحرش أو تمييز أي شخص
- استخدام لغة جنسية أو عدائية
- مهاجمة شخصياً
- الإجهار بمعلومات خاصة الآخرين
- سلوك عدائي آخر

### فرض القوانين

الانتهاكات يمكن أن تؤدي إلى:
- تحذير
- مراجعة الوصول
- الحظر الدائم

---

## طريقة البدء

### المتطلبات الأساسية:

```bash
# Python 3.8+
python --version

# Git
git --version

# المكتبات المطلوبة
pip install -r requirements.txt
pip install pytest black flake8
```

### إعداد بيئة التطوير:

```bash
# 1. اعمل Fork للمستودع على GitHub
# (اضغط زر Fork في أعلى الصفحة)

# 2. استنسخ مستودعك الخاص
git clone https://github.com/BassemMohamed44/LOCK-0.git
cd LOCK-0

# 3. أضف المستودع الأصلي كمصدر للتحديثات
git remote add upstream https://github.com/BassemMohamed44/LOCK-0.git

# 4. أنشئ بيئة افتراضية
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 5. ثبت المكتبات
pip install -r requirements.txt
pip install pytest black flake8 mypy
```

---

## عملية المساهمة

### اختر مجال المساهمة

```
✅ أنواع المساهمات المرحب بها:
- إصلاح الأخطاء (Bug Fixes)
- ميزات جديدة (New Features)
- تحسين التوثيق (Documentation)
- تحسينات الواجهة (UI/UX)
- تحسينات الأداء (Performance)
- تحسينات الأمان (Security)
- إضافة اختبارات (Tests)
- إعادة هيكلة الكود (Refactoring)
```

### أنشئ مشكلة (Issue) أولاً

قبل البدء في العمل:

```bash
# تحقق من المشاكل الموجودة
# للتأكد من عدم عمل أحد بنفس الفكرة

# ثم أنشئ Issue جديد:
# - اذهب إلى Issues
# - اضغط "New Issue"
- اشرح المشكلة أو المميزة بوضوح
- أضف أمثلة أو لقطات شاشة
```

### أنشئ فرع عمل (Branch)

```bash
# تحديث الفرع الرئيسي
git fetch upstream
git checkout main
git merge upstream/main

# أنشئ فرع جديد
git checkout -b feature/your-feature-name

# أمثلة على أسماء الفروع:
# - feature/add-dark-theme
# - bugfix/fix-password-validation
# - docs/improve-readme
# - perf/optimize-encryption
```

### عدّل الكود

```python
# مثال: تحسين دالة التشفير

def encrypt_file(path, password, log):
    """
    حسّن الوثائق إذا لزم الأمر
    """
    try:
        # أضف تحسينات هنا
        # تأكد من اتباع معايير الكود
        pass
    except Exception as e:
        log(f"[!] Error: {str(e)}")
        return False
```

### التزم بالتغييرات

```bash
# عرض التغييرات
git status
git diff

# أضف الملفات
git add .

# أنشئ commit واضح
git commit -m "type: brief description

Longer description explaining:
- What changed
- Why it changed
- How it works

Fixes #ISSUE_NUMBER"

# أمثلة:
# git commit -m "fix: resolve AESGCM key size issue"
# git commit -m "feat: add dark theme support"
# git commit -m "docs: improve CONTRIBUTING.md"
```

### ادفع إلى فرعك

```bash
git push origin feature/your-feature-name
```

### أنشئ Pull Request

1. اذهب إلى مستودعك على GitHub
2. سترى إشعار لإنشاء PR
3. املأ قالب PR:

```markdown
## Description | الوصف
قصير وواضح لما تفعل.

## Type of Change | نوع التغيير
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## How Has This Been Tested? | كيف تم الاختبار؟
اشرح اختبارات الاختبار.

## Checklist | قائمة التحقق
- [ ] My code follows the style guidelines
- [ ] I have tested my changes
- [ ] I have updated the documentation
- [ ] I have added tests for new features

## Related Issues | المشاكل ذات الصلة
Fixes #ISSUE_NUMBER
```

### الانتظار للمراجعة

- ستتلقى تعليقات من المراجعين
- اطلب التوضيحات إذا لزم الأمر
- قم بالتغييرات المطلوبة
- ادفع التحديثات

---

##  معايير الكود

### أسلوب الكود:

```python
# جيد
def derive_key(password: str, salt: bytes) -> bytes:
    """استخلاص مفتاح التشفير من كلمة السر.
    
    Args:
        password: كلمة السر المدخلة
        salt: بيانات عشوائية
        
    Returns:
        المفتاح المشتق (256-bit)
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


# ❌ سيء
def derive_key(password,salt):
    kdf = PBKDF2HMAC(hashes.SHA256(), 32, salt, 600000, default_backend())
    return kdf.derive(password.encode())
```

### معايير Python:

```bash
# استخدم Black لتنسيق الكود
black LOCK-0_IMPROVED.py

# استخدم Flake8 للتحقق من الأخطاء
flake8 LOCK-0_IMPROVED.py

# استخدم MyPy للتحقق من الأنواع
mypy LOCK-0_IMPROVED.py
```

### معايير التعليقات:

```python
# ✅ تعليق جيد
# هذا يمنع استرجاع البيانات من القرص الصلب
for _ in range(3):
    f.write(os.urandom(file_size))

# ❌ تعليق سيء
# اكتب بيانات عشوائية
for _ in range(3):
    f.write(os.urandom(file_size))
```

### معايير الأمان:

```python
# ✅ آمن
password = password_var.get()
if len(password) < 8:
    messagebox.showwarning("Warning", "Password too weak")
    return

# ❌ غير آمن
password = password_var.get()
# لا تتحقق من طول كلمة السر
```

---

## الاختبار

### تشغيل الاختبارات:

```bash
# تثبيت pytest
pip install pytest

# تشغيل جميع الاختبارات
pytest tests/

# تشغيل اختبار محدد
pytest tests/test_encryption.py

# مع تقرير التغطية
pytest --cov=. tests/
```

### كتابة اختبارات جديدة:

```python
# tests/test_encryption.py
import pytest
from LOCK_0_IMPROVED import derive_key, encrypt_file

def test_derive_key():
    """اختبر استخلاص المفتاح"""
    password = "test_password_123"
    salt = b"1234567890123456"
    
    key = derive_key(password, salt)
    
    assert len(key) == 32  # 256 bits
    assert isinstance(key, bytes)

def test_encrypt_file_integration():
    """اختبر التشفير الكامل"""
    # أنشئ ملف اختبار
    test_file = "test_data.txt"
    with open(test_file, "w") as f:
        f.write("test content")
    
    # شفر الملف
    success = encrypt_file(test_file, "password123", print)
    
    assert success
    assert os.path.exists(f"{test_file}.enc")
    assert not os.path.exists(test_file)
```

---

## كتابة التوثيق

### تحسين README:

```markdown
## موضوع جديد

### القسم الفرعي

شرح واضح وبسيط مع:
- ✅ أمثلة عملية
- ✅ رموز
- ✅ روابط مفيدة
```

### تحديث docstrings:

```python
def my_function(param1: str, param2: int) -> bool:
    """وصف قصير للدالة.
    
    وصف أطول إذا لزم الأمر يشرح الآلية.
    
    Args:
        param1: شرح المعامل الأول
        param2: شرح المعامل الثاني
        
    Returns:
        شرح القيمة المرجعة
        
    Raises:
        ValueError: عندما تحدث هذه الحالة
        
    Example:
        >>> my_function("test", 42)
        True
    """
```

---

## أنواع المساهمات

### إصلاح الأخطاء

```bash
git commit -m "fix: brief description of bug"
```

### ميزات جديدة

```bash
git commit -m "feat: brief description of feature

- Feature detail 1
- Feature detail 2"
```

### التوثيق

```bash
git commit -m "docs: update documentation

- Updated section
- Added examples"
```

### تحسينات الواجهة

```bash
git commit -m "ui: improve user interface

- Changed button colors
- Added dark theme"
```

### تحسينات الأداء

```bash
git commit -m "perf: optimize encryption speed

- Reduced memory usage
- Improved algorithm efficiency"
```

### تحسينات الأمان

```bash
git commit -m "security: enhance encryption security

- Increased iterations to 600K
- Added secure deletion"
```

---

## قائمة التحقق قبل الإرسال

- [ ] قرأت CONTRIBUTING.md
- [ ] أتبعت معايير الكود
- [ ] اختبرت التغييرات
- [ ] أضفت اختبارات جديدة
- [ ] حدثت التوثيق
- [ ] لم أجعل أي نصوص مقسومة بشكل غير ضروري
- [ ] التزاماتي واضحة ووصفية
- [ ] أشرت إلى المشكلة المتعلقة

---

## تحتاج مساعدة؟

### قنوات التواصل:

- **البريد الإلكتروني**: contact@lock-0.dev
- **GitHub Issues**: للأسئلة والمشاكل
- **Wiki**: للتوثيق الإضافي
- **Discussions**: للنقاشات العامة

### موارد مفيدة:

- [Git Guide](https://git-scm.com/book/en/v2)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Commit Message Guidelines](https://www.conventionalcommits.org/)

---

## شكر خاص

شكراً لك على المساهمة!

كل مساهمة، مهما كانت صغيرة، تساعدنا على تحسين LOCK-0.

---

<div align="center">

**Happy Contributing!**

[⬆ Back to Top](#contributing-to-lock-0--المساهمة-في-lock-0)

</div>
