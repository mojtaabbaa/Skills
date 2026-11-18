# Version Management & Deprecation Ledger

## 1. Installed Environment Version Snapshot

| Software Component | Exact Inspected Version | Minimum Requirement | Recommended Runtime |
|---|---|---|---|
| **WordPress Core** | 7.1.4 (Local Core Source) / 6.8+ (Live Site) | 6.8 | 7.x |
| **Elementor Free** | 4.2.3 | PHP 7.4, WP 6.8 | PHP 8.2+, WP 7.x |
| **Elementor Pro** | 4.3.2 | Elementor Free 4.0 | Elementor Free 4.2+ |
| **PHP Runtime** | 8.2.4 (CLI active) | 7.4 | 8.2 / 8.3 |
| **WooCommerce** | Fully HPOS-compatible in 4.3.2 Pro | WooCommerce 8.0+ | Latest WC |

---

## 2. API Deprecation & Modern Replacement Matrix

| Deprecated Feature / API | Deprecated In | Modern Replacement | Architectural Impact |
|---|---|---|---|
| `$widgets_manager->register_widget_type()` | 3.5.0 | `$widgets_manager->register( $instance )` | Eliminates redundant object cloning. |
| `$widgets_manager->unregister_widget_type()`| 3.5.0 | `$widgets_manager->unregister( $name )` | Directly removes widget from registry array. |
| `elementor/widgets/widgets_registered` hook | 3.5.0 | `elementor/widgets/register` hook | Passes `$widgets_manager` directly as the first callback parameter. |
| `_register_controls()` method | 3.1.0 | `register_controls()` method | Modern visibility rules (`protected function register_controls()`). |
| Sections & Columns (`section`, `column`) | 3.18.0 | Flexbox / Grid Containers (`container`) | Reduces DOM nodes by over 60%, enables modern CSS flexbox/grid. |
| FontAwesome 4 icon strings | 2.6.0 | Modern `ICONS` control (`value`, `library`) | Supports FontAwesome 5/6 and custom inline SVGs. |
| Legacy Scheme Controls (`Scheme_Color`) | 3.0.0 | Global Style Tokens (`__globals__` & Kit) | Dynamic CSS variables replace hardcoded CSS hex schemes. |
