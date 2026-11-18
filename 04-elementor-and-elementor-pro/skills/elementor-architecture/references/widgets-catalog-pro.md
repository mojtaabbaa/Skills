# کاتالوگ جامع ویجت‌ها و المان‌های المنتور پرو (Elementor Pro Widgets Catalog)

این سند شامل فهرست کامل، دسته‌بندی‌شده و فنی تمامی ویجت‌ها و المان‌های موجود در **Elementor Pro (4.3.2)** است.

---

## ۱. ویجت‌های قالب‌ساز پوسته (Theme Builder & Site Elements - ۱۶ ویجت)

این ویجت‌ها برای طراحی هدر، فوتر، صفحات تکی پست/برگه، صفحات آرشیو، صفحه ۴۰۴ و نتایج جستجو استفاده می‌شوند:

| اسلاگ ویجت | عنوان ویجت | کلاس PHP | مسیر فایل سورس | دسته‌بندی | قابلیت‌ها و جزئیات |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `theme-post-title` | Post Title | `Post_Title` | `modules/theme-builder/widgets/post-title.php` | `theme-elements-single` | عنوان داینامیک پست؛ تگ‌های H1 تا H6؛ کلاس خودکار `entry-title` |
| `post-content` | Post Content | `Post_Content` | `modules/theme-builder/widgets/post-content.php` | `theme-elements-single` | رندر محتوای ویرایشگر برگه یا مقاله با فیلتر کامل `the_content` |
| `post-excerpt` | Post Excerpt | `Post_Excerpt` | `modules/theme-builder/widgets/post-excerpt.php` | `theme-elements-single` | چکیده مقاله با کنترل تعداد کلمات و کاراکتر ادامه مطلب |
| `post-featured-image`| Featured Image | `Post_Featured_Image`| `modules/theme-builder/widgets/post-featured-image.php`| `theme-elements-single` | تصویر شاخص پست؛ سازگار با لایت‌باکس و لینک به پست یا مدیا |
| `author-box` | Author Box | `Author_Box` | `modules/theme-elements/widgets/author-box.php` | `theme-elements-single` | نام نویسنده، آواتار گراواتار، بیوگرافی و لینک بایگانی مقالات |
| `post-comments` | Post Comments | `Post_Comments` | `modules/theme-elements/widgets/post-comments.php` | `theme-elements-single` | فرم و لیست نظرات بومی وردپرس با استایل‌دهی کامل فیلدها |
| `post-info` | Post Info | `Post_Info` | `modules/theme-elements/widgets/post-info.php` | `theme-elements-single` | متادیتای پست (تاریخ، ساعت انتشار، دسته‌ها، تگ‌ها، تعداد نظرات) |
| `post-navigation` | Post Navigation | `Post_Navigation` | `modules/theme-elements/widgets/post-navigation.php` | `theme-elements-single` | دکمه‌های ناوبری پست قبلی/بعدی در همان دسته یا کل وبلاگ |
| `archive-title` | Archive Title | `Archive_Title` | `modules/theme-builder/widgets/archive-title.php` | `theme-elements-archive` | عنوان صفحه آرشیو (نام دسته، برچسب، نویسنده یا تاریخ) |
| `archive-posts` | Archive Posts | `Archive_Posts` | `modules/theme-builder/widgets/archive-posts.php` | `theme-elements-archive` | شبکه مقالات مطابق با کوئری صفحه آرشیو جاری |
| `site-logo` | Site Logo | `Site_Logo` | `modules/theme-builder/widgets/site-logo.php` | `theme-elements` | لوگوی سایت با لینک اتوماتیک به صفحه اصلی سایت |
| `site-title` | Site Title | `Site_Title` | `modules/theme-builder/widgets/site-title.php` | `theme-elements` | عنوان متنی وبلاگ از تنظیمات عمومی وردپرس |
| `page-title` | Page Title | `Page_Title` | `modules/theme-builder/widgets/page-title.php` | `theme-elements-single` | عنوان برگه جاری |
| `search-form` | Search Form | `Search_Form` | `modules/theme-elements/widgets/search-form.php` | `theme-elements` | فرم جستجوی زنده در حالت‌های Classic, Full Screen, Minimal |
| `sitemap` | Sitemap | `Sitemap` | `modules/theme-elements/widgets/sitemap.php` | `theme-elements` | نقشه کامل وب‌سایت شامل صفحات، مقالات و طبقه‌بندی‌ها |
| `breadcrumbs` | Breadcrumbs | `Breadcrumbs` | `modules/theme-elements/widgets/breadcrumbs.php` | `theme-elements` | مسیر راهنمای کاربر سازگار با سئوی Yoast و RankMath |

---

## ۲. ویجت‌های بازاریابی، تعامل و تبدیل (Marketing & Lead Gen - ۱۵ ویجت)

| اسلاگ ویجت | عنوان ویجت | کلاس PHP | مسیر فایل سورس | دسته‌بندی | اکشن‌ها و ویژگی‌ها |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `form` | Form | `Form` | `modules/forms/widgets/form.php` | `pro-elements` | فرم‌ساز با ثبت در پایگاه لیدها (`e_submissions`)، وب‌هوک، ایمیل، میل‌چیمپ، ریدایرکت، ریکپچا |
| `login` | Login | `Login` | `modules/forms/widgets/login.php` | `pro-elements` | فرم ورود کاربران با لینک فراموشی رمز و هدایت دلخواه بعد از لاگین |
| `animated-headline`| Animated Headline| `Animated_Headline`| `modules/animated-headline/widgets/animated-headline.php`| `pro-elements` | تیترهای چرخشی (Rotating) و هایلایت دست‌نویس (Highlighted SVG) |
| `price-list` | Price List | `Price_List` | `modules/pricing/widgets/price-list.php` | `pro-elements` | منوی رستوران و لیست قیمت کاتالوگی با تصویر و خط‌چین |
| `price-table` | Price Table | `Price_Table` | `modules/pricing/widgets/price-table.php` | `pro-elements` | جدول تعرفه پلن‌ها با فیچرهای چک‌خورده، ریبون محبوب و CTA |
| `flip-box` | Flip Box | `Flip_Box` | `modules/flip-box/widgets/flip-box.php` | `pro-elements` | کارت دوروی تعاملی با انیمیشن‌های سه‌بعدی Flip هنگام هاور |
| `call-to-action` | Call to Action | `Call_To_Action` | `modules/call-to-action/widgets/call-to-action.php` | `pro-elements` | بنر دعوت به اقدام با ترکیب تصویر، ریبون تخفیف و دکمه |
| `countdown` | Countdown | `Countdown` | `modules/countdown/widgets/countdown.php` | `pro-elements` | تایمر معکوس موعد مشخص یا چرخه بی‌پایان (Evergreen) با اکشن انقضا |
| `share-buttons` | Share Buttons | `Share_Buttons` | `modules/share-buttons/widgets/share-buttons.php` | `pro-elements` | دکمه‌های اشتراک‌گذاری در شبکه‌های اجتماعی بدون اسکریپت خارجی سنگین |
| `lottie` | Lottie | `Lottie` | `modules/lottie/widgets/lottie.php` | `pro-elements` | رندر انیمیشن‌های وکتور سبک Lottie با کنترل اسکرول، هاور و کلیک |
| `paypal-button` | PayPal Button | `Paypal_Button` | `modules/payments/widgets/paypal-button.php` | `pro-elements` | دکمه پرداخت آنلاین سریع پی‌پال برای خرید محصول یا دونیت |
| `stripe-button` | Stripe Button | `Stripe_Button` | `modules/payments/widgets/stripe-button.php` | `pro-elements` | اتصال مستقیم به درگاه بانکی بین‌المللی کارت اعتباری استرایپ |
| `media-carousel` | Media Carousel | `Media_Carousel` | `modules/carousel/widgets/media-carousel.php` | `pro-elements` | اسلایدر تصویر و ویدیو با افکت‌های ۳ بعدی Coverflow و Cube |
| `reviews` | Reviews | `Reviews` | `modules/carousel/widgets/reviews.php` | `pro-elements` | اسلایدر نظرات مشتریان به سبک کارت‌های شبکه‌های اجتماعی |
| `testimonial-carousel`| Testimonial Carousel| `Testimonial_Carousel`| `modules/carousel/widgets/testimonial-carousel.php`| `pro-elements` | اسلایدر رضایت مشتریان با آواتار و ستاره‌های امتیاز |

---

## ۳. ویجت‌های پویای محتوا، لوپ و مدیا (Dynamic Content, Loop & Media - ۱۴ ویجت)

| اسلاگ ویجت | عنوان ویجت | کلاس PHP | مسیر فایل سورس | قابلیت‌ها |
| :--- | :--- | :--- | :--- | :--- |
| `posts` | Posts | `Posts` | `modules/posts/widgets/posts.php` | نمایش مقالات با پوسته‌های Classic و Cards و صفحه‌بندی ایجکس بدون ریلود |
| `portfolio` | Portfolio | `Portfolio` | `modules/posts/widgets/portfolio.php` | گالری نمونه‌کارها همراه با تب‌های فیلتر ایجکس بر اساس دسته‌ها |
| `loop-grid` | Loop Grid | `Loop_Grid` | `modules/loop-builder/widgets/loop-grid.php` | چیدمان شبکه‌ای پست‌ها یا محصولات با تمپلیت طراحی‌شده در Loop Item |
| `loop-carousel` | Loop Carousel | `Loop_Carousel` | `modules/loop-builder/widgets/loop-carousel.php` | کروسل متحرک پست‌ها بر پایه تمپلیت سفارشی لوپ آیتم |
| `taxonomy-filter` | Taxonomy Filter | `Taxonomy_Filter` | `modules/loop-filter/widgets/taxonomy-filter.php` | فیلتر ایجکس زنده برای دسته‌ها و برچسب‌های لوپ گرید |
| `gallery` | Gallery (Pro) | `Gallery` | `modules/gallery/widgets/gallery.php` | گالری چندتبی با حالت‌های گرید، جاستیفای (Justified) و ماسونری (Masonry) |
| `slides` | Slides | `Slides` | `modules/slides/widgets/slides.php` | اسلایدر بنری هیرو با انیمیشن زوم Ken Burns و محتوای سفارشی |
| `hotspot` | Hotspot | `Hotspot` | `modules/hotspot/widgets/hotspot.php` | نقاط قابل کلیک و تپ روی تصویر با تول‌تیپ‌های تعاملی |
| `table-of-contents`| Table of Contents| `Table_Of_Contents`| `modules/table-of-contents/widgets/table-of-contents.php`| فهرست عناوین خودکار بر اساس تگ‌های هدینگ محتوا (H2-H6) |
| `code-highlight` | Code Highlight | `Code_Highlight` | `modules/code-highlight/widgets/code-highlight.php`| نمایش کدهای برنامه‌نویسی با پشتیبانی از کتابخانه Prism.js |
| `video-playlist` | Video Playlist | `Video_Playlist` | `modules/video-playlist/widgets/video-playlist.php`| لیست پخش ویدیوهای یوتیوب یا هاست شخصی با سرفصل و مدت زمان |
| `blockquote` | Blockquote | `Blockquote` | `modules/blockquote/widgets/blockquote.php` | نقل‌قول اختصاصی همراه با دکمه مستقیم انتشار در توییتر |
| `aparat` | Aparat Video | `AparatVideo` | `modules/aparat-video/widgets/aparat-video.php` | پلیر رسمی و بهینه ویدیوهای آپارات با آی‌دی ویدیو |

---

## ۴. ناوبری پیشرفته، المان‌های تودرتو و شناور پرو (Navigation & Floating - ۲۲ ویجت)

| اسلاگ ویجت | عنوان ویجت | کلاس PHP | مسیر فایل سورس | نوع و کارکرد |
| :--- | :--- | :--- | :--- | :--- |
| `nav-menu` | WordPress Menu | `Nav_Menu` | `modules/nav-menu/widgets/nav-menu.php` | منوی استاندارد وردپرس با کتابخانه SmartMenus |
| `mega-menu` | Mega Menu | `Mega_Menu` | `modules/mega-menu/widgets/mega-menu.php` | منوی مگای تودرتو (هر آیتم منو شامل یک کانتینر فرزند کامل است) |
| `nested-carousel` | Nested Carousel | `Nested_Carousel` | `modules/nested-carousel/widgets/nested-carousel.php` | اسلایدر تودرتو؛ هر اسلاید یک کانتینر آزاد برای چیدمان دلخواه |
| `off-canvas` | Off Canvas | `Off_Canvas` | `modules/off-canvas/widgets/off-canvas.php` | پنل کشویی کناری با کانتینر درونی و تریگرهای متنوع |
| `progress-tracker` | Progress Tracker | `Progress_Tracker` | `modules/progress-tracker/widgets/progress-tracker.php` | نوار پیشرفت مطالعه مقاله بر اساس اسکرول |
| `template` | Template | `Template` | `modules/library/widgets/template.php` | فراخوانی هر تمپلیت یا سکشن ذخیره‌شده در کتابخانه المنتور |
| `global` | Global Widget | `Global_Widget` | `modules/global-widget/widgets/global-widget.php` | رپر ویجت‌های گلوبال؛ ویرایش یکباره و اعمال در کل صفحات |
| `contact-buttons-var-1..10`| 10 Contact Vars | `Contact_Buttons_Var_*`| `modules/floating-buttons/widgets/...` | متغیرهای دکمه‌های پیام‌رسان‌های واتساپ، تلگرام و تماس |
| `floating-bars-var-2..3` | Floating Bars Vars | `Floating_Bars_Var_*` | `modules/floating-buttons/widgets/...` | نوارهای تخفیف و اعلانات شناور ثابت در بالا یا پایین ویوپورت |
| `link-in-bio-var-2..7` | Link in Bio Vars | `Link_In_Bio_Var_*` | `modules/link-in-bio/widgets/...` | استایل‌های تجاری صفحات فرود اینستاگرام و شبکه‌های اجتماعی |
| `facebook-button..page` | Facebook Suite | `Facebook_*` | `modules/social/widgets/...` | مجموعه ویجت‌های لایک، دیدگاه‌ها، امبد و صفحه فیسبوک |

---

## ۵. ویجت‌های اختصاصی فروشگاه‌ساز ووکامرس (WooCommerce Pro - ۳۰ ویجت)

### ۵.۱. صفحه تک محصولی (Single Product - ۱۴ ویجت)
1. `woocommerce-product-title`: عنوان محصول با استایل‌دهی و لینک.
2. `woocommerce-product-images`: تصویر و گالری محصول با زوم و لایت‌باکس FlexSlider.
3. `woocommerce-product-price`: قیمت جاری، قیمت حراج و پسوندهای قیمت.
4. `woocommerce-product-add-to-cart`: فرم خرید استاندارد و انتخاب ویژگی‌های محصولات متغیر.
5. `wc-add-to-cart`: دکمه سفارشی افزودن به سبد خرید.
6. `woocommerce-product-rating`: ستاره‌های امتیاز و شمارنده دیدگاه‌های تاییدشده.
7. `woocommerce-product-stock`: وضعیت موجودی انبار با استایل‌های اختصاصی.
8. `woocommerce-product-meta`: اطلاعات شناسنامه محصول (کد SKU، دسته‌ها، تگ‌ها).
9. `woocommerce-product-data-tabs`: تب‌های استاندارد ووکامرس (توضیحات، نقد و بررسی، مشخصات).
10. `woocommerce-product-short-description`: توضیح کوتاه کنار محصول.
11. `woocommerce-product-additional-information`: جدول ویژگی‌ها و ابعاد کالا.
12. `woocommerce-product-related`: شبکه هوشمند محصولات مرتبط.
13. `woocommerce-product-upsell`: محصولات تشویقی فروش بیشتر (Upsells).
14. `woocommerce-product-content`: محتوای تفصیلی توضیحات کامل محصول.

### ۵.۲. آرشیو فروشگاه و دسته‌بندی‌ها (Shop & Archive - ۷ ویجت)
15. `woocommerce-products` / `wc-products`: شبکه ویترین محصولات با کوئری‌های پیشرفته دستی یا خودکار.
16. `woocommerce-archive-products` / `wc-archive-products`: نمایش محصولات منطبق با آرشیو فعلی همراه با منوی مرتب‌سازی.
17. `woocommerce-archive-description`: توضیحات متنی بالای دسته محصولات.
18. `wc-categories`: نمایش شبکه‌ای دسته‌بندی‌های محصولات با تصویر و شمارنده تعداد کالا.
19. `woocommerce-category-image`: تصویر شاخص دسته‌بندی ووکامرس.
20. `wc-elements`: پیج‌های سیستمی ووکامرس.
21. `wc-single-elements`: المان‌های تک‌منظوره فروشگاه.

### ۵.۳. فرآیند خرید، سبد و تسویه‌حساب (Cart, Checkout & Account - ۹ ویجت)
22. `woocommerce-cart`: صفحه سبد خرید مدرن دو ستونه با اعمال کوپن و محاسبه هزینه ارسال.
23. `woocommerce-checkout-page`: فرم تسویه‌حساب اختصاصی مرحله‌ای یا یک‌صفحه‌ای.
24. `woocommerce-my-account`: داشبورد کامل حساب کاربری با تب‌های سفارشات، آدرس‌ها و خروج.
25. `woocommerce-menu-cart`: آیکون سبد خرید در هدر با پنجره شناور محتویات مینی‌کارت.
26. `woocommerce-notices`: مکان نمایش پیام‌های سیستم ووکامرس (پیام افزوده‌شدن به سبد، خطاها).
27. `woocommerce-purchase-summary`: برگه تشکر و جزئیات فاکتور نهایی پس از پرداخت موفق.
28. `woocommerce-breadcrumb`: مسیر خرده‌نانی فروشگاهی ووکامرس.

---

## ۶. المان‌های اتمیک پرو (Pro Atomic Elements - ۱۱ المان)

المان‌های اتمیک نسل ۴ برای فرم‌سازی و حلقه‌های تکرار با لود فوق‌سریع:

| نوع المان (`e-*`) | عنوان | کلاس PHP | مسیر فایل سورس | کاربرد |
| :--- | :--- | :--- | :--- | :--- |
| `e-form-input` | Input | `Input` | `modules/atomic-form/input/input.php` | اینپوت‌های متنی، ایمیل، شماره تلفن و رمز عبور |
| `e-form-textarea` | Text area | `Textarea` | `modules/atomic-form/textarea/textarea.php` | فیلد متنی چندخطی پیام کاربران |
| `e-form-select` | Select | `Select` | `modules/atomic-form/select/select.php` | دراپ‌داون انتخاب گزینه‌ها |
| `e-form-checkbox` | Checkbox | `Checkbox` | `modules/atomic-form/checkbox/checkbox.php` | چک‌باکس‌های شرایط و انتخاب‌های چندتایی |
| `e-form-radio-button`| Radio button | `Radio_Button` | `modules/atomic-form/radio-button/radio-button.php` | دکمه‌های رادیویی انتخاب تک‌گزینه‌ای |
| `e-form-submit-button`| Submit button | `Submit_Button` | `modules/atomic-form/submit-button/submit-button.php` | دکمه ارسال فرم با لودینگ آیکون اتمیک |
| `e-form-file-upload` | File Upload | `File_Upload` | `modules/atomic-form/file-upload/file-upload.php` | آپلود فایل با اعتبارسنجی حجم و پسوند مجاز |
| `e-form-date-picker` | Date picker | `Date_Picker` | `modules/atomic-form/date-picker/date-picker.php` | انتخاب‌گر تاریخ با تقویم اتمیک |
| `e-form-time-picker` | Time picker | `Time_Picker` | `modules/atomic-form/time-picker/time-picker.php` | انتخاب‌گر زمان |
| `e-form-label` | Label | `Label` | `modules/atomic-form/label/label.php` | برچسب فیلد متصل به شناسه اینپوت |
| `collection-loop` | Collection Loop | `Collection_Loop` | `modules/collection-loop/elements/...` | حلقه داینامیک اتمیک V4 با کارایی بالا در رندرینگ |
