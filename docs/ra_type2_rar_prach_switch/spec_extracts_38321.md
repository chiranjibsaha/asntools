# 38.321 spec extracts used (paths + regeneration)

To avoid loading the entire spec HTML into context, we extract only the needed sections from `docs/38321-j00.html` using the repo’s spec tools.

## Extracted files (generated)

Generated under `artifacts/spec_sections/`:

- `artifacts/spec_sections/38321-j00__5-1-random-access-procedure.md` (TS 38.321 §5.1)
- `artifacts/spec_sections/38321-j00__6-1-5-mac-pdu-random-access-response.md` (TS 38.321 §6.1.5)
- `artifacts/spec_sections/38321-j00__6-1-5-a-mac-pdu-msgb.md` (TS 38.321 §6.1.5a)

Additional RAR-structure sections (needed for Type-2 MAC RAR encoding decisions):

- `artifacts/spec_sections/38321-j00__6-2-2-mac-subheader-for-random-access-response.md` (TS 38.321 §6.2.2)
- `artifacts/spec_sections/38321-j00__6-2-3-mac-payload-for-random-access-response.md` (TS 38.321 §6.2.3)

## Regeneration commands

Run from repo root:

```bash
source .venv/bin/activate

asntools-spec-extract 38321-j00 5.1     --format md --include-heading --out-dir artifacts/spec_sections
asntools-spec-extract 38321-j00 6.1.5   --format md --include-heading --out-dir artifacts/spec_sections
asntools-spec-extract 38321-j00 6-1-5-a-mac-pdu-msgb --format md --include-heading --out-dir artifacts/spec_sections

asntools-spec-extract 38321-j00 6.2.2   --format md --include-heading --out-dir artifacts/spec_sections
asntools-spec-extract 38321-j00 6.2.3   --format md --include-heading --out-dir artifacts/spec_sections
```

