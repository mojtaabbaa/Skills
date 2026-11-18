#!/usr/bin/env python3
"""
validate_all_skills.py - Validates all skills across all categorized folders in the repository.
"""

import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

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
    print(f"Validating Categorized Skills Repository at: {REPO_ROOT}\n")
    
    categories = sorted([d for d in REPO_ROOT.iterdir() if d.is_dir() and d.name.startswith(('01-', '02-', '03-', '04-', '05-', '06-'))])
    
    total_skills = 0
    passed_skills = 0
    errors = []

    for cat in categories:
        skills_dir = cat / "skills"
        if not skills_dir.exists():
            continue
        
        cat_skills = sorted([d for d in skills_dir.iterdir() if d.is_dir()])
        print(f"=== Category: {cat.name} ({len(cat_skills)} skills) ===")
        
        for s in cat_skills:
            total_skills += 1
            ok, msg = check_skill(s)
            if ok:
                print(f"  [PASS] {s.name}")
                passed_skills += 1
            else:
                print(f"  [FAIL] {s.name}: {msg}")
                errors.append((cat.name, s.name, msg))
        print()

    print(f"Summary: {passed_skills}/{total_skills} skills successfully passed verification.")
    if errors:
        print(f"\n{len(errors)} skills failed verification:")
        for cat, s, msg in errors:
            print(f"  - [{cat}] {s}: {msg}")
        sys.exit(1)
    else:
        print("All categorized skills are 100% compliant and ready for production!")

if __name__ == "__main__":
    main()
