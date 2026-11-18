# Engine 04: Surgical Content Refresh, 250w Read-More & 10x Full-Stack Audit

Use this engine whenever updating, refreshing, expanding, or auditing existing published URLs (blogs, brand archives, categories, or landing pages). Load the target `brand-<project>` skill first.

> **The Non-Destructive Golden Rule:** Never blindly rewrite a ranking article when a surgical modular update preserves URL equity, established headings, and historical relevance signals.

---

## 1. Mode Selection Decision Tree

1. **Mode A — Surgical Blog / Guide Insertion (`محل قرارگیری`):** Existing article ranks well but misses a secondary keyword, modern standard, comparison table, or safety/care sub-section.
2. **Mode B — Category `Read More` Semantic Expansion (`~250` Words):** Commercial WooCommerce category or price hub needs incremental topical depth without pushing products below the fold.
3. **Mode C — 10x Full-Stack Page Audit & Surgical Diff (`اصلاحات بلاگی`):** High-value article, `/brand/...`, or core category suffering traffic/click drops, stale years (`2024->2026`), stock/sort UX blockers, cannibalization bloat, or broken schema.

---

## 2. Mode A: Surgical Modular Insertion (200–500 Words)

### Rules:
* Keep valid existing paragraphs intact; **NEVER imitate legacy low-quality prose** of older live posts — every inserted module MUST meet v2 UX-First clarity.
* Open the inserted `H2` or `H3` with a **1–2 line direct answer** (never stack `H2 -> H3`), cap prose at `2` lines (`3` max), use Ordered Lists (`1. 2. 3.`) for steps/timelines/prohibitions vs Bullets (`*`) for attributes.
* Include a brief **Introductory Bridge** referencing the preceding section and a smooth **Concluding Bridge** into the next section so the insertion never feels like an artificial graft.
* Respect `Max 1 link per unique URL` across the *entire* page (including links already live on the page) and zero reportage `تصویر ۱/۲` clutter.

### Required Output Format:
```text
آپدیت [شماره/عنوان] — «[نام دقیق مقاله یا URL]»
کلمه هدف: [کلمه کلیدی یا گپ جستجو]
📍 محل قرارگیری: بعد از بخش «[عنوان دقیق بخش قبلی]» و قبل از «[عنوان دقیق بخش بعدی]» (یا: جایگزین بخش فعلی «...» به دلیل نقص محتوایی)

## [یا ### عنوان دقیق]
[۱ تا ۲ خط پاسخ مستقیم]
[جدول یا لیست عددی ۱. ۲. ۳. / بولت‌های کوتاه زیر ۲۵ کلمه]
```

---

## 3. Mode B: Category `Read More` Semantic Chunk (~250 Words)

### Rules:
* Target **~250 dense words** per expansion block — zero fluff, zero promotional hype, zero FAQ block, zero aggressive CTAs.
* Specify exact heading insertion coordinates between existing category sections.
* Follow **3-Level Semantic Progression** when building category depth over successive updates:
  1. **Level 1 (Foundational / پایه):** Core definition, buyer relevance, local store/production trust.
  2. **Level 2 (Selection & Use / انتخاب و کاربرد):** How to choose models/variants/cuts/roasts for real user scenarios.
  3. **Level 3 (Technical & Specs / فنی و پیشرفته):** Materials, standards, processing methods, dimensional/grade nuances.

---

## 4. Mode C: 10x Full-Stack Audit & Color/Action Diff Protocol

### Strict Anti-Hallucination Rule:
Never fabricate GSC metrics, WooCommerce product IDs (`[products ids="..."]`), sales tables, or unseen HTML bugs. If store/GSC data is missing, emit an explicit **`داده لازم از مدیر فروش و پشتیبانی`** block stating: *«اگر داده نرسید، این جدول/بخش منتشر نشود و هیچ عددی حدس زده نشود.»*

### Mandatory 5-Section Deliverable Order:
1. **Header & Root Diagnosis:**
   * `لینک صفحه:` `<exact URL>`
   * `هدف این آپدیت:` Diagnose BOTH copy gaps AND non-text blockers (e.g., 29/34 SKUs out-of-stock sorted by newest, CTR mismatch vs GSC top queries, stale year in H1, 4,000w informational bloat on a commercial archive).
   * **Change-Tracking Legend:** In Word/DOCX use standard color coding (سیاه=بدون تغییر، سبز=جدید، آبی=جایگزین متن خط‌خورده، خط‌خورده=حذف، زرد=دستور کار تیم، آبی روشن=آدرس لینک). In Markdown, tag blocks explicitly with `[بدون تغییر]` / `[اضافه شود - جدید]` / `[حذف شود - خط خورده]` / `[جایگزین شود به جای متن قبل]` + `اقدام تیم محتوا:` notes.
2. **`# متن مقاله با تغییرات`:**
   * Scrub unverified claims (fake studies, wrong founding dates, banned dealership claims, competitor retail outbound links).
   * Condense sections cannibalizing dedicated spokes into 1-paragraph summaries + internal links; remove irrelevant "Read More" banners; fix legacy `/blog/` links.
   * Flag low-res (`300x300`) or copyrighted images for WebP `Large/Full` replacement with clean `alt`.
3. **`# اصلاح متاها`:** Side-by-side `فعلی` vs `جدید` for SEO Title (`<=60c`), Meta Description (`<=155c`), and H1 (check for Arabic `ي`/`ك` bugs!), keeping `slug` untouched and flagging `dateModified` update.
4. **`# اسکیما`:** Current vs target schema (`BlogPosting` / `CollectionPage`+`ItemList` / `FAQPage` / `BreadcrumbList`), copy-ready JSON-LD matching final text word-for-word (NEVER duplicate Rank Math), + post-publish QA (`Rich Results Test`, `validator.schema.org`, clickable HTTPS check).
5. **`# تسک‌های تیم فنی`:** Page-specific dev tasks (e.g., WooCommerce grid count=36 sorted by popularity with out-of-stock last + lazy-load after card 8; quick-access anchor chips `CLS=0`; convert fake `<p>` headings to semantic `<h2>`/`<h3>`; remove duplicate filter HTML / empty `<a></a>` anchors; normalize fragmented attributes; interactive shortcode specs per Engine 08).
