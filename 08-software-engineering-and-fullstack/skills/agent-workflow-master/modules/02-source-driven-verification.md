# Module 02: Source-Driven Development (Official Docs First)

Consolidated from `source-driven-development`.

---

## The 4-Step Verification Process

Never rely on stale training memory for fast-moving frameworks (Next.js, React, Tailwind v4, Supabase, Elementor v4, WooCommerce HPOS, Gemini SDK):

1. **Detect Exact Stack & Versions:** Read `package.json`, `composer.json`, plugin headers (`Version:`), or lockfiles FIRST.
2. **Consult Official Primary Sources:** Check installed `node_modules/*/docs/` (e.g., Next.js bundled docs!), plugin PHP source code (e.g., Elementor Core/Pro source), official MCP doc servers (e.g., `gemini-api-docs`), or official upstream documentation via web search.
3. **Implement Verified Patterns Only:** Reject deprecated APIs, guessed method signatures, or unverified flags. If docs and training memory disagree, **official current docs + actual installed source win 100% of the time**.
4. **Cite Sources:** Note the exact version, source file, or documentation page backing any non-trivial API usage.

### Red Flags (Stop & Verify Immediately)
- Guessing a hook name, CLI flag, CSS control key, or SDK parameter without reading source/docs.
- Copy-pasting patterns from older major versions (e.g., Tailwind v3 syntax into v4, Elementor v2 deprecated hooks into v4, legacy `generateContent` when modern SDK applies).
