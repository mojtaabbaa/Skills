# Module 10: Figma-to-Code 1:1 Implementation Workflow (Figma MCP)

Integrated from `figma-implement-design` & `figma-mcp`. Governs pixel-accurate translation of Figma frames and components into production code while respecting the target repository's existing design system and conventions.

---

## 1. Prerequisites & Scope

- **Use when:** Translating a Figma URL (`https://figma.com/design/:fileKey/:fileName?node-id=1-2`) or active Figma Desktop selection (`figma-desktop` MCP) into production UI code (React/Next.js/Tailwind, HTML/CSS, or Elementor/WordPress templates).
- **Never guess from memory:** Always fetch live structured context AND a visual screenshot before writing code.

---

## 2. Mandatory 7-Step Figma-to-Code Workflow

1. **Extract File Key & Node ID:**
   - Parse `:fileKey` (segment after `/design/`) and `nodeId` (`node-id` query param, e.g., `42-15`).
   - With local `figma-desktop` MCP, the currently selected node in Figma Desktop can be inspected directly without a URL.
2. **Fetch Structured Design Context (`get_design_context`):**
   - Call `get_design_context(fileKey, nodeId)` to extract Auto Layout, constraints, typography, colors/variables, spacing, padding, and variants.
   - **Truncation Fallback:** If the frame is too large/complex, call `get_metadata(fileKey, nodeId)` first to map major section child IDs (header, hero, cards, sidebar, footer), then call `get_design_context` per child section.
3. **Capture Ground-Truth Visual Screenshot (`get_screenshot`):**
   - Call `get_screenshot(fileKey, nodeId)` for the exact node. Treat this screenshot as the **visual parity oracle** throughout implementation.
4. **Preserve Exact Figma Assets:**
   - Download/use images, icons, and SVGs returned by the Figma MCP asset endpoint directly (including `localhost` asset URLs when served locally).
   - Do NOT invent fake placeholder SVGs or swap in unrelated icon packs when real Figma assets are provided.
5. **Translate to Project Conventions (Never Blindly Copy Raw Output):**
   - Treat Figma MCP output (often React + Tailwind) as a **specification of layout and behavior**, not literal copy-paste code style.
   - **Reuse over recreation:** Map to existing project components (`Button`, `Card`, `Dialog`, Elementor containers, etc.) and extend variants rather than duplicating components.
   - **Design System Tokens First:** Map Figma variables/colors/typography to project tokens (`--color-*`, Tailwind `@theme`, Elementor Kit globals). When a minor conflict exists between Figma raw hex and an official project token, prefer the project token and document any intentional deviation in code comments.
6. **Achieve 1:1 Visual Parity + Responsive & A11y Discipline:**
   - Match alignment, spacing rhythm, font sizes/weights/line-heights, border radii, and interactive states (`hover`, `focus-visible`, `active`, `disabled`).
   - Apply `Module 08` (WCAG 2.2 AA contrast, semantic landmarks, keyboard focus) and `Module 09` (mobile stacking, `>= 44px` tap targets) even if the static Figma frame only shows desktop.
   - For Persian RTL frames, convert physical CSS properties to logical properties (`padding-inline`, `margin-inline`, `text-align: start`) cleanly.
7. **Side-by-Side Visual Validation:**
   - Render in a real browser and verify against the Step 3 Figma screenshot:
     - [ ] Layout, alignment, spacing, and sizing match
     - [ ] Typography (font family, size, weight, line-height) matches
     - [ ] Colors and surfaces match project tokens / Figma spec
     - [ ] Interactive states work cleanly (`hover`, `focus-visible`, `disabled`, modals/drawers)
     - [ ] Responsive breakpoints (`375px`, `768px`, `1024px`, `1440px`) behave with zero horizontal overflow
     - [ ] All Figma images/SVGs render crisply with zero broken URLs
