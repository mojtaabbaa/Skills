# Engine 03: Content Strategy, Hub-and-Spoke Clusters & Anti-Cannibalization

Use this engine when planning editorial calendars, mapping keyword/GSC exports to URL tiers, resolving cannibalization, or preparing writer-ready content briefs. Load the target `brand-<project>` skill first to check verified existing URLs and avoid duplicating published topics.

---

## 1. Tiered URL Ownership Decision Tree (Which Page Wins?)

| Tier | Page Role | Search Intent Owned | Rules |
| :--- | :--- | :--- | :--- |
| **Tier 1: Homepage** | Brand & broad store/city head terms | Broad brand or primary service/shop intent | Never create a separate blog or duplicate landing competing with `/` |
| **Tier 1B: Dedicated Hub / Price / Service Page** | Live pricing hubs, core service hubs, calculators | High-intent transactional/utility queries | Receives upward links from blogs and categories; zero off-topic tutorials |
| **Tier 2: Brand & Category Archives** | Group/brand commercial browsing & price intent | `خرید/قیمت + دسته/برند` | Keep bottom text concise & buying-focused; condense deep guides into 1-paragraph links UP/OUT |
| **Tier 3: Product PDPs** | Specific SKU / model / cut purchase | Exact product buying queries | One canonical SKU per intent; differentiate color/variant codes cleanly |
| **Tier 4: Blog Cluster (Hub & Spoke)** | Top/mid-funnel educational, how-to, authenticity, troubleshooting, nutrition, comparison | Informational & commercial investigation | Check `brand-*` verified published URLs first! If already published, route to Engine 04 (Refresh) instead of creating a duplicate post |

---

## 2. Two-Sheet Keyword Triage Standard (`کلمات مرتبط` vs. `حذف شده`)

Raw Iranian SEO tool / GSC exports frequently mix valid demand with junk noise. Always filter through these 5 gates before assigning keywords:
1. **Out-of-Scope / Junk Noise (`حذف شده — نامرتبط`):** Unrelated products, unstocked items, or random unrelated SERP queries.
2. **Wrong Geographic City (`حذف شده — شهر غیرمرتبط`):** Queries targeting other cities where the business does not serve locally (never target on local landing pages).
3. **Outdated Year Strings (`حذف شده — تاریخ منقضی`):** Stale years (`۱۴۰۰`, `۲۰۲۲`).
4. **Cross-Page Intent Collision (`حذف شده — تداخل اینتنت / کنیبالیزیشن`):** Queries belonging to another URL tier (e.g., recipe queries on Homepage, or competitor brand names on commercial hubs).
5. **Business-Model Mismatch (`حذف شده — خارج از مدل فروش`):** Queries outside the client's actual inventory/service model (e.g., live livestock sales for a retail butcher).

---

## 3. Anti-Cannibalization Resolution Matrix

| Signal Observed | Root Cause | Strategic Action |
| :--- | :--- | :--- |
| **Commercial Brand/Category page carries 3,000w of educational/authenticity text** | Informational bloat competing against dedicated blog guides | Condense the overlapping block on the commercial page to **1 summary paragraph + internal link** to the dedicated guide, and link the main hub to the new spoke. |
| **Two adjacent blog topics overlap** (e.g., yellow-lens vs night-driving glasses; computer vs reading glasses) | Unclear primary SERP promise | Assign crisp distinct H1 + primary SERP promise to each, and enforce a **post-publish reciprocal 1-paragraph summary + bidirectional internal link**. |
| **Two PDPs fluctuate for the same commercial query** | Mismatched copy or misassigned anchors | Designate ONE canonical PDP, realign all internal/off-page anchors, and confirm with user before redirecting/rewriting the secondary SKU. |
| **Spelling variants split demand** (`کارتیه/کارتیر`, `ریبن/ری بن`) | Fragmented targeting | Map all spelling variants to ONE canonical target page rather than creating duplicate posts. |
| **Informational query ranks on a PDP** | Missing definitional guide | Publish a focused Tier-4 blog post answering the informational intent and passing a bare contextual link UP to the Tier-3 PDP. |

---

## 4. Writer-Ready Content Brief Template

```markdown
# بریف استراتژیک محتوا: [عنوان پیشنهادی / موضوع]
- **نوع خروجی و موتور اجرا:** [مقاله بلاگ v2 | رفرش ۲۵۰ کلمه‌ای | لندینگ/محصول | رپورتاژ]
- **آدرس هدف:** [URL تاییدشده از brand-* یا «آدرس جدید — پیشنهاد اسلاگ انگلیسی /.../»]
- **کلیدواژه اصلی:** [...]
- **کلیدواژه‌های فرعی و هم‌املا (`کلمات مرتبط`):** [...]
- **کلمات خارج از محدوده / ضد کنیبالیزیشن (`حذف شده`):** [کلمات متعلق به صفحات دیگر + آدرس مالک]
- **نیت جستجو و گپ سرپ:** [آنچه رقبای فعلی جا انداخته‌اند: استاندارد، جدول، هشدار واقعی]
- **محور پاسخ مستقیم (Rule 0):** [طرز تهیه: مراحل ۱..۴ | خواص: ۱۰۰٪ تغذیه بدون پخت | انواع: لیست انواع | بهترین: میانگین + شرطی | تایم‌لاین/تشخیصی]
- **سقف کلمات:** [پیش‌فرض v2 فشرده ۱۴۰۰ تا ۱۸۰۰ (زیر ۲۰۰۰) | یا استثنای بریف]

## ساختار پیشنهادی بدنه و جداول
1. **مقدمه ۴ بخشی + `## [موضوع] در یک نگاه`**
2. **تک جدول متمرکز آغازین:** [ستون‌ها] + `نکته‌ای که در این جدول پنهان است:` (`۲` بولت)
3. **گام‌های عملی / راهکار فوری (`۱. ۲. ۳.`) -> کارهای ممنوعه (`۱. ۲. ۳.`)**
4. **سرفصل‌های H2 -> H3 متقارن (هر H2 با ۱-۲ خط پاسخ مستقیم):** [...]
5. **بخش اعتمادسازی برند (از `brand-*`) -> جمع‌بندی (`۱..۴` اشتباه) -> `۴-۶` FAQ -> `## منابع`**

## نقشه لینک‌سازی داخلی و اقدامات پس از انتشار
- **لینک‌های لخت تاییدشده (`حداکثر ۱ بار برای هر URL`):** [...]
- **آپدیت متقابل صفحات هم‌خانواده/بالادستی پس از انتشار:** [...]
- **ورودی‌های مفقود / نیازمند تایید کاربر:** [...]
```
