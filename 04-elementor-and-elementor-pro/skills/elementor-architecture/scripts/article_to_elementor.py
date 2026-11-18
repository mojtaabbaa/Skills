#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brand-Agnostic Compiler: article_to_elementor.py
Compiles structured editorial content into native Elementor Flexbox Container AST JSON
(_elementor_data) strictly obeying all 7 Deadly Sins:
  1. ZERO duplicate H1 widgets (starts editorial headings at H2).
  2. Full-width single-column CTA banners (NO cramped 2-col squished banners).
  3. Uses `image_border_radius` (NEVER `border_radius`) on image widgets.
  4. Container settings bare (`padding`/`margin`), widget settings underscored (`_margin`).
  5. Multi-column desktop grids explicitly include `width_mobile: 100%` & `flex_direction_mobile: column`.
  6. Sources container placed strictly BEFORE FAQ accordion.
  7. Respects active brand's orthography (`strip_zwnj=False` by default; enable ONLY for Zero-ZWNJ brands).
"""

from dataclasses import dataclass
import json
import re
import uuid


def gen_id() -> str:
    return uuid.uuid4().hex[:7]


@dataclass
class BrandThemeConfig:
    font_family: str = "Vazirmatn"
    canvas_bg: str = "#FFFFFF"
    surface_bg: str = "#F8FAFC"
    accent_color: str = "#1E293B"
    accent_secondary: str = "#3B82F6"
    danger_color: str = "#DC2626"
    text_primary: str = "#0F172A"
    text_secondary: str = "#334155"
    text_muted: str = "#64748B"
    border_subtle: str = "rgba(15, 23, 42, 0.10)"
    cta_text_color: str = "#FFFFFF"
    cta_btn_bg: str = "#FFFFFF"
    cta_btn_text: str = "#1E293B"
    strip_zwnj: bool = False
    strip_exclamation: bool = False


class ElementorEditorialBuilder:
    def __init__(self, theme: BrandThemeConfig | None = None):
        self.theme = theme or BrandThemeConfig()
        self.elements: list[dict] = []

    def clean_text(self, text: str) -> str:
        if not isinstance(text, str):
            return text
        if self.theme.strip_zwnj:
            text = text.replace("\u200c", " ")
            text = re.sub(r"([هة])\s+ی\s+", r"\1 ", text)
        if self.theme.strip_exclamation:
            text = text.replace("!", "")
        return text

    def _typo(self, prefix: str, size: int, weight: str = "400", line_height: float = 1.75) -> dict:
        return {
            f"{prefix}_typography": "custom",
            f"{prefix}_font_family": self.theme.font_family,
            f"{prefix}_font_size": {"unit": "px", "size": size},
            f"{prefix}_font_weight": weight,
            f"{prefix}_line_height": {"unit": "em", "size": line_height},
        }

    def add_direct_answer(self, title: str, html_body: str):
        t = self.theme
        self.elements.append({
            "id": gen_id(),
            "elType": "container",
            "settings": {
                "content_width": "boxed",
                "background_background": "classic",
                "background_color": t.surface_bg,
                "border_border": "solid",
                "border_width": {"unit": "px", "top": "1", "right": "4", "bottom": "1", "left": "1", "isLinked": False},
                "border_color": t.accent_secondary,
                "border_radius": {"unit": "px", "top": "14", "right": "14", "bottom": "14", "left": "14", "isLinked": True},
                "padding": {"unit": "px", "top": "24", "right": "24", "bottom": "24", "left": "24", "isLinked": True},
                "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "28", "left": "0", "isLinked": False},
            },
            "elements": [
                {
                    "id": gen_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": self.clean_text(title),
                        "header_size": "h2",
                        "title_color": t.accent_secondary,
                        **self._typo("typography", 20, "700", 1.5),
                    },
                },
                {
                    "id": gen_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": self.clean_text(html_body),
                        "text_color": t.text_primary,
                        **self._typo("typography", 15, "400", 1.85),
                    },
                },
            ],
        })

    def add_single_column_cta(self, title: str, description: str, button_text: str, button_url: str):
        """Full-width single-column CTA banner (obeys Deadly Sin #2: no squished 2-col image CTA)."""
        t = self.theme
        self.elements.append({
            "id": gen_id(),
            "elType": "container",
            "settings": {
                "content_width": "boxed",
                "flex_direction": "column",
                "flex_align_items": "center",
                "flex_justify_content": "center",
                "background_background": "gradient",
                "background_color": t.accent_color,
                "background_color_b": t.accent_secondary,
                "background_gradient_type": "linear",
                "background_gradient_angle": {"unit": "deg", "size": 135},
                "border_radius": {"unit": "px", "top": "16", "right": "16", "bottom": "16", "left": "16", "isLinked": True},
                "padding": {"unit": "px", "top": "36", "right": "32", "bottom": "36", "left": "32", "isLinked": False},
                "margin": {"unit": "px", "top": "24", "right": "0", "bottom": "32", "left": "0", "isLinked": False},
            },
            "elements": [
                {
                    "id": gen_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": self.clean_text(title),
                        "header_size": "h3",
                        "align": "center",
                        "title_color": t.cta_text_color,
                        **self._typo("typography", 21, "700", 1.5),
                    },
                },
                {
                    "id": gen_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": f'<p style="text-align:center;">{self.clean_text(description)}</p>',
                        "text_color": t.cta_text_color,
                        **self._typo("typography", 15, "400", 1.8),
                    },
                },
                {
                    "id": gen_id(),
                    "elType": "widget",
                    "widgetType": "button",
                    "settings": {
                        "text": self.clean_text(button_text),
                        "link": {"url": button_url, "is_external": False, "nofollow": False},
                        "align": "center",
                        "button_text_color": t.cta_btn_text,
                        "background_color": t.cta_btn_bg,
                        "border_radius": {"unit": "px", "top": "10", "right": "10", "bottom": "10", "left": "10", "isLinked": True},
                        "text_padding": {"unit": "px", "top": "12", "right": "28", "bottom": "12", "left": "28", "isLinked": False},
                        **self._typo("typography", 15, "700", 1.4),
                    },
                },
            ],
        })

    def add_image(self, url: str, alt: str, attachment_id: int | str = "", radius_px: int = 12):
        """Uses `image_border_radius` strictly (Deadly Sin #3)."""
        self.elements.append({
            "id": gen_id(),
            "elType": "container",
            "settings": {
                "content_width": "boxed",
                "margin": {"unit": "px", "top": "16", "right": "0", "bottom": "24", "left": "0", "isLinked": False},
            },
            "elements": [
                {
                    "id": gen_id(),
                    "elType": "widget",
                    "widgetType": "image",
                    "settings": {
                        "image": {"url": url, "id": attachment_id, "alt": self.clean_text(alt), "source": "library"},
                        "image_size": "large",
                        "align": "center",
                        "image_border_radius": {
                            "unit": "px",
                            "top": str(radius_px),
                            "right": str(radius_px),
                            "bottom": str(radius_px),
                            "left": str(radius_px),
                            "isLinked": True,
                        },
                    },
                }
            ],
        })

    def add_sources_and_faq(self, sources: list[tuple[str, str]], faqs: list[tuple[str, str]], sources_title: str = "منابع معتبر", faq_title: str = "پرسش‌های متداول"):
        """Enforces Sources strictly BEFORE FAQ Accordion (Deadly Sin #6)."""
        t = self.theme
        if sources:
            self.elements.append({
                "id": gen_id(),
                "elType": "container",
                "settings": {
                    "content_width": "boxed",
                    "border_border": "solid",
                    "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
                    "border_color": t.border_subtle,
                    "padding": {"unit": "px", "top": "24", "right": "0", "bottom": "16", "left": "0", "isLinked": False},
                    "margin": {"unit": "px", "top": "28", "right": "0", "bottom": "20", "left": "0", "isLinked": False},
                },
                "elements": [
                    {
                        "id": gen_id(),
                        "elType": "widget",
                        "widgetType": "heading",
                        "settings": {
                            "title": self.clean_text(sources_title),
                            "header_size": "h3",
                            "title_color": t.text_muted,
                            **self._typo("typography", 15, "600", 1.5),
                        },
                    },
                    {
                        "id": gen_id(),
                        "elType": "widget",
                        "widgetType": "icon-list",
                        "settings": {
                            "icon_list": [
                                {
                                    "_id": gen_id(),
                                    "text": self.clean_text(label),
                                    "link": {"url": url, "is_external": True, "nofollow": True},
                                    "selected_icon": {"value": "fas fa-external-link-alt", "library": "fa-solid"},
                                }
                                for label, url in sources
                            ],
                            "icon_color": t.accent_secondary,
                            "text_color": t.text_muted,
                            **self._typo("icon_typography", 13, "400", 1.7),
                        },
                    },
                ],
            })
        if faqs:
            self.elements.append({
                "id": gen_id(),
                "elType": "container",
                "settings": {
                    "content_width": "boxed",
                    "margin": {"unit": "px", "top": "12", "right": "0", "bottom": "36", "left": "0", "isLinked": False},
                },
                "elements": [
                    {
                        "id": gen_id(),
                        "elType": "widget",
                        "widgetType": "heading",
                        "settings": {
                            "title": self.clean_text(faq_title),
                            "header_size": "h2",
                            "title_color": t.text_primary,
                            **self._typo("typography", 22, "700", 1.5),
                        },
                    },
                    {
                        "id": gen_id(),
                        "elType": "widget",
                        "widgetType": "accordion",
                        "settings": {
                            "tabs": [
                                {
                                    "_id": gen_id(),
                                    "tab_title": self.clean_text(q),
                                    "tab_content": f"<p>{self.clean_text(a)}</p>",
                                }
                                for q, a in faqs
                            ],
                            "title_html_tag": "h3",
                            "icon": {"value": "fas fa-chevron-down", "library": "fa-solid"},
                            "icon_active": {"value": "fas fa-chevron-up", "library": "fa-solid"},
                            "icon_align": "left",
                            "title_color": t.text_primary,
                            "tab_active_color": t.accent_secondary,
                            "title_background": t.surface_bg,
                            "content_color": t.text_secondary,
                            "content_background_color": t.canvas_bg,
                            **self._typo("title_typography", 16, "600", 1.5),
                            **self._typo("content_typography", 14, "400", 1.8),
                        },
                    },
                ],
            })

    def to_json(self, indent: int | None = None) -> str:
        return json.dumps(self.elements, ensure_ascii=False, indent=indent)


if __name__ == "__main__":
    builder = ElementorEditorialBuilder()
    builder.add_direct_answer("پاسخ سریع", "<p>نمونه خروجی کامپایلر بدون وابستگی به برند.</p>")
    builder.add_single_column_cta("مشاوره تخصصی", "توضیح کوتاه دعوت به اقدام.", "ثبت درخواست", "https://example.com/")
    builder.add_image("https://example.com/img.webp", "تصویر نمونه", 101)
    builder.add_sources_and_faq(
        [("منبع مرجع نمونه", "https://example.org/")],
        [("سوال نمونه؟", "پاسخ دقیق نمونه.")],
    )
    print(builder.to_json(indent=2))
