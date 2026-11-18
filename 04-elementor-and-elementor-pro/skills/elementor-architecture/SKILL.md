---
name: elementor-architecture
description: >-
  Complete global engineering memory, architectural blueprints, widgets catalog, internal APIs,
  and 12 categorized development rulebooks for Elementor Core (v4.2.3+) and Elementor Pro (v4.3.2+).
  Enforces strict 0-to-100 lifecycle graph, 3 development paradigms (Classic, Nested, Atomic V4),
  and the mandatory Source Code Fallback Directive whenever an entity is unrecognized.
---

# حافظه گلوبال مهندسی و معماری المنتور (Elementor & Elementor Pro Architecture Master Skill)

این مهارت (Skill) پایگاه دانش مرجع، قطعی و دائمی مهندسی **Elementor Core (4.2.3)** و **Elementor Pro (4.3.2)** است که مستقیماً بر اساس تحلیل خط‌به‌خط سورس‌کد (۲۴۳۱ فایل PHP، ۱۰۰۹ فایل JS/TS، ۲۱۸۹ کلاس و ۲۶۴ فیلتر و ۱۸۹ اکشن) استخراج و مدلسازی شده است.

---

> [!CAUTION]
> ## 🚨 دستورالعمل بنیادین و الزامی: بازگشت مستقیم به سورس‌کد (The Source Fallback Directive)
> 
> **در صورت عدم شناسایی، ابهام یا نبود مستندات برای هر تابع، متد، کلاس، هوک یا کنترل:**
> عامل هوش مصنوعی تحت هیچ شرایطی نباید حدس بزند یا بر اساس فرضیات کد تولید کند. **عامل موظف و متعهد است مستقیماً به سورس‌کد افزونه در مسیرهای زیر مراجعه کرده و فایل مربوطه را خط‌به‌خط مطالعه کند:**
> * سورس‌کد هسته: `elementor/`
> * سورس‌کد پرو: `elementor-pro/`
> 
> سورس‌کد همواره مرجع نهایی و حقیقت قطعی است.

---

> [!IMPORTANT]
> **قانون عدم تداخل با سایر حافظه‌ها (Zero-Conflict Isolation):**
> این مهارت مرجع یکپارچه و گلوبال مهندسی **Elementor Core (v4.2.3+) و Elementor Pro (v4.3.2+)** است و بدون هیچ‌گونه تداخل در کنار `wordpress-master`، `seo-master`، `design-master`، `engineering-master` و اسکیل‌های محلی برند هر ورک‌اسپیس (`.agents/skills/brand-*/SKILL.md`) عمل می‌کند.
> **هسته مرجع = تحلیل مستقیم سورس‌کد (بخش‌های ۱، ۲ و ۳ زیر)**؛ و **بخش ۴ (`extensions/` و `scripts/`)** گپ‌های عملیاتی تولید JSON AST، بویلرپلیت‌های PHP، الگوهای ادیتوریال و انتشار اتمیک MCP/REST را پر می‌کند.

---

## ۱. گراف مهندسی صفر تا صد معماری (0-to-100 Graph)

📊 **[مشاهده نقشه و گراف کامل صفر تا صد: graph-zero-to-hundred.md](./references/graph-zero-to-hundred.md)**
شامل دیاگرام‌های کامل مراحل ۳۶ گانه از `plugins_loaded` وردپرس، بوت‌استرپ هسته، لود ماژول‌های ۶۸ گانه پرو، پایپ‌لاین رندرینگ بازگشتی، کشینگ CSS، ساندباکس ادیتور، تا جداول اختصاصی دیتابیس.

---

## ۲. دوازده فایل قوانین تفکیک‌شده بر اساس دسته‌بندی (12 Categorized Rulebooks)

برای هر بخش معماری، یک فایل قوانین تخصصی با ضوابط کدنویسی، الگوهای ممنوعه و الزامات امنیتی تدوین شده است:

| # | دسته‌بندی قوانین | فایل رفرنس قوانین | موضوع و حیطه نظارت |
| :-: | :--- | :--- | :--- |
| **۱** | چرخه حیات و بوت‌استرپ | **[01-rules-core-bootstrap-lifecycle.md](./rules/01-rules-core-bootstrap-lifecycle.md)** | زمان‌بندی لود، اتولودر، شیء Singleton، دسترسی به ۴۰ منیجر هسته |
| **۲** | ساختار لایه‌بندی و المان‌ها | **[02-rules-layout-and-elements.md](./rules/02-rules-layout-and-elements.md)** | کانتینرهای فلکس‌باکس و گرید، سکشن‌ها، بهینه‌سازی عمق DOM، المان‌های اتمیک |
| **۳** | موتور ویجت‌ها و پارادایم‌ها | **[03-rules-widgets-engine-and-paradigms.md](./rules/03-rules-widgets-engine-and-paradigms.md)** | قوانین ویجت‌های کلاسیک (`Widget_Base`)، تودرتو (`Widget_Nested_Base`) و اتمیک (`Atomic_Widget_Base`) |
| **۴** | کنترل‌ها و موتور استایل | **[04-rules-controls-and-styling-engine.md](./rules/04-rules-controls-and-styling-engine.md)** | توکن الزامی `{{WRAPPER}}`، ۴۲ کنترل UI، کنترل‌های گروهی، نقاط شکست واکنش‌گرا |
| **۵** | ذخیره‌سازی و دیتابیس | **[05-rules-data-storage-and-schema.md](./rules/05-rules-data-storage-and-schema.md)** | اسکیما و متای `_elementor_data`، جداول لیدها (`wp_e_submissions`) و کش استایل |
| **۶** | ادیتور زنده و پیش‌نمایش | **[06-rules-editor-and-live-preview.md](./rules/06-rules-editor-and-live-preview.md)** | ساندباکس Top Window و Preview Iframe، پروتکل PostMessage، متد `content_template` |
| **۷** | فرانت‌اند و مدیریت است‌ها | **[07-rules-frontend-runtime-and-assets.md](./rules/07-rules-frontend-runtime-and-assets.md)** | انکیو شرطی (`get_script_depends`)، شیء `elementorFrontend`، ایونت‌باس |
| **۸** | پوسته ساز و پاپ‌آپ | **[08-rules-pro-theme-builder-and-popup.md](./rules/08-rules-pro-theme-builder-and-popup.md)** | لوکیشن‌های قالب، ارزیابی شروط نمایش (Display Conditions)، تریگرها و تایمینگ پاپ‌آپ |
| **۹** | فرم‌ساز و بازاریابی | **[09-rules-pro-forms-and-marketing.md](./rules/09-rules-pro-forms-and-marketing.md)** | خط لوله ارسال فرم، وب‌هوک‌ها، اکشن‌های سفارشی، درگاه‌های پرداخت، فرم اتمیک V4 |
| **۱۰** | فروشگاه‌ساز ووکامرس | **[10-rules-pro-woocommerce-and-ecommerce.md](./rules/10-rules-pro-woocommerce-and-ecommerce.md)** | ۳۰ ویجت تخصصی تک‌محصولی، آرشیو، سبد خرید، تسویه‌حساب و فرگمنت‌های مینی‌کارت |
| **۱۱** | لوپ‌ها و موتور داده‌های پویا | **[11-rules-pro-loops-and-dynamic-engine.md](./rules/11-rules-pro-loops-and-dynamic-engine.md)** | لوپ گرید و کروسل، فیلتر زنده تاکسونومی، تمپلیت‌های آلترناتیو، ۵۸ تگ داینامیک |
| **۱۲** | هوک‌های توسعه و فال‌بک سورس | **[12-rules-developer-extensibility-and-fallbacks.md](./rules/12-rules-developer-extensibility-and-fallbacks.md)** | هوک‌های ثبت، تزریق کنترل (`before_section_end`)، فیلتر رندر و دستورالعمل الزام سورس |

---

## ۳. مستندات تفصیلی و کاتالوگ ویجت‌ها (Reference Catalogs)

1. 📄 **[معماری هسته، بوت‌استرپ و سیستم داده](./references/core-architecture.md)**
2. 📄 **[کالبدشکافی ویجت‌ها و الگوهای توسعه](./references/widget-paradigms-and-rules.md)**
3. 📄 **[کاتالوگ کامل ویجت‌ها و المان‌های هسته (۴۱ ویجت + ۱۹ المان اتمیک)](./references/widgets-catalog-core.md)**
4. 📄 **[کاتالوگ کامل ویجت‌ها و المان‌های پرو (۱۰۰+ ویجت + ۱۱ المان اتمیک)](./references/widgets-catalog-pro.md)**
5. 📄 **[مرجع هوک‌ها و APIهای توسعه‌دهندگان](./references/hooks-and-developer-api.md)**

---

## ۴. افزونه‌های عملیاتی پرکننده گپ (Production Extensions & CLI Scripts)

این بخش بر پایه هسته سورس‌کد v4.2.3/v4.3.2 سوار شده و گپ‌های عملیاتی استخراج‌شده از پروژه‌ها (با حذف هاردکد برندها و اصلاح باگ‌ها) را پوشش می‌دهد:

| # | افزونه عملیاتی | فایل | کاربرد کلیدی |
| :-: | :--- | :--- | :--- |
| **۱** | اسکیما JSON AST و تله‌های کنترل‌ها | **[01-json-ast-and-controls-schema.md](./extensions/01-json-ast-and-controls-schema.md)** | Flattening تب‌ها، قانون پیشوند کانتینر در برابر ویجت (`_margin`)، تله **`image_border_radius`**، `__dynamic__`/`__globals__`، اسکیما JSON ویجت‌های تعاملی و WoodMart |
| **۲** | بویلرپلیت‌های آماده توسعه‌دهندگان Pro | **[02-pro-developer-php-recipes.md](./extensions/02-pro-developer-php-recipes.md)** | کدهای PHP آماده `Widget_Base`، `DynamicTags\Tag`، `Forms\Action_Base`، `elementor/query/{id}`، `elementor_theme_do_location`، Loop Builder و `elementorFrontend.hooks` |
| **۳** | ۱۳ الگوی ادیتوریال و انتشار اتمیک MCP/REST | **[03-editorial-patterns-and-mcp-publish.md](./extensions/03-editorial-patterns-and-mcp-publish.md)** | قانون Anti-HTML-Dump، ۱۳ الگوی Brand-Agnostic، **۷ گناه کبیره AST** و **پروتکل ۳مرحله‌ای ایمن قفل‌گشایی `_elementor_edit_mode`** + پاکسازی کش |
| **۴** | تطبیق قالب‌ها، DOM و کش | **[04-theme-and-cache-integration.md](./extensions/04-theme-and-cache-integration.md)** | Astra / Hello Elementor / WoodMart، مالکیت DOM و CLS، بازنصب Idempotent در AJAX، خطرات WP Rocket RUCSS و Autoptimize |

### ابزارهای خط فرمان (Scripts)
- **`scripts/inspect_widget.py`:** استخراج مستقیم کنترل‌های هر ویجت از سورس‌کد واقعی Elementor v4.2.3 و Elementor Pro v4.3.2.
- **`extensions/05-acf-woocommerce-and-validation.md`:** ادغام بومی ACF Dynamic Tags (`__dynamic__`) و WooCommerce HPOS، محدودیت‌های تاییدشده سورس + پروتکل استثنا، چک‌لیست ۵مرحله‌ای QA و بویلرپلیت‌های PHP در `references/sample-php/`.
- **`scripts/article_to_elementor.py`:** کامپایلر Brand-Agnostic برای تولید `_elementor_data` منطبق با ۷ گناه کبیره (بدون H1 تکراری، CTA تک‌ستونه، احترام به ZWNJ هر برند).
