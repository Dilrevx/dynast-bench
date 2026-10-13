# DynAST benchmark dataset

549 authored vulnerability labels and 146 near-miss labels across 19 applications, with 38 vulnerable/fixed source trees. Label entries are not independent real CVEs; safe twins are mechanism-specific controls.

[Cases](dataset/cases.jsonl) and [manifest](dataset/manifest.json) are the data entry points. The manifest binds complete source trees, runtime context, operation catalogues, reference PoCs and original file modes/hashes. Annotated sources remain gated from blind model input.

Typed operation catalogues preserve 594 operations and their case relationships. LLM categories, network segments/open expectations and documented API versions are retained alongside the source labels.

This dataset contains deliberately insecure applications. Never deploy them on a public network. Runtime assets and reference PoCs are preserved data, not a claim of executed confirmation.

From [embed](https://github.com/Dilrevx/embed/tree/spec-audit-ab):

```sh
PYTHONPATH=src python3 -m embedbench validate-dataset \\
  --benchmark-checkout ../dynast-bench --lock benchmarks/dynast/dataset-lock.json
```

The [fixed dataset lock](https://github.com/Dilrevx/embed/blob/spec-audit-ab/benchmarks/dynast/dataset-lock.json) and [shared runner](https://github.com/Dilrevx/embed/blob/spec-audit-ab/docs/method-runner.md) define evaluation inputs and label handling.

Native input: [cd660d8295b61cb99787e641938d358bea1c2086](https://github.com/Dilrevx/dynast-bench/tree/cd660d8295b61cb99787e641938d358bea1c2086). Upstream provenance is retained in the manifest and each case; original bytes are preserved in assets. [MIT licence](LICENSE) and embedded notices remain unchanged.
