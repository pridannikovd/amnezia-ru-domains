#!/usr/bin/env python3
"""Convert the public Amnezia domain feed into an AWG Manager text subscription."""
import argparse
import json
from pathlib import Path
import re

HOST = re.compile(r'(?=.{1,253}\Z)[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?\Z')


def convert(raw):
    rows = json.loads(raw)
    if not isinstance(rows, list) or not 1500 <= len(rows) <= 10000:
        raise ValueError('Unexpected domain-feed size')
    hosts = set()
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get('hostname'), str):
            raise ValueError('Invalid domain-feed entry')
        host = row['hostname'].lower().rstrip('.').encode('idna').decode('ascii')
        if not HOST.fullmatch(host) or '..' in host or any(len(label) > 63 for label in host.split('.')):
            raise ValueError('Invalid hostname')
        hosts.add(host)
    return '\n'.join(sorted(hosts)) + '\n'


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input', type=Path)
    p.add_argument('output', type=Path)
    args = p.parse_args()
    text = convert(args.input.read_text())
    if args.output.exists():
        old_count = len(args.output.read_text().splitlines())
        if old_count and not 0.8 <= len(text.splitlines()) / old_count <= 1.2:
            raise SystemExit('Feed changed by >20%; review before publishing')
    temporary = args.output.with_suffix(args.output.suffix + '.tmp')
    temporary.write_text(text)
    temporary.replace(args.output)
    print(f'{len(text.splitlines())} domains')
