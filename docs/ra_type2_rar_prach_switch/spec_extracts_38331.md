# 38.331 spec extracts used (paths + regeneration)

To avoid loading the entire spec HTML into context, we extract only the needed sections from `docs/38331-i60.html` using the repo’s spec tools.

## Extracted files (generated)

Generated under `artifacts/spec_sections/`:

- `artifacts/spec_sections/38331-i60__sib1.md` (SIB1 container + definition)
- `artifacts/spec_sections/38331-i60__servingcellconfigcommonsib.md` (SIB1 serving cell common config)
- `artifacts/spec_sections/38331-i60__uplinkconfigcommonsib.md` (SIB1 UL common config)
- `artifacts/spec_sections/38331-i60__bwp-uplinkcommon.md` (where `rach-ConfigCommon` is carried)
- `artifacts/spec_sections/38331-i60__rach-configcommon.md` (4-step RA common config)
- `artifacts/spec_sections/38331-i60__rach-configgeneric.md` (4-step RA generic PRACH params)

Context / comparison sections (already-existing “two-step RA” & multi-RACH patterns):

- `artifacts/spec_sections/38331-i60__rach-configcommontwostepra.md`
- `artifacts/spec_sections/38331-i60__rach-configgenerictwostepra.md`
- `artifacts/spec_sections/38331-i60__rach-configtwota.md`

## Regeneration commands

Run from repo root:

```bash
source .venv/bin/activate

asntools-spec-extract 38331-i60 sib1                    --format md --include-heading --out-dir artifacts/spec_sections
asntools-spec-extract 38331-i60 servingcellconfigcommonsib --format md --include-heading --out-dir artifacts/spec_sections
asntools-spec-extract 38331-i60 uplinkconfigcommonsib   --format md --include-heading --out-dir artifacts/spec_sections
asntools-spec-extract 38331-i60 bwp-uplinkcommon         --format md --include-heading --out-dir artifacts/spec_sections

asntools-spec-extract 38331-i60 rach-configcommon        --format md --include-heading --out-dir artifacts/spec_sections
asntools-spec-extract 38331-i60 rach-configgeneric       --format md --include-heading --out-dir artifacts/spec_sections

asntools-spec-extract 38331-i60 rach-configcommontwostepra   --format md --include-heading --out-dir artifacts/spec_sections
asntools-spec-extract 38331-i60 rach-configgenerictwostepra  --format md --include-heading --out-dir artifacts/spec_sections
asntools-spec-extract 38331-i60 rach-configtwota             --format md --include-heading --out-dir artifacts/spec_sections
```

