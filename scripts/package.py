#!/usr/bin/env python3
"""Build the standalone skill, Claude .skill, and dual-runtime plugin release archives."""
import argparse
from pathlib import Path
import zipfile
from check import ROOT, PLUGIN, SKILL, check


def package(root=ROOT, output=None):
    check(root)
    output = output or root / 'dist'
    output.mkdir(parents=True, exist_ok=True)
    skill = root / 'skills' / SKILL
    license_file = root / 'LICENSE'
    archives = []
    # Each source is (path, base): members are named prefix + path relative to base.
    for name, sources, prefix in [
        (f'{SKILL}-skill.zip', [(skill, skill), (license_file, root)], ''),
        (f'{SKILL}.skill', [(skill, skill), (license_file, root)], SKILL + '/'),
        (f'{SKILL}-plugin.zip', [(root / path, root) for path in ('plugin.json', '.claude-plugin/plugin.json', '.codex-plugin/plugin.json', 'skills', 'LICENSE')], PLUGIN + '/'),
    ]:
        destination = output / name
        with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as archive:
            for source, base in sources:
                files = sorted(source.rglob('*')) if source.is_dir() else [source]
                for file in files:
                    if not file.is_file() or any(part.startswith('.') or part == '__pycache__' for part in file.relative_to(source if source.is_dir() else source.parent).parts):
                        continue
                    archive.write(file, prefix + file.relative_to(base).as_posix())
        archives.append(destination)
    return archives

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='output directory (default: repository dist/)')
    args = parser.parse_args()
    for path in package(output=args.output):
        print(path)
