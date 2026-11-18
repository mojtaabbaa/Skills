# قوانین مهندسی دسته ۸: پوسته ساز و موتور پاپ‌آپ (Theme Builder & Popup Rules)

این سند قوانین مربوط به زیرسیستم‌های طراحی قالب پوسته و پنجره‌های پاپ‌آپ در **Elementor Pro** را تبیین می‌کند.

---

## ۱. قوانین پوسته ساز (Theme Builder)
1. **ثبت لوکیشن‌های جدید قالب:** ثبت موقعیت‌ها باید صرفاً با اکشن `elementor/theme/register_locations` و از طریق کلاس `Locations_Manager` صورت پذیرد.
2. **بررسی موقعیت‌های پیش‌فرض:** المنتور پرو موقعیت‌های استاندارد زیر را مدیریت می‌کند:
   - `header` (هدر سایت)
   - `footer` (فوتر سایت)
   - `single` (برگه یا نوشته تکی)
   - `archive` (بایگانی، دسته‌ها، برچسب‌ها و تاریخ)
3. **شرط‌های نمایش (Display Conditions):** شروط درج (Include) و استثنا (Exclude) توسط ماژول `display-conditions` ارزیابی می‌شوند. هنگام ایجاد شروط جدید، اولویت با شروط خاص‌تر (Specific Post) نسبت به شروط عمومی (All Posts) است.

---

## ۲. قوانین موتور پاپ‌آپ (Popup Engine)
1. **جداسازی سه‌گانه منطق پاپ‌آپ:**
   - **Conditions (شرط‌ها):** تعیین صفحاتی که پاپ‌آپ باید لود شود.
   - **Triggers (محرک‌ها):** رویداد نمایش (Page Load, Scroll, Scroll to Element, Click, Inactivity, Exit Intent).
   - **Advanced Rules (قوانین پیشرفته):** دفعات نمایش (Show after X page views, Show up to X times, When arriving from specific URL, Show on devices).
2. پاپ‌آپ‌ها به عنوان سند `ElementorPro\Modules\Popup\Document` مدیریت می‌شوند و بارگذاری آنها در فرانت‌اند از طریق اکشن فرانت‌اند `elementorFrontend.modules.popup` صورت می‌گیرد.

---

## ۳. قانون الزام بازگشت به سورس‌کد (Source Code Fallback Directive)
> [!IMPORTANT]
> در صورت نیاز به بررسی نحوه ارزیابی شروط، هوک‌های بازنویسی تمپلیت یا کدهای تریگر پاپ‌آپ، عامل باید مستقیماً سورس فایل‌های `elementor-pro/modules/theme-builder/`، `elementor-pro/modules/theme-builder/classes/locations-manager.php` و `elementor-pro/modules/popup/` را بازبینی کند.
