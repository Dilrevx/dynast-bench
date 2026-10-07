#!/usr/bin/env python3
"""Generate the additive v1 inventory using the reviewed embed adapter.

No upstream executable is imported or launched. PyYAML is a parser dependency.
Existing output must be byte-identical; this command never overwrites changes.
"""
import argparse
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--embed-src', type=Path, required=True)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    sys.path.insert(0, str(args.embed_src.resolve()))
    from embedbench.benchmarks import GitSnapshot
    from embedbench.dynast import UPSTREAM_COMMIT, normalize, original_blobs
    root = Path(__file__).resolve().parents[2]
    snapshot = GitSnapshot(root, UPSTREAM_COMMIT)
    blobs, entries = original_blobs(snapshot)
    artifacts = normalize(blobs, entries)
    for relative, body in artifacts.items():
        output = root / relative
        if output.exists():
            if output.read_bytes() != body:
                raise ValueError('Existing normalization differs: ' + relative)
        elif args.check:
            raise ValueError('Missing normalization: ' + relative)
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            with output.open('xb') as handle:
                handle.write(body)
    print('Verified' if args.check else 'Generated', len(artifacts), 'deterministic inventory artifacts')


if __name__ == '__main__':
    main()
