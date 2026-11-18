#!/usr/bin/env python3
"""
build_safe_zip.py - Safe WordPress & Skills ZIP Archive Builder
---------------------------------------------------------------
Ensures that all archive paths inside the ZIP file strictly use POSIX
forward slashes ('/'), preventing fatal extraction failures in WordPress's
unzip_file() on Linux/cPanel servers when built from a Windows machine.
"""

import os
import sys
import zipfile
import argparse
from pathlib import Path

EXCLUDE_PATTERNS = {
    '.git', '.svn', '.hg', '.vscode', '.idea',
    '__pycache__', '.pytest_cache', '.DS_Store', 'Thumbs.db',
    'node_modules', '*.tmp', '*.log'
}

def should_exclude(rel_path_str: str) -> bool:
    parts = rel_path_str.replace('\\', '/').split('/')
    for part in parts:
        if part in EXCLUDE_PATTERNS or part.startswith('.'):
            return True
        if part.endswith('.tmp') or part.endswith('.log'):
            return True
    return False

def create_safe_zip(source_dir: Path, output_zip: Path, root_folder_name: str = None):
    source_dir = source_dir.resolve()
    output_zip = output_zip.resolve()

    if not source_dir.is_dir():
        print(f"Error: Source directory {source_dir} does not exist.")
        sys.exit(1)

    output_zip.parent.mkdir(parents=True, exist_ok=True)

    print(f"Packaging: {source_dir}")
    print(f"Destination: {output_zip}")

    count = 0
    with zipfile.ZipFile(output_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                full_path = Path(root) / file
                rel_path = full_path.relative_to(source_dir)
                rel_str = str(rel_path).replace('\\', '/')

                if should_exclude(rel_str):
                    continue

                if root_folder_name:
                    arcname = f"{root_folder_name}/{rel_str}"
                else:
                    arcname = rel_str

                # Explicitly enforce forward slashes in ZipInfo
                zinfo = zipfile.ZipInfo(arcname)
                zinfo.compress_type = zipfile.ZIP_DEFLATED
                # Read file data
                with open(full_path, 'rb') as f:
                    data = f.read()
                zf.writestr(zinfo, data)
                count += 1

    print(f"Successfully packaged {count} files into {output_zip.name} with strict forward slashes ('/').")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build safe ZIP archive for WordPress / Antigravity.")
    parser.add_argument("source", type=str, help="Source directory to pack")
    parser.add_argument("output", type=str, help="Output ZIP file path")
    parser.add_argument("--root", type=str, default=None, help="Optional top-level folder name inside ZIP")

    args = parser.parse_args()
    create_safe_zip(Path(args.source), Path(args.output), args.root)
