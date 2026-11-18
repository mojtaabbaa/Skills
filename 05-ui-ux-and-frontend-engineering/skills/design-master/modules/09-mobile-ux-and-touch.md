# Module 09: Mobile-First UX, Touch Psychology & Native App Craft

Integrated from `mobile-design`. Governs both **mobile-first responsive web UI** (`320px–430px`) and **native/cross-platform mobile apps** (iOS HIG, Android Material Design 3, React Native, Flutter).

> **Core Principle:** Mobile is NOT a shrunken desktop. Design for the **worst real-world conditions**: one hand, imprecise thumb (~7mm contact area), bright sunlight, flaky network, frequent interruptions, and low battery.

---

## 1. Touch Ergonomics & Fitts' Law

- **Minimum Touch Targets:**
  - **iOS HIG:** `44pt × 44pt` minimum.
  - **Android Material 3 / Responsive Web:** `48dp × 48dp` (`44–48px`) minimum.
  - **Gap Between Adjacent Targets:** At least **`8–12px`** to prevent accidental mis-taps.
- **Thumb Zone Anatomy (One-Handed Reach):**
  - **Bottom Arc (Natural / Easy):** Primary CTAs, bottom navigation bar, main sticky action bar.
  - **Middle Zone (Comfortable):** Primary content browsing, cards, secondary filters.
  - **Top Corners (Hard / Stretch):** Infrequent settings, back button, destructive/overflow actions (keep destructive actions away from accidental thumb hits).
- **No Hover Dependency:** Mobile has NO `:hover`. Never hide essential information, tooltips, or actions behind hover states.
- **Gesture + Button Parity:** Every swipe/drag gesture MUST also have an explicit visible tap button for discoverability and accessibility (WCAG 2.5.7).
- **320px–390px Overflow Rule:** Zero horizontal overflow at `320px`, `360px`, and `390px`; stack multi-column splits cleanly with text/primary value first and full-width primary buttons where appropriate.

---

## 2. Platform Conventions: Unify vs. Diverge (Native & Cross-Platform Apps)

| Layer | Unify Across iOS & Android | Diverge by Platform Convention |
| :--- | :--- | :--- |
| **Business Logic, Data, Core Features** | Always unified | — |
| **Navigation & Back** | — | **iOS:** edge swipe back + bottom tabs (`SF Symbols`) | **Android:** system back gesture/button + bottom nav/drawer (`Material Symbols`) |
| **Sheets & Pickers** | — | **iOS:** bottom action sheet / native wheel pickers | **Android:** Material bottom sheet / dialog / M3 pickers |
| **Typography & Touch Floor** | — | **iOS:** SF Pro (`44pt`) | **Android:** Roboto (`48dp`) *(Persian apps: Vazirmatn / IRANSansX / PelakFA with crisp weight scale)* |

---

## 3. Mobile Performance, States & Security Non-Negotiables

- **GPU-Only Animations:** Animate **ONLY `transform` and `opacity`** (60fps GPU-composited). NEVER animate `width`, `height`, `top`, `left`, `margin`, or `padding`.
- **Mandatory UI States (Every Screen):**
  1. **Loading state** (skeletons/progress — never a blank white freeze)
  2. **Empty state** (clear explanation + direct primary action)
  3. **Error state** (actionable message + explicit Retry button)
  4. **Offline / slow-network graceful degradation** (cached view + clear offline banner)
- **Native / Cross-Platform Anti-Patterns (Strictly Banned):**
  - **Lists:** NEVER render long lists inside `ScrollView` — always use `FlatList` / `FlashList` (with stable `keyExtractor`, `React.memo`, `useCallback`, `getItemLayout`) or Flutter `ListView.builder` + `const` constructors.
  - **Animations:** Always enable `useNativeDriver: true` in React Native where supported.
  - **Security:** NEVER store auth tokens in plain `AsyncStorage` — always use `SecureStore` / Keychain / `EncryptedSharedPreferences`. Never hardcode API keys or leave `console.log` in production builds.
  - **Cleanup:** Always dispose subscriptions, event listeners, and timers on unmount.

---

## 4. Pre-Ship Mobile UX Gate

- [ ] Touch targets `>= 44–48px` with `>= 8px` spacing between controls
- [ ] Primary CTA reachable inside the lower thumb zone (not buried behind fixed bars)
- [ ] Zero horizontal overflow at `320px` and `390px`
- [ ] Loading, empty, error+retry, and offline states implemented
- [ ] Animations strictly limited to `transform` / `opacity` + `prefers-reduced-motion` respected
- [ ] Readable typography under daylight glare (`>= 16px` body text, `>= 4.5:1` contrast)
