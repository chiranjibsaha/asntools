<INSTRUCTIONS>
# Scope: docs/ra_type2_rar_prach_switch

This folder captures design notes for a proposed Random Access enhancement (new Type-2 RAR triggering a second Msg1 with PHY pre-compensation).

## Writing conventions
- Keep docs in Markdown.
- Prefer concrete clause hooks into TS 38.321 (e.g., "5.1.4 Random Access Response reception").
- When proposing spec text, separate:
  - "Normative deltas" (shall/shall not) vs
  - "Design notes / rationale" (informative).

## Terminology
- Use existing 38.321 terms where possible: "Random Access procedure", "Random Access Preamble", "RA-RNTI", "PREAMBLE_INDEX", "ra-ResponseWindow".
- For new items, use stable placeholders (e.g., "Type-2 RAR (proposed)"), and keep a short glossary section.

## Outputs
- Maintain a single source-of-truth delta list for 38.321 in `mac_procedure_deltas.md`.
- Track open items (fields, timers, counters, fallback rules) in `open_questions.md`.
</INSTRUCTIONS>
