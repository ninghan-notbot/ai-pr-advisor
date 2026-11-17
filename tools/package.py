#!/usr/bin/env python3
"""Build an allowlisted development archive; never publish or change visibility."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SECRET = re.compile(r'(?<![A-Za-z0-9])(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)')


def payload(root=ROOT):
    root = Path(root).resolve(strict=True)
    names = json.loads((root / 'package-files.json').read_text())
    if not isinstance(names, list) or not names or len(names) != len(set(names)):
        raise ValueError('Manifest must be a nonempty unique list')
    result = {}
    for name in names:
        parts = PurePosixPath(name)
        if parts.is_absolute() or '..' in parts.parts or '\\' in name:
            raise ValueError('Unsafe package path')
        path = root / name
        if any(parent.is_symlink() for parent in [path, *path.parents]
               if parent == root or root in parent.parents):
            raise ValueError(f'Symlink rejected: {name}')
        if not path.is_file() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f'Missing or external package file: {name}')
        data = path.read_bytes()
        text = data.decode('utf-8')
        if SECRET.search(text) or '/Volumes/' in text or '/Users/' in text:
            raise ValueError(f'Private path or credential pattern: {name}')
        result[name] = data
    return result


def digest(files):
    return {name: hashlib.sha256(data).hexdigest() for name, data in sorted(files.items())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--release', action='store_true')
    parser.add_argument('--layout', choices=['directory', 'flat'], default='directory',
                        help='flat places SKILL.md at ZIP root for importers that require it')
    args = parser.parse_args()
    try:
        if args.release:
            raise ValueError('This tool prepares local candidates only; publication requires owner approval')
        files = payload()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.output, 'x', zipfile.ZIP_DEFLATED) as archive:
            for name, data in sorted(files.items()):
                prefix = 'ai-pr-advisor/' if args.layout == 'directory' else ''
                info = zipfile.ZipInfo(prefix + name, date_time=(2026, 11, 17, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data)
        print(json.dumps({'status': 'local_candidate_archive', 'layout': args.layout, 'output': str(args.output),
                          'files': digest(files)}, indent=2))
    except (OSError, ValueError) as error:
        parser.exit(2, f'Error: {error}\n')


if __name__ == '__main__':
    main()
