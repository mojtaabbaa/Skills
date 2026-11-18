# کاتالوگ جامع ویجت‌ها و المان‌های هسته (Elementor Core Widgets Catalog)

این سند شامل فهرست کامل، دسته‌بندی‌شده و فنی تمام المان‌های موجود در **Elementor Core (4.2.3)** است.

---

## ۱. المان‌های ساختاری لایه‌بندی (Layout Elements)

| اسلاگ (`elType`) | عنوان | کلاس PHP | مسیر فایل سورس | کاربرد و ساختار |
| :--- | :--- | :--- | :--- | :--- |
| `container` | Container | `Container` | `elementor/includes/elements/container.php` | کانتینر نسل جدید بر پایه CSS Flexbox و CSS Grid؛ پشتیبانی از کانتینرهای تودرتوی نامحدود |
| `section` | Section | `Element_Section` | `elementor/includes/elements/section.php` | ساختار ردیف کلاسیک (نسل ۲) برای نگهداری ستون‌ها |
| `column` | Column | `Element_Column` | `elementor/includes/elements/column.php` | ستون‌های درونی سکشن که محتوا و ویجت‌ها در آن قرار می‌گیرند |

---

## ۲. ویجت‌های کلاسیک پایه و عمومی (Core Classic Widgets - ۳۴ ویجت)

### ۲.۱. ویجت‌های پایه (Basic Category)
این ویجت‌ها در دسته `basic` قرار دارند و برای ساختارهای اولیه متنی و بصری استفاده می‌شوند:

| اسلاگ ویجت | عنوان ویجت | کلاس PHP | مسیر فایل سورس | کتابخانه‌ها و وابستگی‌ها |
| :--- | :--- | :--- | :--- | :--- |
| `heading` | Heading | `Widget_Heading` | `elementor/includes/widgets/heading.php` | — |
| `image` | Image | `Widget_Image` | `elementor/includes/widgets/image.php` | — |
| `text-editor` | Text Editor | `Widget_Text_Editor` | `elementor/includes/widgets/text-editor.php` | ویرایشگر TinyMCE وردپرس |
| `video` | Video | `Widget_Video` | `elementor/includes/widgets/video.php` | YouTube, Vimeo, Dailymotion, Hosted |
| `button` | Button | `Widget_Button` | `elementor/includes/widgets/button.php` | — |
| `divider` | Divider | `Widget_Divider` | `elementor/includes/widgets/divider.php` | خطوط جداکننده SVG و CSS |
| `spacer` | Spacer | `Widget_Spacer` | `elementor/includes/widgets/spacer.php` | — |
| `google_maps` | Google Maps | `Widget_Google_Maps` | `elementor/includes/widgets/google-maps.php` | Google Maps Embed API |
| `icon` | Icon | `Widget_Icon` | `elementor/includes/widgets/icon.php` | کتابخانه‌های FontAwesome و SVG |
| `inner-section`| Inner Section | `Widget_Inner_Section`| `elementor/includes/widgets/inner-section.php` | بخش داخلی کلاسیک برای ستون‌های تودرتو |

---

### ۲.۲. ویجت‌های عمومی (General Category)
این ویجت‌ها در دسته `general` قرار داشته و المان‌های تعاملی و محتوایی غنی را می‌سازند:

| اسلاگ ویجت | عنوان ویجت | کلاس PHP | مسیر فایل سورس | وابستگی و قابلیت |
| :--- | :--- | :--- | :--- | :--- |
| `image-box` | Image Box | `Widget_Image_Box` | `elementor/includes/widgets/image-box.php` | ترکیب تصویر، عنوان و توضیحات |
| `icon-box` | Icon Box | `Widget_Icon_Box` | `elementor/includes/widgets/icon-box.php` | ترکیب آیکون با عنوان و لینک |
| `star-rating` | Star Rating | `Widget_Star_Rating` | `elementor/includes/widgets/star-rating.php` | ستاره‌های امتیازدهی اسکیما |
| `rating` | Rating | `Widget_Rating` | `elementor/includes/widgets/rating.php` | ریتینگ جدید با قابلیت آیکون‌های دلخواه |
| `image-carousel`| Image Carousel | `Widget_Image_Carousel`| `elementor/includes/widgets/image-carousel.php`| اسکریپت `swiper` |
| `image-gallery` | Basic Gallery | `Widget_Image_Gallery` | `elementor/includes/widgets/image-gallery.php` | گالری شبکه‌ای تصاویر وردپرس |
| `icon-list` | Icon List | `Widget_Icon_List` | `elementor/includes/widgets/icon-list.php` | لیست‌های آیکون‌دار تکی و افقی |
| `counter` | Counter | `Widget_Counter` | `elementor/includes/widgets/counter.php` | اسکریپت `jquery-numerator` |
| `progress` | Progress Bar | `Widget_Progress` | `elementor/includes/widgets/progress.php` | اسکریپت `waypoints` |
| `testimonial` | Testimonial | `Widget_Testimonial` | `elementor/includes/widgets/testimonial.php` | باکس رضایت مشتری با تصویر و نام |
| `tabs` | Tabs (Classic) | `Widget_Tabs` | `elementor/includes/widgets/tabs.php` | تب‌های کلاسیک عمودی و افقی |
| `accordion` | Accordion | `Widget_Accordion` | `elementor/includes/widgets/accordion.php` | آکاردئون متنی تا شونده |
| `toggle` | Toggle | `Widget_Toggle` | `elementor/includes/widgets/toggle.php` | تاگل‌های باز و بسته شونده مستقل |
| `social-icons` | Social Icons | `Widget_Social_Icons` | `elementor/includes/widgets/social-icons.php` | دکمه‌های سوشیال مدیا |
| `alert` | Alert | `Widget_Alert` | `elementor/includes/widgets/alert.php` | باکس هشدارهای رنگی با دکمه بستن |
| `audio` | SoundCloud | `Widget_Audio` | `elementor/includes/widgets/audio.php` | ساندکلاد امبد پلیر |
| `shortcode` | Shortcode | `Widget_Shortcode` | `elementor/includes/widgets/shortcode.php` | اجرای شورت‌کدهای وردپرس |
| `html` | HTML | `Widget_Html` | `elementor/includes/widgets/html.php` | کدهای خام HTML/JS/CSS |
| `menu-anchor` | Menu Anchor | `Widget_Menu_Anchor` | `elementor/includes/widgets/menu-anchor.php` | شناسه هدایت اسکرول نرم (ID) |
| `sidebar` | Sidebar | `Widget_Sidebar` | `elementor/includes/widgets/sidebar.php` | نمایش سایدبارهای پوسته وردپرس |
| `read-more` | Read More | `Widget_Read_More` | `elementor/includes/widgets/read-more.php` | دکمه ادامه مطلب برای برش متن آرشیو |
| `text-path` | Text Path | `TextPath` | `elementor/modules/shapes/widgets/text-path.php` | نوشتن متن روی مسیرهای برداری SVG |
| `contact-buttons`| Single Chat | `Contact_Buttons` | `elementor/modules/floating-buttons/widgets/...` | دکمه چت شناور در گوشه صفحه |
| `floating-bars-var-1`| Floating Bar CTA | `Floating_Bars_Var_1` | `elementor/modules/floating-buttons/widgets/...` | نوار بنر ثابت شناور در بالا یا پایین صفحه |
| `link-in-bio` | Minimalist | `Link_In_Bio` | `elementor/modules/link-in-bio/widgets/...` | صفحه فرود مینیمال لینک در بیو |

---

## ۳. ویجت‌های تودرتوی پیشرفته هسته (Nested Core Widgets)

این ویجت‌ها کلاس `Widget_Nested_Base` را ارث‌بری کرده و امکان درگ کردن کانتینرهای کامل به درون آیتم‌هایشان را فراهم می‌کنند:

| اسلاگ ویجت | عنوان ویجت | کلاس PHP | مسیر فایل سورس | ساختار محتوایی |
| :--- | :--- | :--- | :--- | :--- |
| `nested-tabs` | Tabs (Nested) | `NestedTabs` | `elementor/modules/nested-tabs/widgets/nested-tabs.php` | هر تب یک کانتینر آزاد و انعطاف‌پذیر فلکس‌باکس است که هر نوع ویجت دیگری می‌تواند در آن قرار گیرد |
| `nested-accordion`| Accordion (Nested)| `Nested_Accordion` | `elementor/modules/nested-accordion/widgets/nested-accordion.php`| هر آیتم آکاردئون شامل یک کانتینر مستقل با چیدمان کامل است |

---

## ۴. المان‌های اتمیک نسل ۴ هسته (Core Atomic Elements - ۱۹ المان)

المان‌های ساخته‌شده بر پایه معماری اتمیک V4 با کلاس پایه `Atomic_Widget_Base`، موتور قالب‌سازی Twig و پروپ‌های تایپ‌شده قوی:

| نوع المان (`e-*`) | عنوان نمایشی | کلاس PHP | مسیر فایل سورس | نقش در صفحه |
| :--- | :--- | :--- | :--- | :--- |
| `e-button` | Button | `Atomic_Button` | `modules/atomic-widgets/elements/atomic-button/atomic-button.php` | دکمه فوق‌سریع اتمیک با خروجی Twig و Markdown |
| `e-divider` | Divider | `Atomic_Divider` | `modules/atomic-widgets/elements/atomic-divider/atomic-divider.php` | جداکننده با استایل‌های Utility |
| `e-heading` | Heading | `Atomic_Heading` | `modules/atomic-widgets/elements/atomic-heading/atomic-heading.php` | تیتر با تایپوگرافی اتمیک |
| `e-image` | Image | `Atomic_Image` | `modules/atomic-widgets/elements/atomic-image/atomic-image.php` | المان تصویر با اندازه‌های استاندارد و لود بهینه |
| `e-paragraph` | Paragraph | `Atomic_Paragraph` | `modules/atomic-widgets/elements/atomic-paragraph/atomic-paragraph.php` | پاراگراف متنی تمیز بدون رپرهای اضافه |
| `e-self-hosted-video`| Video | `Atomic_Self_Hosted_Video` | `modules/atomic-widgets/elements/atomic-self-hosted-video/...` | پلیر سبک ویدیوهای لوکال با HTML5 Video |
| `e-svg` | SVG | `Atomic_Svg` | `modules/atomic-widgets/elements/atomic-svg/atomic-svg.php` | وکتورهای برداری با استایل‌دهی رنگ Fill و Stroke |
| `e-youtube` | YouTube | `Atomic_Youtube` | `modules/atomic-widgets/elements/atomic-youtube/atomic-youtube.php` | پلیر سبک و بهینه یوتیوب با Lazy Load |
| `e-tabs` | Tabs Container | `Atomic_Tabs` | `modules/atomic-widgets/elements/atomic-tabs/atomic-tabs/...` | ظرف کلی تب‌های اتمیک |
| `e-tab` | Tab Trigger | `Atomic_Tab` | `modules/atomic-widgets/elements/atomic-tabs/atomic-tab/...` | دکمه فعال‌کننده هر تب |
| `e-tab-content` | Tab Content | `Atomic_Tab_Content` | `modules/atomic-widgets/elements/atomic-tabs/atomic-tab-content/...` | کانتینر محتوای هر تب |
| `e-tabs-menu` | Tabs Menu | `Atomic_Tabs_Menu` | `modules/atomic-widgets/elements/atomic-tabs/atomic-tabs-menu/...` | نوار ناوبری دکمه‌های تب‌ها |
| `e-tabs-content-area`| Tabs Content Area | `Atomic_Tabs_Content_Area` | `modules/atomic-widgets/elements/atomic-tabs/atomic-tabs-content-area/...` | محدوده رندر محتوای تب فعال |
| `e-div-block` | Div Block | `Div_Block` | `modules/atomic-widgets/elements/div-block/div-block.php` | بلوک خام `<div>` برای چیدمان‌های بدون بار اضافه |
| `e-flexbox` | Flexbox | `Flexbox` | `modules/atomic-widgets/elements/flexbox/flexbox.php` | کانتینر فلکس‌باکس خالص اتمیک |
| `e-grid` | Grid | `Grid` | `modules/atomic-widgets/elements/grid/grid.php` | گرید دوبعدی با تنظیمات مستقیم ستون و ردیف |
| `e-component` | Component Instance | `Component_Instance` | `modules/components/widgets/component-instance.php` | فراخوانی کامپوننت‌های قابل‌استفاده مجدد (Components) |
| `e-form-error-message`| Error message | `Form_Error_Message` | `modules/atomic-widgets/elements/atomic-form/...` | پیام خطای اعتبارسنجی فرم‌ها |
| `e-form-success-message`| Success message | `Form_Success_Message` | `modules/atomic-widgets/elements/atomic-form/...` | پیام موفقیت ارسال فرم‌ها |
