#!/usr/bin/env python3
"""Local, revision-preserving consultation ledger. No network dependencies."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import tempfile
import uuid
import fcntl

KINDS = ('verified', 'internal', 'unknown', 'assumption', 'decision')


def validate(doc):
    if not isinstance(doc, dict) or doc.get('schema_version') != 1 or not isinstance(doc.get('events'), list):
        raise ValueError('Unsupported or malformed session')
    seen, latest = set(), {}
    for event in doc['events']:
        if not isinstance(event, dict) or event.get('kind') not in KINDS or not event.get('claim') or not event.get('text'):
            raise ValueError('Invalid event')
        if not event.get('id') or event['id'] in seen:
            raise ValueError('Duplicate or absent event id')
        if event['kind'] == 'verified' and not (event.get('source') and event.get('scope')):
            raise ValueError('Verified claims require source and scope')
        prior = latest.get(event['claim'])
        if event.get('supersedes') != prior:
            raise ValueError('Revision must supersede the current event for the same claim')
        seen.add(event['id'])
        latest[event['claim']] = event['id']
    return doc


def load(path):
    if path.is_symlink():
        raise ValueError('Session symlinks are not accepted')
    return validate(json.loads(path.read_text(encoding='utf-8')))


def write(path, doc):
    validate(doc)
    fd, temporary = tempfile.mkstemp(prefix='.session-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(doc, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def add(doc, kind, claim, text, source='', scope='', supersedes=None):
    event = dict(id=str(uuid.uuid4()), at=dt.datetime.now(dt.timezone.utc).isoformat(),
                 kind=kind, claim=claim, text=text, source=source, scope=scope,
                 supersedes=supersedes)
    candidate = {**doc, 'events': [*doc['events'], event]}
    return validate(candidate), event['id']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    init = commands.add_parser('init')
    init.add_argument('path', type=Path)
    init.add_argument('--language', default='zh', choices=['zh', 'en', 'bilingual'])
    append = commands.add_parser('add')
    append.add_argument('path', type=Path)
    append.add_argument('--kind', required=True, choices=KINDS)
    append.add_argument('--claim', required=True)
    append.add_argument('--text', required=True)
    append.add_argument('--source', default='')
    append.add_argument('--scope', default='')
    append.add_argument('--supersedes')
    show = commands.add_parser('show')
    show.add_argument('path', type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'init':
            args.path.parent.mkdir(parents=True, exist_ok=True)
            doc = dict(schema_version=1, language=args.language, events=[])
            fd = os.open(args.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            with os.fdopen(fd, 'w', encoding='utf-8') as stream:
                json.dump(doc, stream, ensure_ascii=False, indent=2)
                stream.write('\n')
            print(args.path)
        elif args.command == 'add':
            lock_path = args.path.with_name(args.path.name + '.lock')
            fd = os.open(lock_path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
            with os.fdopen(fd, 'r+') as lock:
                fcntl.flock(lock, fcntl.LOCK_EX)
                doc, event_id = add(load(args.path), args.kind, args.claim, args.text,
                                    args.source, args.scope, args.supersedes)
                write(args.path, doc)
            print(event_id)
        else:
            doc = load(args.path)
            latest = {e['claim']: e for e in doc['events']}
            print(json.dumps(dict(language=doc['language'], current=list(latest.values()),
                                  history_events=len(doc['events'])), ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f'Error: {error}\n')


if __name__ == '__main__':
    main()
