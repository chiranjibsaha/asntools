ASNT Tools (NR-RRC ASN.1)
==========================

Python utilities for inspecting, merging, and serving 3GPP NR‑RRC ASN.1 using pycrate.

Quick Start (Linux/macOS)
-------------------------
1) Python 3.11+ and Git installed.  
2) Create & activate venv:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3) Install deps (plus dev tools):
   ```
   python -m pip install --upgrade pip
   python -m pip install -e .[dev]
   ```
4) Run tests to validate:
   ```
   pytest
   ```

Windows Setup
-------------
- See `docs/windows_setup.rst` for the step‑by‑step PowerShell flow (Git, Python, venv, install, pytest).

Core CLI Usage
--------------
- Fetch Wireshark NR-RRC ASN.1:
  ```
  python -m asntools.fetch_asn1 --output asn1/NR-RRC-Definitions.asn
  ```
- Compile ASN.1 to pycrate modules:
  ```
  python -m asntools.compile_rrc --asn1-path asn1/NR-RRC-Definitions.asn
  ```
- One-shot merge + compile (accepts multiple ASN files and directories):
  ```
  asntools --compile --asnfiles path/to/file1.asn --asnfiles path/to/file2.asn --input-dir asn_sources
  ```
- Use a compile setup file (e.g., checked into your repo) to list ASN.1 and field description sources:
  ```
  {
    "asnfiles": [
      "/data/specs/NR-RRC-Definitions.asn",
      "/data/specs/LPP.asn"
    ],
    "field_descriptions": [
      "/data/specs/field_descriptions.json",
      "/data/custom/overrides.json"
    ]
  }
  ```
  Then run:
  ```
  asntools --compile --compile-setup compile_setup.json
  ```
- Search ASN text:
  ```
  asntools --grep "RACH-Config"
  ```
- Describe an IE:
  ```
  asntools --show RACH-ConfigGeneric
  ```
- Tree back from a leaf IE:
  ```
  asntools --tree pdcch-ConfigCommon --tree-pretty
  ```
- Serve HTTP API (FastAPI):
  ```
  asntools --serve --host 0.0.0.0 --port 8080
  ```

Project Layout
--------------
- `asntools/` library code
- `scripts/` and CLI entry points
- `asn1/` input ASN.1; `pycrate_asn1dir/` generated modules
- `docs/` additional docs; `tests/` pytest suite; `artifacts/` generated outputs

Notes
-----
- The CLI auto-compiles modules when missing; pass `--no-compile` to skip.
- For SSH cloning on Windows, ensure your key is in `~/.ssh` and registered with your host.
