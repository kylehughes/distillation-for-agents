#!/usr/bin/env python3
"""Validate this repository's deliberately small, shared plugin format."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'distillation-for-agents'
SKILL = 'distill'
SEMVER = re.compile(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\Z')


def scalar_fields(text):
    """Read authored single-line YAML scalars, not arbitrary YAML."""
    fields = {}
    for line in text.splitlines():
        match = re.fullmatch(r'\s*([a-z_]+):\s*(.+?)\s*', line)
        if match:
            value = match[2]
            if value.startswith('"'):
                value = json.loads(value)
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1].replace("''", "'")
            fields[match[1]] = value
    return fields


def frontmatter_fields(text):
    """Read top-level frontmatter keys, folding `>`/`>-` and `|`/`|-` block scalars into one string."""
    fields, key, block = {}, None, None
    for line in text.splitlines():
        match = re.fullmatch(r'([A-Za-z0-9_-]+):(?:\s+(.*?))?\s*', line)
        if match:
            key, value = match[1], match[2] or ''
            block = [] if value in ('>', '>-', '|', '|-') else None
            fields[key] = scalar_fields(f'{key}: {value}').get(key, '') if block is None else ''
        elif block is not None and line.strip():
            block.append(line.strip())
            fields[key] = ' '.join(block)
    return fields


# The .skill upload format accepts only these keys and limits (skill-creator's quick_validate).
SKILL_KEYS = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}


def check(root=ROOT, expected_version=None):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    def load(relative):
        return json.loads((root / relative).read_text())
    claude = load('.claude-plugin/plugin.json')
    codex = load('.codex-plugin/plugin.json')
    portable = load('plugin.json')
    market = load('.claude-plugin/marketplace.json')
    cm = load('.agents/plugins/marketplace.json')
    for label, data in [('Claude', claude), ('Codex', codex), ('Portable', portable)]:
        require(data.get('name') == PLUGIN, f'{label} plugin name must be {PLUGIN}')
    require(market.get('name') == PLUGIN and cm.get('name') == PLUGIN, 'marketplace identities must match plugin')
    require(len(market.get('plugins', [])) == 1 and len(cm.get('plugins', [])) == 1, 'both marketplaces must contain exactly one plugin')
    entry, centry = market['plugins'][0], cm['plugins'][0]
    require(entry.get('name') == PLUGIN and centry.get('name') == PLUGIN, 'marketplace entry identities must match plugin')
    versions = [portable.get('version'), claude.get('version'), codex.get('version'), market.get('metadata', {}).get('version'), entry.get('version')]
    require(all(isinstance(v, str) and SEMVER.fullmatch(v) for v in versions), 'versions must be numeric X.Y.Z without leading zeros')
    require(len(set(versions)) == 1, f'versions differ: {versions}')
    if expected_version is not None:
        require(all(v == expected_version for v in versions), f'tag {expected_version!r} must equal all manifest versions')
    require(portable.get('description') == claude.get('description') == codex.get('description') == entry.get('description'), 'plugin descriptions must match')
    require(entry.get('source') == './', 'Claude marketplace source must be ./')
    require(centry.get('source') == {'source': 'local', 'path': './'}, 'Codex marketplace source must be local ./')
    require(codex.get('skills') == './skills/', 'Codex skills path must be ./skills/')
    require(entry.get('strict') is not False, 'Claude entry must use the plugin manifest, not strict:false')
    skill = root / 'skills' / SKILL
    text = (skill / 'SKILL.md').read_text()
    require(text.startswith('---\n') and '\n---\n' in text[4:], 'SKILL.md requires YAML frontmatter')
    fields = frontmatter_fields(text.split('---', 2)[1])
    require(fields.get('name') == SKILL, 'skill name must match directory')
    require(re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', SKILL) and len(SKILL) <= 64, 'skill name must be kebab-case, at most 64 characters')
    description = fields.get('description', '')
    require(bool(description), 'skill description is required')
    require(len(description) <= 1024 and not re.search('[<>]', description), 'skill description must be at most 1024 characters without angle brackets')
    require(set(fields) <= SKILL_KEYS, f'unsupported SKILL.md frontmatter keys: {sorted(set(fields) - SKILL_KEYS)}')
    ui = scalar_fields((skill / 'agents/openai.yaml').read_text())
    for field in ('display_name', 'short_description', 'default_prompt'):
        require(bool(ui.get(field)), f'skill UI requires {field}')
    require(f'${SKILL}' in ui.get('default_prompt', ''), 'UI prompt must invoke the skill')
    require((root / 'LICENSE').is_file(), 'LICENSE is required')
    for file in (root / 'skills').rglob('*.md'):
        for target in re.findall(r'\]\(([^\s)]+)\)', file.read_text()):
            path = unquote(urlsplit(target.strip('<>')).path)
            if path and not urlsplit(target).scheme:
                resolved = (file.parent / path).resolve()
                require(resolved.is_relative_to(root.resolve()) and resolved.exists(), f'{file.relative_to(root)}: broken or escaping link {target}')
    if errors:
        raise ValueError('\n'.join(errors))
    return versions[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', help='require every manifest version to equal this release tag')
    args = parser.parse_args()
    try:
        version = check(expected_version=args.version)
    except (ValueError, OSError, KeyError, IndexError, TypeError) as error:
        parser.exit(1, f'Validation failed: {error}\n')
    print(f'Validated {PLUGIN} {version}')

if __name__ == '__main__':
    main()
