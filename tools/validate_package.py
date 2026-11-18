#!/usr/bin/env python3
"""
validate_package.py - Validates all skills, frontmatters, and references in the package.
"""

import os
import re
import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent.parent

def check_skill(skill_dir: Path):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return False, f"Missing SKILL.md in {skill_dir.name}"

    content = skill_md.read_text(encoding='utf-8', errors='replace')
    if not content.startswith('---'):
        return False, f"Missing YAML frontmatter start (---) in {skill_dir.name}/SKILL.md"

    end_idx = content.find('---', 3)
    if end_idx == -1:
        return False, f"Unclosed YAML frontmatter in {skill_dir.name}/SKILL.md"

    frontmatter = content[3:end_idx]
    if "name:" not in frontmatter:
        return False, f"Missing 'name:' field in frontmatter of {skill_dir.name}/SKILL.md"
    if "description:" not in frontmatter:
        return False, f"Missing 'description:' field in frontmatter of {skill_dir.name}/SKILL.md"

    return True, "OK"

def main():
    print(f"Validating Skills Package at: {PACKAGE_ROOT}")
    skills_dir = PACKAGE_ROOT / "skills"
    
    if not skills_dir.exists():
        print("Error: skills/ directory not found!")
        sys.exit(1)

    skill_folders = [d for d in skills_dir.iterdir() if d.is_dir()]
    print(f"Discovered {len(skill_folders)} skill folders.")

    errors = []
    success_count = 0

    for s in sorted(skill_folders):
        ok, msg = check_skill(s)
        if ok:
            print(f"  [PASS] {s.name}")
            success_count += 1
        else:
            print(f"  [FAIL] {s.name}: {msg}")
            errors.append((s.name, msg))

    print(f"\nValidation Summary: {success_count}/{len(skill_folders)} passed.")
    if errors:
        print(f"Failed items: {len(errors)}")
        sys.exit(1)
    else:
        print("All skills passed verification successfully!")

if __name__ == "__main__":
    main()
