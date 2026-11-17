#!/usr/bin/env python3
"""Install the reviewed development payload into a selected project only."""
import argparse
import json
from pathlib import Path
import shutil
import tempfile
from package import payload, digest

LOCATIONS = {'codex': '.agents/skills', 'claude': '.claude/skills', 'kimi': '.agents/skills'}


def install(project, platform, files):
    project = Path(project).resolve(strict=True)
    if not project.is_dir():
        raise ValueError('Project directory must already exist')
    destination = project / LOCATIONS[platform] / 'ai-pr-advisor'
    if any(p.is_symlink() for p in [destination, *destination.parents]
           if p == project or project in p.parents):
        raise ValueError('Destination and its parents must not be symlinks')
    if destination.exists():
        existing = {str(p.relative_to(destination)): p.read_bytes()
                    for p in destination.rglob('*') if p.is_file() and not p.is_symlink()}
        if any(p.is_symlink() for p in destination.rglob('*')) or existing != files:
            raise ValueError('Existing installation differs; review and move it aside manually')
        return destination, 'already_identical'
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix='.ai-pr-install-', dir=destination.parent))
    try:
        for name, data in files.items():
            target = temporary / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        # mkdir is an exclusive reservation: never replace an existing installation.
        destination.mkdir()
        for child in temporary.iterdir():
            shutil.move(str(child), str(destination / child.name))
    finally:
        shutil.rmtree(temporary)
    return destination, 'installed'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--platform', choices=LOCATIONS, required=True)
    args = parser.parse_args()
    try:
        files = payload()
        destination, status = install(args.project, args.platform, files)
        print(json.dumps(dict(status=status, destination=str(destination), sha256=digest(files)), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(2, f'Error: {error}\n')


if __name__ == '__main__':
    main()
