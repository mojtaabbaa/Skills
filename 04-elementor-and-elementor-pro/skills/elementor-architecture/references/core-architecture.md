# معماری هسته، چرخه حیات و پایگاه داده المنتور (Core Architecture & DB)

این سند مرجع فنی عمیق ساختار زیربنایی **Elementor Core (4.2.3)** و **Elementor Pro (4.3.2)** است.

---

## ۱. چرخه حیات بوت‌استرپ (Bootstrap Sequence)

### ۱.۱. فایل ورودی هسته (`elementor/elementor.php`)
- **پیش‌نیازهای محیطی:**
  - PHP نسخه 7.4 به بالا
  - WordPress نسخه 6.8 به بالا
- **ثابت‌های عمومی:**
  - `ELEMENTOR_VERSION`: مقدار `4.2.3`
  - `ELEMENTOR_PATH`: مسیر فیزیکی پوشه پلاگین در سرور
  - `ELEMENTOR_URL`: آدرس وب پوشه پلاگین
  - `ELEMENTOR_ASSETS_PATH` و `ELEMENTOR_ASSETS_URL`: مسیر فایل‌های استاتیک فرانت‌اند و ادیتور
- **اتولودر اختصاصی (`includes/autoloader.php`):**
  - رجیستر کردن فضای نام پایه `Elementor\`.
  - تبدیل خودکار نام کلاس به فایل با جایگزینی `_` با `-` و استفاده از حروف کوچک (مثال: `Elementor\Controls_Manager` -> `includes/managers/controls.php`).
- **راه‌اندازی پلاگین:**
  - هوک به اکشن `plugins_loaded` در وردپرس برای نمونه‌سازی کلاس Singleton اصلی:
    ```php
    add_action( 'plugins_loaded', 'elementor_load_plugin' );
    function elementor_load_plugin() {
        \Elementor\Plugin::instance();
    }
    ```

### ۱.۲. فایل ورودی پرو (`elementor-pro/elementor-pro.php`)
- **ثابت‌های عمومی:**
  - `ELEMENTOR_PRO_VERSION`: مقدار `4.3.2`
  - `ELEMENTOR_PRO_REQUIRED_CORE_VERSION`: مقدار `'4.0'`
  - `ELEMENTOR_PRO_RECOMMENDED_CORE_VERSION`: مقدار `'4.2'`
- **بررسی صحت نسخه هسته:**
  - اگر نسخه Elementor Core کمتر از 4.0 باشد، لود پلاگین Pro متوقف شده و یک Admin Notice هشدار در داشبورد وردپرس نمایش داده می‌شود.
- **راه‌اندازی ماژول‌ها:**
  - پس از تایید لایسنس و نیازمندی‌ها، با هوک `elementor/init` نمونه `\ElementorPro\Plugin::instance()` فعال می‌شود.

---

## ۲. کلاس اصلی اورکستراتور (`\Elementor\Plugin`) و منیجرها

کلاس `Elementor\Plugin` الگوی Singleton مرکزی است که تمامی سرویس‌های حیاتی را در قالب خصوصیات عمومی نگهداری می‌کند:

| خصوصیت (Property) | کلاس سرویس | شرح وظیفه در سیستم |
| :--- | :--- | :--- |
| `controls_manager` | `Controls_Manager` | ثبت و واکشی انواع کنترل‌های فرم و استایل (شامل ۴۲ تایپ کنترل) |
| `elements_manager` | `Elements_Manager` | ثبت المان‌های سازنده کالبد (`container`, `section`, `column`) |
| `widgets_manager` | `Widgets_Manager` | ثبت، اینیشیالایز و نگهداری کاتالوگ تمام ویجت‌ها |
| `documents` | `Core\Documents_Manager` | مدیریت انواع پست‌ها و تمپلیت‌ها (`post`, `page`, `header`, `footer`, `popup`, `loop`) |
| `modules_manager` | `Core\Modules_Manager` | مدیریت و فعال‌سازی ۶۴ ماژول مستقل هسته |
| `posts_css_manager`| `Core\Files\CSS\Post` | تولید فایل‌های فیزیکی کش CSS و واکشی آن در هدر صفحات |
| `dynamic_tags` | `Core\DynamicTags\Manager` | اتصال کنترل‌های ویجت به تگ‌های داینامیک دیتابیس وردپرس و ACF/Pods |
| `experiments` | `Core\Experiments\Manager` | سیستم کنترل فیچرهای بتا و آزمایشی (مانند Grid, Container, Atomic) |
| `frontend` | `Frontend` | ران‌تایم سمت کلاینت، فیلتر `the_content` و تزریق فایل‌های استاتیک |
| `editor` | `Core\Editor\Editor` | آماده‌سازی داده‌های کانفیگ، انکیو اسکریپت‌های ادیتور و بارگذاری Iframe |
| `kits_manager` | `Core\Kits\Manager` | مدیریت Kit Document برای استایل‌های سراسری، پالت رنگ و تایپوگرافی |
| `templates_manager`| `TemplateLibrary\Manager` | ایمپورت، اکسپورت و اتصال به کتابخانه آنلاین تمپلیت‌ها |
| `breakpoints` | `Core\Breakpoints\Manager` | کنترل سیستم نقاط شکست ریسپانسیو (موبایل، تبلت، لپ‌تاپ و دسکتاپ بزرگ) |
| `data_manager_v2` | `Data\Manager` | مدیریت تبادل داده با معماری مدرن REST API V2 |
| `logger` | `Core\Logger\Manager` | ثبت لاگ خطاها و گزارش کرش‌های جاوااسکریپت و PHP |

---

## ۳. تفکیک وظایف دایرکتوری‌های پروژه

### ۳.۱. پوشه `elementor/`
* **`app/`**: برنامه‌های مستقل مبتنی بر React (Site Editor, Kit Library, User Preferences).
* **`assets/`**: است‌های استاتیک کامپایل‌شده؛ `js/frontend.min.js`، `css/frontend.min.css`، است‌های پکیج ادیتور (`assets/js/packages/`).
* **`core/`**: زیرساخت نرم‌افزاری؛ شامل پایگاه داده، سیستم مدیریت اسناد (Documents)، مدیریت فایل‌ها و کش CSS، سیستم اعلان‌های منسوخ‌شدن کدها (`dev-tools`).
* **`includes/`**: لایه کلاسیک و پایه‌ای؛ شامل کنترل‌ها (`includes/controls/`)، ویجت‌های پیش‌فرض (`includes/widgets/`) و کلاس‌های والد (`includes/base/`).
* **`modules/`**: ۶۴ ماژول ماژولار هسته، شامل ماژول انقلابی `atomic-widgets`، `nested-elements`، `nested-tabs`، `nested-accordion`، `floating-buttons`، `link-in-bio`، `components`، `ai` و `mcp`.

### ۳.۲. پوشه `elementor-pro/`
* **`core/modules-manager.php`**: هاب ثبت و بارگذاری ۶۸ ماژول اختصاصی پرو.
* **`base/`**: شامل `Base_Widget` و `Module_Base` که پایه ویجت‌ها و ماژول‌های پرو هستند.
* **`modules/`**: ۶۸ ماژول حرفه‌ای نظیر `theme-builder`، `forms`، `atomic-form`، `popup`، `woocommerce`، `loop-builder`، `collection-loop`، `mega-menu`، `off-canvas`، `dynamic-tags`، `motion-fx`، `custom-css`، `custom-code`، `payments` و `aparat-video`.

---

## ۴. جریان داده و ساختار پایگاه داده (Data Flow & Storage)

### ۴.۱. متادیتاهای وردپرس در جدول `wp_postmeta`
هر برگه‌ای که با المنتور ویرایش می‌شود، داده‌های زیر را در جدول `wp_postmeta` دارد:

1. **`_elementor_data`**:
   - مهم‌ترین فیلد؛ یک ساختار درختی JSON است که تمامی عناصر، کانتینرها، ویجت‌ها، ستون‌ها و مقادیر تنظیمات (`settings`) را با شناسه رندوم (`id`) ذخیره می‌کند:
   ```json
   [
     {
       "id": "e4f3a21",
       "elType": "container",
       "isInner": false,
       "settings": {
         "flex_direction": "column",
         "boxed_width": {"unit": "px", "size": 1140}
       },
       "elements": [
         {
           "id": "b7c8d90",
           "elType": "widget",
           "widgetType": "heading",
           "settings": {
             "title": "سلام دنیا",
             "header_size": "h1"
           },
           "elements": []
         }
       ]
     }
   ]
   ```
2. **`_elementor_edit_mode`**: رشته `'builder'` که نشان‌دهنده رندر شدن برگه توسط موتور المنتور به جای ویرایشگر پیش‌فرض گوتنبرگ یا ادیتور کلاسیک است.
3. **`_elementor_template_type`**: نوع تمپلیت ذخیره‌شده (`post`, `page`, `header`, `footer`, `popup`, `single`, `archive`, `loop-item`).
4. **`_elementor_page_settings`**: تنظیمات سراسری صفحه شامل پدینگ صفحه، عنوان صفحه، چیدمان (Elementor Canvas / Elementor Full Width).
5. **`_elementor_css`**: متادیتای کش زمان ساخت فایل فیزیکی CSS صفحه.
6. **`_elementor_version` و `_elementor_pro_version`**: برای مدیریت نسخه‌بندی و اجرای تسک‌های ارتقای دیتابیس (Upgrades).

### ۴.۲. جداول سفارشی پایگاه داده در المنتور پرو (Custom Tables)
المنتور پرو برای مدیریت فرم‌ها و سیستم حاشیه‌نویسی از جداول اختصاصی بدون تداخل با جدول `wp_posts` استفاده می‌کند:

* **`wp_e_submissions`**:
  - ردیف‌های اصلی سابمیشن‌های فرم شامل `id`، `type`، `hash_id`، `post_id` (برگه‌ای که فرم در آن ثبت شده)، `form_name`، `user_id`، `created_at_gmt`.
* **`wp_e_submissions_values`**:
  - مقادیر تفکیک‌شده فیلدهای فرم شامل `id`، `submission_id` (کلید خارجی)، `key` (شناسه فیلد)، `value` (مقدار پرشده).
* **`wp_e_submissions_actions_log`**:
  - لاگ اکشن‌های پس از ارسال فرم شامل `id`، `submission_id`، `action_name` (مانند email, webhook, mailchimp)، `status` (success یا failed) و `log` خطا.
* **`wp_e_notes` و `wp_e_notes_users_relations`**:
  - سیستم ثبت یادداشت‌های مشارکتی تیم روی المنت‌ها با موقعیت مختصات x,y و وضعیت خوانده‌شدن.

---

## ۵. پایپ‌لاین رندرینگ فرانت‌اند و تولید استایل (Rendering & CSS Generation)

1. **فراخوانی اولیه:** درخواست کاربر توسط وردپرس دریافت و هوک `the_content` (یا فیلتر قالب `template_include` برای تم بیلدر) صدا زده می‌شود.
2. **بررسی سند (`Document`):** سند برگه از طریق `Plugin::$instance->documents->get($post_id)` نمونه‌سازی می‌شود.
3. **تولید یا فراخوانی فایل CSS:**
   - کلاس `Elementor\Core\Files\CSS\Post` وضعیت کش فایل `wp-content/uploads/elementor/css/post-{id}.css` را بررسی می‌کند.
   - اگر فایل موجود و معتبر باشد، یک تگ `<link rel="stylesheet">` در `<head>` صفحه تزریق می‌شود.
   - اگر تولید فایل با محدودیت دسترسی فایل‌سیستم روبه‌رو شود، کل CSS استخراج‌شده به صورت تگ اینلاین `<style id="elementor-post-{id}">` در بدنه تزریق می‌گردد.
4. **پیمایش بازگشتی درخت المان‌ها:**
   - متد `print_elements()` گره به گره عناصر را می‌خواند.
   - به ازای هر گره متدهای `before_render()` -> `render()` -> `after_render()` اجرا می‌شوند.
   - در صورت استفاده از تگ‌های داینامیک، متد `dynamic_tags->parse_tags_text()` قبل از رندر مقادیر را با دیتای زنده جایگزین می‌کند.
5. **بارگذاری شرطی کتابخانه‌های فرانت‌اند (Conditional Loading):**
   - اسکریپت‌ها و استایل‌های ویجت‌های فعال ثبت می‌شوند؛ اگر در صفحه‌ای هیچ ویجت اسلایدری وجود نداشته باشد، اسکریپت و استایل `swiper` هرگز انکیو نمی‌شود.
6. **اجرای ران‌تایم جاوااسکریپت فرانت‌اند:**
   - فایل `assets/js/frontend.min.js` اجرا و شیء سراسری `window.elementorFrontend` را می‌سازد.
   - برای هر ویجت رندر شده روی DOM، رویداد `frontend/element_ready/{widget_name}.default` فعال شده و کدهای جاوااسکریپت اختصاصی ویجت را اجرا می‌نماید.

---

## ۶. معماری ویرایشگر زنده (Editor Two-Frame Sandbox)

ویرایشگر زنده المنتور با دو پنجره مستقل اما هماهنگ کار می‌کند:
1. **Top Window (Admin Context):**
   - سایدبار تنظیمات، پنل انتخاب ویجت‌ها، ساختار درختی لایه‌ها (Navigator)، نوار بالایی (Top Bar) و تاریخچه ویرایش. این فریم با کتابخانه‌های React مدیریت می‌شود.
2. **Preview Iframe (Canvas Context):**
   - صفحه وب واقعی سایت کاربر که درون یک Iframe بارگذاری شده است.
3. **مکانیزم همگام‌سازی (Live Sync Protocol):**
   - وقتی کاربری در پنل چپ یک کنترل را تغییر می‌دهد:
     - برای تغییرات استایل (رنگ، فاصله): جاوااسکریپت بلافاصله تگ `<style id="elementor-preview-{id}">` را در Iframe آپدیت می‌کند (صفر میلی‌ثانیه تاخیر بدون لود صفحه).
     - برای تغییرات محتوا: متد تمپلیت جاوااسکریپت `content_template()` در کانوَس صدا زده شده و بدون درخواست به سرور، المان رندر می‌شود.
     - برای المان‌های سنگین سرور: درخواست ایجکس `elementor_ajax` با اکشن `render_widget` به سرور فرستاده می‌شود.
4. **سیستم ذخیره‌سازی:** با فشردن کلید انتشار، درخواست ایجکس `save_builder` داده‌های به‌روز درخت JSON را به سرور فرستاده و در متای `_elementor_data` ذخیره کرده و فایل‌های فیزیکی CSS را بازتولید می‌کند.
