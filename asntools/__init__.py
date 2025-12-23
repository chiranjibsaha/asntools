"""Top-level package for NR-RRC ASN.1 tooling."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("asntools")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"

DEFAULT_ASN1_PATH = "asn1/NR-RRC-Definitions.asn"
DEFAULT_OUTPUT_DIR = "pycrate_asn1dir"
DEFAULT_FIELD_DESCRIPTION_PATH = "asn1/field_descriptions.json"
