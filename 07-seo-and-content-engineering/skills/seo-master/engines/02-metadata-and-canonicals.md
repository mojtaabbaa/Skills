# Engine 02: SEO Metadata, CTR Formulas & Canonical Hygiene

Use this engine for writing or optimizing standalone or batch Persian SEO Titles, Meta Descriptions, H1 headings, and attribute/color filter canonical metadata. Load the active workspace's local `.agents/skills/brand-*/SKILL.md` skill first to apply exact orthography (`ZWNJ` vs `Zero-ZWNJ`), forbidden claims, and brand suffixes.

---

## 1. Non-Negotiable Length & Quality Constraints
* **SEO Title (`عنوان اصلی سئو`):** Strictly **`<= 60` characters** (sweet spot `50–59` chars, counting spaces). Distinct from the comprehensive H1.
* **Alternative Title (`عنوان جایگزین`):** Secondary A/B test angle when using a top metadata block.
* **Meta Description (`متا دیسکریپشن`):** Strictly **`130–155` characters** (`<= 155–160` max).
* **H1 Heading:** Clear, human-readable full match to search intent without keyword stuffing or stray Arabic characters (`ي` / `ك` -> must be Persian `ی` / `ک`).
* **Zero Legacy Spam:** ZERO exclamation marks (`!`), zero empty superlatives (`فوق‌العاده`, `باورنکردنی`, `ارزان‌ترین ایران`), zero unverified dealership claims (`نمایندگی رسمی` unless verified in local `.agents/skills/brand-*/SKILL.md`), and zero repeated boilerplate across batch sheets.
* **Exact Reporting:** When producing standalone or batch metadata sheets, report exact character counts (`(54 کاراکتر)`) alongside every Title and Meta, and preserve existing URL slugs (`slug صفحه تغییر نمی‌کند`) unless a migration is explicitly requested.

---

## 2. Proven High-CTR Formulas by Page Type

### A. Educational & Guide Articles (Blog)
* **SEO Title Pattern:** `[کلیدواژه اصلی]: [علت/معیار اصلی] + [عدد] [راهکار/نکته کاربردی]`
  * *Alternative Question Pattern:* `[سوال اصلی کاربر]؟ [پاسخ کوتاه یا جدول زمانی]`
  * *Freshness Rule:* Avoid stale year tags (`2024` / `۱۴۰۰`) — either update to active year for genuinely seasonal topics or omit the year for evergreen guides.
  * *GSC Alignment Rule:* Align title directly to the dominant high-impression query intent rather than secondary angles.
* **Meta Description Pattern:** `[پاسخ مستقیم یا سوال اصلی] + [وعده عناصر ارزشمند: جدول مقایسه/زمان‌بندی/علائم خطر] + [ختم یا CTA مجاز برند هدف].`

### B. Commercial Brand & Category Archives (`/brand/<slug>/`, `/product-category/.../`)
* **SEO Title Pattern:** `[محصول/برند] [هم‌املا در صورت نیاز] اصل | خرید [محصول/دسته] [تخصیص کلیدی]`
  * Include verified high-impression Persian spelling variants naturally when backed by GSC data (e.g., `کارتیه (کارتیر)`, `ریبن / ری بن`, `پلیس / عینک پلیسی`).
* **Meta Description Pattern:** `خرید [محصول/برند] [تخصیص]؛ [۲-۳ ویژگی یا مدل متمایز واقعی همان برند — بدون کپی‌پیست عمومی] با [۲-۳ مزیت تاییدشده برند هدف].`

### C. Canonical Attribute & Filter Pages (e.g., Frame Colors, Sub-Variants)
* **Primary (`اصلی`) Canonical Pages:** Own the broad head modifier (`عینک آبی`, `عینک مشکی`).
* **Sub-Variant Pages:** Must target their exact distinguishing modifier (`آبی شفاف`, `قهوه‌ای هاوانا`, `مشکی مات`) so they NEVER cannibalize their primary canonical parent.
* **Multi-Variant Product SKUs:** When two SKUs share one model code, append the exact color/variant code inside the focus keyword, SEO Title, Meta Description, and H2 #1 to prevent SKU cannibalization.

---

## 3. Metadata Placement Contract
Follow the active workspace's local `.agents/skills/brand-*/SKILL.md` rule:
* **Top Block Standard (Default for most projects):** `# مشخصات سئو و متادیتا` (`عنوان اصلی سئو`, `عنوان جایگزین`, `متا دیسکریپشن`) separated from `# H1` by `---`.
* **Bottom `.md` Block Exception (when mandated by the active project's local brand skill & `rep/` advertorials):** `# H1` at line 1 -> body -> `---` -> `**متا تایتل:**` & `**متا دسکریپشن:**` at bottom (excluded from publisher word limits in `rep/`).
