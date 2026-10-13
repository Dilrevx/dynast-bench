# DynAST dataset maintenance

This branch contains canonical benchmark data, not the upstream authoring workspace. The native files remain traceable at the commit recorded in dataset/manifest.json.

- Preserve original asset bytes, executable modes, labels, notices and vulnerable/fixed relationships. Do not repair intentionally insecure source code.
- Source assets contain answer-bearing annotations; labels and reference PoCs are not blind model input. Retain source gates until a separately audited projection exists.
- Do not execute applications, containers or PoCs as part of format validation. Runtime execution requires an explicitly scoped isolated test; never expose these applications publicly, and preserve the original loopback bindings and resource limits.
- Keep dataset/ the single data entry point. Methods and evaluation commands belong to embed; do not add parallel native exports or process documents here.
