# DynAST normalized inventory v1

This additive layer preserves every upstream tracked file and its Git history at
`998d9c4cf2f65b660fc4655a9e7b34354e449aaa`. The upstream MIT license and all
original third-party notices remain unchanged. No target or PoC was executed.

`datasets/dynast/` contains evaluator-only normalized labels, per-app inventories,
the complete original-file provenance manifest, and a computed summary. The
original `VULNERABILITIES.yaml` records remain authoritative, including their
complete annotations, variant paths, match anchors, and reference PoC metadata.
This is not a detector result, semantic review, or safety certification.

Computed inventory: 19 apps / 38 variants; 549 vulnerability labels and 146
near-miss labels; 594 cataloged operations; 546 distinct referenced PoC paths;
1,785 unchanged original Git entries. There are 1,244 label bindings: 549
vulnerable, 549 author-safe twin (547 present, 2 documented absent), and 146
near-miss (119 vulnerable-variant, 26 safe-variant, 1 reference artifact).
The 1,022 app-variant files exclude the unused `_template` skeleton.
Of 507 supplied ranges, 366 are physical-line ranges and 141 include the
terminal empty line. No source execution or semantic verification is claimed.

Forty-six answer-key entries repeat `discovery` with an identical scalar. The
normalizer permits only that exact non-conflicting key duplication, records both
line locations in each app's `yaml_duplicate_keys`, and rejects every other
duplicate. Original YAML is unchanged. Several upstream README per-app counts
are stale; normalized counts are reconstructed from pinned YAML, not that table.

The inventory distinguishes vulnerability labels, author-safe twin observations,
and near-miss observations. A near-miss binds only its authored path (some are
safe-only and one is an evaluator reference); a counterpart file is not silently
labeled safe. Source-range validation follows the author's LF-split convention (which
can include a terminal empty line), records the exact author range and hashed
physical bytes, and does not infer safe-twin line ranges. Two safe artifacts are
absent as documented fixes; absent files are never invented as negative snippets.

## Model boundary

**Raw source export is blocked.** Merely excluding `ground-truth/` would still
leak the answers through inline bug IDs and explanations, variant names,
`SAFE_MODE` switches, served documentation, and source maps. V1 has no audited
sanitized source projection and exports zero model source files. A new version
must preserve program meaning, review leakage beyond comments, and publish
original-to-projection file/line mappings before a blind source experiment.
Never put this repository, normalized labels, manifests with label-selected
paths, PoCs, or evaluator export in a model-accessible sandbox.

## Reproduction

Use Python 3 with the already-available PyYAML parser and the reviewed `embed`
integration source; this script performs no automatic installation:

```sh
python3 normalization/dynast/normalize.py --embed-src /path/to/embed/src --check
```

Omit `--check` only to create missing additive files. Existing differing outputs
are refused. The generator reads pinned Git objects rather than mutable working
tree source, and does not import or execute any upstream application code.
