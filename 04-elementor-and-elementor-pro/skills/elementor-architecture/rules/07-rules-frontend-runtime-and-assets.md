# قوانین مهندسی دسته ۷: ران‌تایم فرانت‌اند و مدیریت است‌ها (Frontend Runtime & Assets Rules)

این سند استانداردهای کار با ران‌تایم کلاینت جاوااسکریپت و بهینه‌سازی بارگذاری است‌ها در فرانت‌اند را مشخص می‌سازد.

---

## ۱. قوانین بارگذاری شرطی فایل‌های استاتیک (Conditional Asset Enqueueing)
1. **استفاده از متدهای وابستگی:** هر اسکریپت یا استایل خارجی حجیم باید در وردپرس رجیستر شده و شناسه آن در متدهای `get_script_depends()` یا `get_style_depends()` ویجت بازگردانده شود.
2. **پرهیز از انکیوی سراسری بی‌مورد:** هرگز کتابخانه‌هایی مانند Swiper یا Waypoints را در تمام صفحات بدون اینکه ویجت متناظر حضور داشته باشد `wp_enqueue_script` نکنید.

---

## ۲. قوانین ران‌تایم فرانت‌اند جاوااسکریپت (`window.elementorFrontend`)
1. **ثبت هندلر رویداد ویجت:** راه‌اندازی کدهای جاوااسکریپت تعاملی برای یک ویجت باید منحصراً از طریق Event Bus فرانت‌اند المنتور ثبت شود:
   ```javascript
   jQuery(window).on('elementor/frontend/init', function() {
       elementorFrontend.hooks.addAction('frontend/element_ready/my-widget-slug.default', function($scope, $) {
           // کد راه‌اندازی اسلایدر یا انیمیشن
       });
   });
   ```
2. **تخریب و بازنشانی (Destroy Handlers):** در صورتی که ویجت کتابخانه‌ای با رویدادهای تایمر یا لیسنر اسکرول ایجاد می‌کند، هنگام بازرندر شدن در ادیتور، ابتدا باید اینستنس قبلی Destroy شود تا از نشت حافظه (Memory Leak) در مرورگر جلوگیری گردد.

---

## ۳. قانون الزام بازگشت به سورس‌کد (Source Code Fallback Directive)
> [!IMPORTANT]
> در صورت نیاز به بررسی دقیق شیوه فعال‌سازی هندلرها، لودر است‌ها یا ساختار `frontend.js`، عامل باید مستقیماً سورس فایل‌های `elementor/includes/frontend.php`، `elementor/assets/js/frontend.js` و `elementor/core/page-assets/loader.php` را بررسی کند.
