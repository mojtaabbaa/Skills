#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI Tool: inspect_widget.py
Inspects any Elementor Core (v4.2.3+) or Elementor Pro (v4.3.2+) widget directly from
the authoritative PHP source tree (Source Code Fallback Directive).

Usage:
    python inspect_widget.py <widget_name> [--source-dir <path>]
Examples:
    python inspect_widget.py image
    python inspect_widget.py call-to-action
    python inspect_widget.py loop-grid
"""

import argparse
import os
import re
import sys

DEFAULT_SOURCE_ROOT = os.environ.get("ELEMENTOR_SOURCE_ROOT", "./elementor-source")


def get_search_paths(source_root: str):
    return [
        os.path.join(source_root, "elementor", "includes", "widgets"),
        os.path.join(source_root, "elementor", "modules"),
        os.path.join(source_root, "elementor-pro", "modules"),
    ]


def find_widget_files(name: str, source_root: str):
    clean = name.lower().replace("_", "-")
    alt = name.lower().replace("-", "_")
    exact_matches = []
    partial_matches = []

    for base in get_search_paths(source_root):
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for fn in files:
                if not fn.endswith(".php"):
                    continue
                fl = fn.lower()
                fp = os.path.join(root, fn)
                if fl in (f"{clean}.php", f"{alt}.php", f"widget-{clean}.php"):
                    exact_matches.append(fp)
                elif (clean in fl or alt in fl) and ("widget" in root.lower() or "widgets" in root.lower()):
                    partial_matches.append(fp)
    return exact_matches or partial_matches


def extract_controls(file_path: str):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

    controls = []
    pattern = re.compile(
        r"\$this->(add_control|add_responsive_control|add_group_control)\(\s*([^,]+?)\s*,\s*\[(.*?)\]\s*\);",
        re.DOTALL,
    )
    for m in pattern.finditer(code):
        method = m.group(1)
        raw_first = m.group(2).strip().strip("'\"")
        body = m.group(3)

        if method == "add_group_control":
            n_match = re.search(r"['\"]name['\"]\s*=>\s*['\"]([^'\"]+)['\"]", body)
            c_name = n_match.group(1) if n_match else raw_first
            c_type = f"GROUP({raw_first})"
            c_default = "-"
        else:
            c_name = raw_first
            t_match = re.search(r"['\"]type['\"]\s*=>\s*([^,\n\]]+)", body)
            c_type = t_match.group(1).strip() if t_match else "UNKNOWN"
            if method == "add_responsive_control":
                c_type = f"RESPONSIVE:{c_type}"
            d_match = re.search(r"['\"]default['\"]\s*=>\s*([^,\n\]]+)", body)
            c_default = d_match.group(1).strip() if d_match else "NONE"

        controls.append({"name": c_name, "type": c_type, "default": c_default})
    return controls


def main():
    parser = argparse.ArgumentParser(description="Inspect Elementor widget controls directly from PHP source.")
    parser.add_argument("widget_name", help="Widget slug (e.g. image, heading, call-to-action, loop-grid)")
    parser.add_argument("--source-dir", default=DEFAULT_SOURCE_ROOT, help="Root containing elementor/ and elementor-pro/")
    args = parser.parse_args()

    matches = find_widget_files(args.widget_name, args.source_dir)
    if not matches:
        print(f"Widget '{args.widget_name}' not found under: {args.source_dir}")
        sys.exit(1)

    target = matches[0]
    print(f"Source file: {target}")
    if len(matches) > 1:
        print(f"(Other candidates: {len(matches) - 1})")
    controls = extract_controls(target)
    print(f"Found {len(controls)} control declarations:")
    for c in controls:
        print(f" - {c['name']:34} | {c['type']:34} | Default: {c['default']}")


if __name__ == "__main__":
    main()
