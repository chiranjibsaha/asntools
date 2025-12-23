# Repository Guidelines

This repository contains Python tooling around 3GPP NR‑RRC ASN.1 (Wireshark `NR-RRC-Definitions.asn`) and pycrate-based introspection.

## Project Structure & Module Organization
- Place library code under `asntools/` (e.g. `asntools/rrc_introspect.py`).
- Put command-line entrypoints and small scripts in `bin/` or `scripts/`.
- Store ASN.1 inputs under `asn1/` and generated pycrate modules under `pycrate_asn1dir/`.
- Keep documentation in `project.md` and additional docs in `docs/` if needed.
- Put automated tests in `tests/` mirroring the package structure.

## Build, Test, and Development Commands
- Use a virtual environment (`python -m venv .venv && source .venv/bin/activate`).
- Install dependencies: `pip install -e .[dev]` (or see `pyproject.toml` / `requirements*.txt`).
- Run tests: `pytest` from the repository root.
- Optional helpers (if present): `make lint`, `make test`, or `make format`.

## Coding Style & Naming Conventions
- Use 4‑space indentation and standard Python 3 type hints.
- Prefer explicit, descriptive names (`rach_config_json`, not `rcj`).
- Modules and packages: `snake_case`; classes: `PascalCase`; functions/variables: `snake_case`.
- Keep functions small and focused; prefer pure functions where practical.

## Testing Guidelines
- Use `pytest` with tests under `tests/` named `test_*.py`.
- Write tests for new behavior and edge cases (e.g. missing IE, bad ASN.1 path).
- When changing behavior, update or add tests to reflect the new contract.

## Commit & Pull Request Guidelines
- Write clear commit messages: short imperative subject, optional body (e.g. `add RRC IE JSON introspection`).
- Group related changes in a single commit; avoid mixing refactors with feature work.
- Pull requests should describe purpose, key changes, and how to exercise or test the feature.
- Reference related issues where applicable and include sample commands or outputs for reviewers.

