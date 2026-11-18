#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brand-Agnostic Compiler v2: article_to_elementor.py
Compiles structured Persian editorial content into native, Non-Atomic Elementor
Flexbox Container AST JSON (_elementor_data), strictly enforcing:
  1. ZERO duplicate H1 widgets (starts editorial headings at H2).
  2. Full-width single-column CTA banners (NO cramped 2-col squished banners).
  3. Uses `image_border_radius` (NEVER `border_radius`) on image widgets.
  4. Container settings bare (`padding`/`margin`/`flex_gap`/`_title`), widget settings underscored (`_margin`/`_padding`).
  5. Flex-trap immunity:
     - Every flex child container with explicit width sets `content_width: "full"` (no boxed collapse).
     - Every column container sets explicit `flex_align_items: "stretch"` (unless centered).
     - Every row holding fixed avatar/badge + growing text pairs `_flex_size: "none"` with `_flex_size: "grow"` + `_flex_grow: "1"`.
     - Every widget carries `"isInner": False` and `"elements": []`.
  6. Multi-column desktop grids explicitly include `width_mobile: 100%` & `flex_direction_mobile: "column"`.
  7. Sources container placed strictly BEFORE FAQ accordion.
  8. Respects active brand's orthography (`strip_zwnj=False` by default; enable ONLY for Zero-ZWNJ brands).
  9. Zero HTML-widget visual dumps — native Elementor widgets only (Pill Badges, RTL Timelines,
     E-E-A-T Expert Cards, Decomposed Feature/Comparison Cards, CTA Banners, Sources & FAQ).
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
    accent_soft_bg: str = "rgba(59, 130, 246, 0.10)"
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

    def _typo(
        self,
        prefix: str,
        size: int,
        weight: str = "400",
        line_height: float = 1.8,
        size_mobile: int | None = None,
    ) -> dict:
        out = {
            f"{prefix}_typography": "custom",
            f"{prefix}_font_family": self.theme.font_family,
            f"{prefix}_font_size": {"unit": "px", "size": size, "sizes": []},
            f"{prefix}_font_weight": weight,
            f"{prefix}_line_height": {"unit": "em", "size": line_height, "sizes": []},
        }
        if size_mobile is not None:
            out[f"{prefix}_font_size_mobile"] = {"unit": "px", "size": size_mobile, "sizes": []}
        return out

    def _widget(self, widget_type: str, settings: dict) -> dict:
        return {
            "id": gen_id(),
            "elType": "widget",
            "isInner": False,
            "widgetType": widget_type,
            "settings": settings,
            "elements": [],
        }

    def _container(self, settings: dict, elements: list[dict], is_inner: bool = False, title: str | None = None) -> dict:
        merged = dict(settings)
        if title and not is_inner:
            merged["_title"] = self.clean_text(title)
        return {
            "id": gen_id(),
            "elType": "container",
            "isInner": is_inner,
            "settings": merged,
            "elements": elements,
        }

    def _pill_widget(self, label: str, url: str = "#") -> dict:
        t = self.theme
        return self._widget(
            "button",
            {
                "text": self.clean_text(label),
                "link": {"url": url, "is_external": False, "nofollow": False},
                "size": "xs",
                "_element_width": "auto",
                "button_text_color": t.accent_secondary,
                "background_color": t.accent_soft_bg,
                "border_radius": {"unit": "px", "top": "100", "right": "100", "bottom": "100", "left": "100", "isLinked": True},
                "text_padding": {"unit": "px", "top": "6", "right": "14", "bottom": "6", "left": "14", "isLinked": False},
                **self._typo("typography", 12, "600", 1.3),
            },
        )

    def add_direct_answer(self, title: str, html_body: str, badge_label: str | None = None):
        """Golden snippet direct-answer card with optional native Pill Badge."""
        t = self.theme
        children = []
        if badge_label:
            children.append(self._pill_widget(badge_label))
        children.extend([
            self._widget(
                "heading",
                {
                    "title": self.clean_text(title),
                    "header_size": "h2",
                    "align": "right",
                    "title_color": t.accent_secondary,
                    **self._typo("typography", 20, "700", 1.5, size_mobile=18),
                },
            ),
            self._widget(
                "text-editor",
                {
                    "editor": self.clean_text(html_body),
                    "align": "right",
                    "text_color": t.text_primary,
                    **self._typo("typography", 15, "400", 1.85),
                },
            ),
        ])
        self.elements.append(
            self._container(
                {
                    "content_width": "boxed",
                    "flex_direction": "column",
                    "flex_align_items": "stretch",
                    "flex_gap": {"column": "12", "row": "12", "unit": "px", "isLinked": True},
                    "background_background": "classic",
                    "background_color": t.surface_bg,
                    "border_border": "solid",
                    "border_width": {"unit": "px", "top": "1", "right": "4", "bottom": "1", "left": "1", "isLinked": False},
                    "border_color": t.accent_secondary,
                    "border_radius": {"unit": "px", "top": "14", "right": "14", "bottom": "14", "left": "14", "isLinked": True},
                    "padding": {"unit": "px", "top": "24", "right": "24", "bottom": "24", "left": "24", "isLinked": True},
                    "padding_mobile": {"unit": "px", "top": "20", "right": "18", "bottom": "20", "left": "18", "isLinked": False},
                    "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "28", "left": "0", "isLinked": False},
                },
                children,
                is_inner=False,
                title=f"پاسخ سریع — {title[:32]}",
            )
        )

    def add_section(self, heading: str, html_body: str, header_size: str = "h2"):
        """Core editorial section (strictly enforces h2–h6; never emits h1)."""
        if header_size.lower() == "h1":
            header_size = "h2"
        t = self.theme
        self.elements.append(
            self._container(
                {
                    "content_width": "boxed",
                    "flex_direction": "column",
                    "flex_align_items": "stretch",
                    "flex_gap": {"column": "14", "row": "14", "unit": "px", "isLinked": True},
                    "margin": {"unit": "px", "top": "12", "right": "0", "bottom": "24", "left": "0", "isLinked": False},
                },
                [
                    self._widget(
                        "heading",
                        {
                            "title": self.clean_text(heading),
                            "header_size": header_size,
                            "align": "right",
                            "title_color": t.text_primary,
                            **self._typo("typography", 22 if header_size == "h2" else 18, "700", 1.45, size_mobile=19 if header_size == "h2" else 16),
                        },
                    ),
                    self._widget(
                        "text-editor",
                        {
                            "editor": self.clean_text(html_body),
                            "align": "right",
                            "text_color": t.text_secondary,
                            **self._typo("typography", 15, "400", 1.85),
                        },
                    ),
                ],
                is_inner=False,
                title=f"بخش — {heading[:36]}",
            )
        )

    def add_rtl_timeline(self, section_title: str, steps: list[tuple[str, str, str]]):
        """
        Native zero-HTML vertical RTL editorial timeline.
        steps: list of (pill_label, step_title, step_description_html)
        """
        t = self.theme
        step_containers = []
        for idx, (pill, stitle, sbody) in enumerate(steps, 1):
            step_containers.append(
                self._container(
                    {
                        "content_width": "full",
                        "flex_direction": "column",
                        "flex_align_items": "stretch",
                        "flex_gap": {"column": "8", "row": "8", "unit": "px", "isLinked": True},
                        "background_background": "classic",
                        "background_color": t.surface_bg,
                        "border_border": "solid",
                        "border_width": {"unit": "px", "top": "1", "right": "3", "bottom": "1", "left": "1", "isLinked": False},
                        "border_color": t.accent_secondary,
                        "border_radius": {"unit": "px", "top": "12", "right": "12", "bottom": "12", "left": "12", "isLinked": True},
                        "padding": {"unit": "px", "top": "18", "right": "20", "bottom": "18", "left": "20", "isLinked": False},
                    },
                    [
                        self._pill_widget(pill or f"مرحله {idx}"),
                        self._widget(
                            "heading",
                            {
                                "title": self.clean_text(stitle),
                                "header_size": "h3",
                                "align": "right",
                                "title_color": t.text_primary,
                                **self._typo("typography", 17, "700", 1.5, size_mobile=16),
                            },
                        ),
                        self._widget(
                            "text-editor",
                            {
                                "editor": self.clean_text(sbody),
                                "align": "right",
                                "text_color": t.text_secondary,
                                **self._typo("typography", 14, "400", 1.85),
                            },
                        ),
                    ],
                    is_inner=True,
                )
            )

        self.elements.append(
            self._container(
                {
                    "content_width": "boxed",
                    "flex_direction": "column",
                    "flex_align_items": "stretch",
                    "flex_gap": {"column": "16", "row": "16", "unit": "px", "isLinked": True},
                    "margin": {"unit": "px", "top": "20", "right": "0", "bottom": "28", "left": "0", "isLinked": False},
                },
                [
                    self._widget(
                        "heading",
                        {
                            "title": self.clean_text(section_title),
                            "header_size": "h2",
                            "align": "right",
                            "title_color": t.text_primary,
                            **self._typo("typography", 22, "700", 1.45, size_mobile=19),
                        },
                    ),
                    *step_containers,
                ],
                is_inner=False,
                title=f"تایم‌لاین — {section_title[:32]}",
            )
        )

    def add_feature_cards_row(self, section_title: str, cards: list[tuple[str, str, str]], columns: int = 3):
        """
        Decomposed native cards grid (immune to boxed-child collapse & mobile squish).
        cards: list of (fa_icon_class, card_title, card_body_text)
        """
        t = self.theme
        pct = 48.0 if columns == 2 else 31.5
        card_nodes = []
        for icon_cls, ctitle, cbody in cards:
            card_nodes.append(
                self._container(
                    {
                        "content_width": "full",
                        "width": {"unit": "%", "size": pct, "sizes": []},
                        "width_tablet": {"unit": "%", "size": 48.0, "sizes": []},
                        "width_mobile": {"unit": "%", "size": 100, "sizes": []},
                        "flex_direction": "column",
                        "flex_align_items": "stretch",
                        "flex_gap": {"column": "10", "row": "10", "unit": "px", "isLinked": True},
                        "background_background": "classic",
                        "background_color": t.surface_bg,
                        "border_border": "solid",
                        "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
                        "border_color": t.border_subtle,
                        "border_radius": {"unit": "px", "top": "14", "right": "14", "bottom": "14", "left": "14", "isLinked": True},
                        "padding": {"unit": "px", "top": "22", "right": "20", "bottom": "22", "left": "20", "isLinked": False},
                    },
                    [
                        self._widget(
                            "icon",
                            {
                                "selected_icon": {"value": icon_cls, "library": "fa-solid"},
                                "align": "right",
                                "primary_color": t.accent_secondary,
                                "size": {"unit": "px", "size": 24, "sizes": []},
                            },
                        ),
                        self._widget(
                            "heading",
                            {
                                "title": self.clean_text(ctitle),
                                "header_size": "h3",
                                "align": "right",
                                "title_color": t.text_primary,
                                **self._typo("typography", 16, "700", 1.5),
                            },
                        ),
                        self._widget(
                            "text-editor",
                            {
                                "editor": f"<p>{self.clean_text(cbody)}</p>",
                                "align": "right",
                                "text_color": t.text_secondary,
                                **self._typo("typography", 14, "400", 1.8),
                            },
                        ),
                    ],
                    is_inner=True,
                )
            )

        grid_row = self._container(
            {
                "content_width": "full",
                "flex_direction": "row",
                "flex_direction_mobile": "column",
                "flex_wrap": "wrap",
                "flex_justify_content": "space-between",
                "flex_align_items": "stretch",
                "flex_gap": {"column": "16", "row": "16", "unit": "px", "isLinked": True},
            },
            card_nodes,
            is_inner=True,
        )

        self.elements.append(
            self._container(
                {
                    "content_width": "boxed",
                    "flex_direction": "column",
                    "flex_align_items": "stretch",
                    "flex_gap": {"column": "16", "row": "16", "unit": "px", "isLinked": True},
                    "margin": {"unit": "px", "top": "20", "right": "0", "bottom": "28", "left": "0", "isLinked": False},
                },
                [
                    self._widget(
                        "heading",
                        {
                            "title": self.clean_text(section_title),
                            "header_size": "h2",
                            "align": "right",
                            "title_color": t.text_primary,
                            **self._typo("typography", 22, "700", 1.45, size_mobile=19),
                        },
                    ),
                    grid_row,
                ],
                is_inner=False,
                title=f"کارت‌ها — {section_title[:32]}",
            )
        )

    def add_eeat_expert_card(
        self,
        name: str,
        role_badge: str,
        bio_text: str,
        avatar_url: str,
        avatar_id: int | str = "",
    ):
        """E-E-A-T author/reviewer box pairing `_flex_size: none` avatar with `_flex_size: grow` bio."""
        t = self.theme
        avatar = self._widget(
            "image",
            {
                "image": {"url": avatar_url, "id": avatar_id, "alt": self.clean_text(name), "source": "library"},
                "image_size": "thumbnail",
                "width": {"unit": "px", "size": 76, "sizes": []},
                "_element_width": "initial",
                "_element_custom_width": {"unit": "px", "size": 76, "sizes": []},
                "_flex_size": "none",
                "image_border_radius": {"unit": "px", "top": "50", "right": "50", "bottom": "50", "left": "50", "isLinked": True},
            },
        )
        bio_col = self._container(
            {
                "content_width": "full",
                "_flex_size": "grow",
                "_flex_grow": "1",
                "flex_direction": "column",
                "flex_align_items": "stretch",
                "flex_gap": {"column": "8", "row": "8", "unit": "px", "isLinked": True},
            },
            [
                self._pill_widget(role_badge),
                self._widget(
                    "heading",
                    {
                        "title": self.clean_text(name),
                        "header_size": "h3",
                        "align": "right",
                        "title_color": t.text_primary,
                        **self._typo("typography", 17, "700", 1.45),
                    },
                ),
                self._widget(
                    "text-editor",
                    {
                        "editor": f"<p>{self.clean_text(bio_text)}</p>",
                        "align": "right",
                        "text_color": t.text_secondary,
                        **self._typo("typography", 14, "400", 1.8),
                    },
                ),
            ],
            is_inner=True,
        )
        self.elements.append(
            self._container(
                {
                    "content_width": "boxed",
                    "flex_direction": "row",
                    "flex_direction_mobile": "column",
                    "flex_align_items": "center",
                    "flex_align_items_mobile": "stretch",
                    "flex_gap": {"column": "20", "row": "16", "unit": "px", "isLinked": False},
                    "background_background": "classic",
                    "background_color": t.surface_bg,
                    "border_border": "solid",
                    "border_width": {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True},
                    "border_color": t.border_subtle,
                    "border_radius": {"unit": "px", "top": "16", "right": "16", "bottom": "16", "left": "16", "isLinked": True},
                    "padding": {"unit": "px", "top": "22", "right": "24", "bottom": "22", "left": "24", "isLinked": False},
                    "margin": {"unit": "px", "top": "24", "right": "0", "bottom": "28", "left": "0", "isLinked": False},
                },
                [avatar, bio_col],
                is_inner=False,
                title=f"کارت متخصص — {name[:28]}",
            )
        )

    def add_single_column_cta(self, title: str, description: str, button_text: str, button_url: str):
        """Full-width single-column CTA banner (obeys Deadly Sin #2: no squished 2-col image CTA)."""
        t = self.theme
        self.elements.append(
            self._container(
                {
                    "content_width": "boxed",
                    "flex_direction": "column",
                    "flex_align_items": "center",
                    "flex_justify_content": "center",
                    "flex_gap": {"column": "14", "row": "14", "unit": "px", "isLinked": True},
                    "background_background": "gradient",
                    "background_color": t.accent_color,
                    "background_color_b": t.accent_secondary,
                    "background_gradient_type": "linear",
                    "background_gradient_angle": {"unit": "deg", "size": 135, "sizes": []},
                    "border_radius": {"unit": "px", "top": "16", "right": "16", "bottom": "16", "left": "16", "isLinked": True},
                    "padding": {"unit": "px", "top": "36", "right": "32", "bottom": "36", "left": "32", "isLinked": False},
                    "padding_mobile": {"unit": "px", "top": "28", "right": "20", "bottom": "28", "left": "20", "isLinked": False},
                    "margin": {"unit": "px", "top": "24", "right": "0", "bottom": "32", "left": "0", "isLinked": False},
                },
                [
                    self._widget(
                        "heading",
                        {
                            "title": self.clean_text(title),
                            "header_size": "h3",
                            "align": "center",
                            "title_color": t.cta_text_color,
                            **self._typo("typography", 21, "700", 1.5, size_mobile=18),
                        },
                    ),
                    self._widget(
                        "text-editor",
                        {
                            "editor": f'<p style="text-align:center;">{self.clean_text(description)}</p>',
                            "align": "center",
                            "text_color": t.cta_text_color,
                            **self._typo("typography", 15, "400", 1.8),
                        },
                    ),
                    self._widget(
                        "button",
                        {
                            "text": self.clean_text(button_text),
                            "link": {"url": button_url, "is_external": False, "nofollow": False},
                            "align": "center",
                            "_element_width": "auto",
                            "button_text_color": t.cta_btn_text,
                            "background_color": t.cta_btn_bg,
                            "border_radius": {"unit": "px", "top": "10", "right": "10", "bottom": "10", "left": "10", "isLinked": True},
                            "text_padding": {"unit": "px", "top": "12", "right": "28", "bottom": "12", "left": "28", "isLinked": False},
                            **self._typo("typography", 15, "700", 1.4),
                        },
                    ),
                ],
                is_inner=False,
                title=f"بنر CTA — {title[:32]}",
            )
        )

    def add_image(self, url: str, alt: str, attachment_id: int | str = "", radius_px: int = 12):
        """Uses `image_border_radius` strictly (Deadly Sin #3)."""
        self.elements.append(
            self._container(
                {
                    "content_width": "boxed",
                    "flex_direction": "column",
                    "flex_align_items": "center",
                    "margin": {"unit": "px", "top": "16", "right": "0", "bottom": "24", "left": "0", "isLinked": False},
                },
                [
                    self._widget(
                        "image",
                        {
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
                    )
                ],
                is_inner=False,
                title=f"تصویر — {alt[:32]}",
            )
        )

    def add_sources_and_faq(
        self,
        sources: list[tuple[str, str]],
        faqs: list[tuple[str, str]],
        sources_title: str = "منابع معتبر",
        faq_title: str = "پرسش‌های متداول",
    ):
        """Enforces Sources strictly BEFORE FAQ Accordion (Deadly Sin #6)."""
        t = self.theme
        if sources:
            self.elements.append(
                self._container(
                    {
                        "content_width": "boxed",
                        "flex_direction": "column",
                        "flex_align_items": "stretch",
                        "flex_gap": {"column": "12", "row": "12", "unit": "px", "isLinked": True},
                        "border_border": "solid",
                        "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
                        "border_color": t.border_subtle,
                        "padding": {"unit": "px", "top": "24", "right": "0", "bottom": "16", "left": "0", "isLinked": False},
                        "margin": {"unit": "px", "top": "28", "right": "0", "bottom": "20", "left": "0", "isLinked": False},
                    },
                    [
                        self._widget(
                            "heading",
                            {
                                "title": self.clean_text(sources_title),
                                "header_size": "h3",
                                "align": "right",
                                "title_color": t.text_muted,
                                **self._typo("typography", 15, "600", 1.5),
                            },
                        ),
                        self._widget(
                            "icon-list",
                            {
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
                        ),
                    ],
                    is_inner=False,
                    title="منابع معتبر",
                )
            )
        if faqs:
            self.elements.append(
                self._container(
                    {
                        "content_width": "boxed",
                        "flex_direction": "column",
                        "flex_align_items": "stretch",
                        "flex_gap": {"column": "14", "row": "14", "unit": "px", "isLinked": True},
                        "margin": {"unit": "px", "top": "12", "right": "0", "bottom": "36", "left": "0", "isLinked": False},
                    },
                    [
                        self._widget(
                            "heading",
                            {
                                "title": self.clean_text(faq_title),
                                "header_size": "h2",
                                "align": "right",
                                "title_color": t.text_primary,
                                **self._typo("typography", 22, "700", 1.5, size_mobile=19),
                            },
                        ),
                        self._widget(
                            "accordion",
                            {
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
                        ),
                    ],
                    is_inner=False,
                    title="پرسش‌های متداول (FAQ)",
                )
            )

    def validate(self) -> list[str]:
        """Pre-flight AST audit catching all 7 Deadly Sins + Flexbox/Navigator traps."""
        errors: list[str] = []
        seen_ids: set[str] = set()

        def walk(node: dict, parent_dir: str | None = None, depth: int = 0):
            nid = node.get("id")
            if not nid or nid in seen_ids:
                errors.append(f"Duplicate or missing id: {nid}")
            else:
                seen_ids.add(nid)

            s = node.get("settings", {})
            etype = node.get("elType")

            if etype == "container":
                if depth == 0 and not s.get("_title"):
                    errors.append(f"Top-level container {nid} missing Navigator _title")
                if depth == 0 and node.get("isInner") is not False:
                    errors.append(f"Top-level container {nid} must have isInner=False")
                if parent_dir == "row" and "width" in s and s.get("content_width") != "full":
                    errors.append(f"Row flex child {nid} has width without content_width='full'")
                if s.get("flex_direction") == "column" and "flex_align_items" not in s:
                    errors.append(f"Column container {nid} missing explicit flex_align_items")
                if "gap" in s:
                    errors.append(f"Container {nid} uses ignored 'gap' instead of 'flex_gap'")
                if "_padding" in s or "_margin" in s:
                    errors.append(f"Container {nid} uses underscored _padding/_margin")
            elif etype == "widget":
                if "elements" not in node or node["elements"] != []:
                    errors.append(f"Widget {nid} missing elements=[]")
                wtype = node.get("widgetType")
                if wtype == "heading" and s.get("header_size", "").lower() == "h1":
                    errors.append(f"Heading widget {nid} illegally uses H1")
                if wtype == "image" and ("border_radius" in s or "_border_radius" in s):
                    errors.append(f"Image widget {nid} uses border_radius instead of image_border_radius")

            for child in node.get("elements", []):
                walk(child, s.get("flex_direction"), depth + 1)

        for top in self.elements:
            walk(top, None, 0)
        return errors

    def to_json(self, indent: int | None = None) -> str:
        errs = self.validate()
        if errs:
            raise ValueError("Elementor AST validation failed:\n" + "\n".join(errs))
        return json.dumps(self.elements, ensure_ascii=False, indent=indent)


if __name__ == "__main__":
    builder = ElementorEditorialBuilder()
    builder.add_direct_answer("پاسخ سریع", "<p>نمونه خروجی کامپایلر نسخه ۲ بدون وابستگی به برند.</p>", badge_label="خلاصه کلیدی")
    builder.add_rtl_timeline("مراحل گام‌به‌گام", [("گام اول", "آماده‌سازی", "<p>بررسی اولیه و انتخاب ابزار مناسب.</p>"), ("گام دوم", "اجرای دقیق", "<p>تنظیم فاصله‌ها و تایپوگرافی استاندارد.</p>")])
    builder.add_feature_cards_row("مقایسه ویژگی‌ها", [("fas fa-check", "کارت یک", "توضیح کوتاه اول."), ("fas fa-star", "کارت دو", "توضیح کوتاه دوم."), ("fas fa-shield-alt", "کارت سه", "توضیح کوتاه سوم.")], columns=3)
    builder.add_eeat_expert_card("نام کارشناس نمونه", "بازبینی تخصصی", "توضیح کوتاه درباره سابقه و تخصص بازبین مقاله.", "https://example.com/avatar.webp", 202)
    builder.add_single_column_cta("مشاوره تخصصی", "توضیح کوتاه دعوت به اقدام.", "ثبت درخواست", "https://example.com/")
    builder.add_image("https://example.com/img.webp", "تصویر نمونه", 101)
    builder.add_sources_and_faq(
        [("منبع مرجع نمونه", "https://example.org/")],
        [("سوال نمونه؟", "پاسخ دقیق نمونه.")],
    )
    out = builder.to_json(indent=2)
    print(f"SMOKE TEST PASS! Sections={len(builder.elements)}, Bytes={len(out)}, Errors={len(builder.validate())}")
