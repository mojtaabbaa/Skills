# راهنمای شروع سریع (Quick Start Guide)

این راهنما گام‌به‌گام نحوه استفاده و بهره‌برداری از ساختار دسته‌بندی‌شده اسکیل‌ها و ریسورس‌های نمونه را توضیح می‌دهد.

---

## ۱. نحوه بارگذاری و استفاده در پروژه‌ها

هر پوشه اسکیل شامل یک فایل استاندار `SKILL.md` است. برای استفاده در پروژه‌های محلی یا ابزارهای کدنویسی هوش مصنوعی (مانند Google Antigravity، Claude Code، Cursor و Windsurf):

### الف) استفاده به صورت Workspace Skills (پیشنهادی برای پروژه‌ها):
پوشه اسکیل دلخواه خود را مستقیماً در مسیر `.agents/skills/` پروژه خود کپی کنید:
```bash
# مثال: افزودن اسکیل مهندسی وودمارت به پروژه
mkdir -p .agents/skills
cp -r 03-woodmart-theme-engineering/skills/woodmart-theme-engineering .agents/skills/
```

### ب) استفاده به صورت Global Skills:
می‌توانید اسکیل‌ها را در مسیر گلوبال ابزار هوش مصنوعی خود کپی کنید (در Antigravity مسیر `~/.gemini/config/skills/`).

---

## ۲. استفاده از کدهای نمونه (Sample Resources)

در هر دسته‌بندی، یک پوشه اختصاصی به نام `sample-resources` در کنار اسکیل‌ها قرار دارد:

1. **در پوشه `01-wordpress-core-and-architecture/sample-resources`**:
   - `custom-plugin-boilerplate`: افزونه آماده بر پایه معماری ماژولار شیءگرا، با پشتیبانی کامل از HPOS و هوک‌های امنیتی.
   - `rest-api-controller-example.php`: کلاس کنترلر REST API با تفکیک متدهای خواندن و ایجاد داده.
   - `custom-table-dbdelta-migration.php`: مایگریشن جداول دیتابیس با نسخه اختصاصی در جدول آپشن‌ها.

2. **در پوشه `02-woocommerce-and-catalog-systems/sample-resources`**:
   - `ajax-catalog-filter`: فیلتر سریع کاتالوگ با پشتیبانی از کشویی موبایل و اعمال آنی دسکتاپ.
   - `custom-payment-gateway-sample.php`: اسکلت پیاده‌سازی کلاس درگاه پرداخت ووکامرس.

3. **در پوشه `03-woodmart-theme-engineering/sample-resources`**:
   - `woodmart-pjax-reinit-handler.js`: مدیریت رویدادهای `pjax:complete` و `wdShopPageInit` برای اجرای مجدد اسکریپت‌ها.
   - `sticky-sidebar-flexbox-fix.css`: رفع تضمینی باگ جمع‌شدگی ستون فیلتر استیکی المنتور در کانتینرها.

4. **در پوشه `04-elementor-and-elementor-pro/sample-resources`**:
   - `class-custom-product-card-widget.php`: الگوی ساخت ویجت المنتور با استایل‌های ریسپانسیو.
   - `class-custom-form-webhook-action.php`: اکشن ارسال داده‌های فرم المنتور پرو به وب‌هوک و CRM.

5. **در پوشه `05-ui-ux-and-frontend-engineering/sample-resources`**:
   - `rtl-typography-and-spacing.css`: تنظیمات تایپوگرافی دو زبانه فارسی/انگلیسی و حداقل سایز ۴۴ پیکسل برای تاچ.
   - `sample-design-tokens.json`: ساختار توکن‌های استاندارد طراحی.

---

## ۳. تست و اعتبارسنجی خودکار

پیش از هرگونه کامیت یا استفاده، برای اعتبارسنجی تمام اسکیل‌ها دستور زیر را اجرا کنید:
```bash
python tools/validate_all_skills.py
```
