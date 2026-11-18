# Elementor Design System & Global Styles

## 1. The Active Kit Architecture
Elementor centralizes all global design tokens inside a dedicated document type called **Kit** (`Elementor\Core\Kits\Documents\Kit`).
- Stored as a post in `wp_posts` with `post_type: 'elementor_library'`.
- Template type: `_elementor_template_type = 'kit'`.
- Identified by option: `elementor_active_kit_id`.
- Settings stored in `_elementor_page_settings` on the Kit post.

---

## 2. Global Colors System

### Four Default System Colors
Elementor initializes four base semantic color tokens:
1. **Primary (`primary`)**: Main brand color (Used for headings, primary buttons, accents).
2. **Secondary (`secondary`)**: Supporting brand tone (Used for sub-headings, borders, list icons).
3. **Text (`text`)**: Body text color (Used for paragraphs, descriptions, input labels).
4. **Accent (`accent`)**: Call-to-action highlight color (Used for active links, badges, sale ribbons).

### Custom Global Colors
Users can add unlimited brand colors to the Kit repeater (`custom_colors`). Each entry receives a unique 7-character `_id` and compiles into a CSS variable:
`--e-global-color-{$id}: #...;`

### CSS Output in `global.css`:
```css
:root {
  --e-global-color-primary: #1e3a8a;
  --e-global-color-secondary: #0284c7;
  --e-global-color-text: #374151;
  --e-global-color-accent: #f59e0b;
  --e-global-color-7c9d1a4: #10b981; /* Custom Brand Success */
}
```

### Binding a Global Color in Widget JSON:
```json
{
  "title_color": "",
  "__globals__": {
    "title_color": "globals/colors?id=primary"
  }
}
```

---

## 3. Global Typography System

### Four Default System Typography Presets
1. **Primary (`primary`)**: Heading font family, weight, and default scale.
2. **Secondary (`secondary`)**: Subheading font family and style.
3. **Text (`text`)**: Body copy font, line-height, and size.
4. **Accent (`accent`)**: Button and metadata font family, transform, and spacing.

### Custom Global Typography Presets
Added via the `custom_typography` repeater in Site Settings. Each generates CSS variables:
```css
:root {
  --e-global-typography-primary-font-family: "Inter", Sans-serif;
  --e-global-typography-primary-font-weight: 700;
  --e-global-typography-text-font-family: "Inter", Sans-serif;
  --e-global-typography-text-font-size: 16px;
  --e-global-typography-text-line-height: 1.6em;
}
```

### Binding Global Typography in Widget JSON:
```json
{
  "typography_typography": "",
  "__globals__": {
    "typography_typography": "globals/typography?id=primary"
  }
}
```

---

## 4. Theme Style (Site-Wide Base Overrides)
Theme Style settings configure base HTML elements across the entire website without custom CSS:
- **Typography**: Base styles for `<body>`, `<a>`, `<p>`, `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`.
- **Buttons**: Default background, text color, border radius, padding, and hover states for all buttons site-wide.
- **Images**: Default border radius, opacity, and box-shadow for all standard images.
- **Form Fields**: Base border, background, typography, padding, and focus outlines for all forms.

---

## 5. Engineering Governance Rules for Global Styles
1. **Never Hardcode Common Hex Values**: If a brand color is used in more than two places, bind it via `__globals__` to ensure site-wide theme maintainability.
2. **Respect Existing Kits**: When working on an existing WordPress site, inspect the active Kit ID and existing system colors first. Do not overwrite or redefine global colors without authorization.
3. **Zero Inline Styles for Typography**: Typography families, sizes, and line heights should reference Global Typography tokens whenever possible.
