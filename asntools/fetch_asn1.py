"""Fetch NR-RRC ASN.1 definitions from the Wireshark repo."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import click
import requests

from . import DEFAULT_ASN1_PATH
from .logging_utils import setup_logging

WIRESHARK_ASN1_URL = (
    "https://gitlab.com/wireshark/wireshark/-/raw/{ref}/epan/dissectors/asn1/nr-rrc/NR-RRC-Definitions.asn"
)


def download_nr_rrc_asn1(destination: Path, ref: str = "master") -> Path:
    """Download NR-RRC-Definitions.asn to *destination*.

    Args:
        destination: Path where the ASN.1 file should be stored.
        ref: Git reference (branch/tag/commit) in the Wireshark repo.
    Returns:
        Path to the downloaded file.
    """

    destination.parent.mkdir(parents=True, exist_ok=True)
    url = WIRESHARK_ASN1_URL.format(ref=ref)
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    destination.write_bytes(response.content)
    return destination


@click.command()
@click.option("--output", "output_path", type=click.Path(path_type=Path), default=DEFAULT_ASN1_PATH, help="Destination .asn file")
@click.option("--ref", default="master", show_default=True, help="Wireshark git ref to fetch from")
def main(output_path: Path, ref: str) -> None:
    """CLI entrypoint for fetching NR-RRC ASN.1."""

    logger = setup_logging()
    try:
        path = download_nr_rrc_asn1(output_path, ref=ref)
    except Exception as exc:  # pragma: no cover - log then re-raise to click
        logger.exception("Failed to download NR-RRC ASN.1 (ref=%s, output=%s)", ref, output_path)
        raise
    click.echo(f"Downloaded NR-RRC ASN.1 to {path}")


if __name__ == "__main__":  # pragma: no cover
    main()
