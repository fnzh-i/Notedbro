"""Find the vault from this script's folder, or from BRAIN_VAULT."""

import os
from pathlib import Path


def vault_root():
    override = os.environ.get("BRAIN_VAULT")
    if override:
        return Path(os.path.realpath(os.path.expanduser(override)))
    return Path(__file__).resolve().parent.parent
