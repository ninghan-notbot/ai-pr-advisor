#!/usr/bin/env python3
"""Structural checks only; these do not certify professional advice quality."""
import json
from pathlib import Path
import re
from package import ROOT, payload


def main():
    files = payload()
    text = files['SKILL.md'].decode()
    assert text.startswith('---\n')
    header, body = text[4:].split('\n---\n', 1)
    assert re.search(r'^name: ai-pr-advisor$', header, re.M)
    desc = re.search(r'^description: (.+)$', header, re.M).group(1)
    assert 1 <= len(desc) <= 1024
    for name, data in files.items():
        if name.endswith('.md'):
            for link in re.findall(r'\]\(([^)]+)\)', data.decode()):
                if '://' not in link and not link.startswith('#'):
                    resolved = (ROOT / name).parent / link.split('#')[0]
                    assert resolved.is_file(), f'Broken link {name}: {link}'
    media = json.loads(files['references/media-examples.json'])
    for entry in media['entries']:
        assert entry['route'] in {'independent_editorial', 'paid_brand_content', 'press_release_distribution'}
        price = entry['price']
        if price.get('amount') is not None:
            assert price.get('source') and price.get('currency') and price.get('verified_on') and price.get('conditions')
    status = json.loads((ROOT / 'release-status.json').read_text())
    assert not status['public_release_authorized']
    print(json.dumps({'structural_validation': 'PASS', 'package_files': len(files),
                      'skill_lines': len(text.splitlines()), 'professional_quality': 'UNVERIFIED'}))


if __name__ == '__main__':
    main()
