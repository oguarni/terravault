#!/usr/bin/env python3
"""Generate pip-compatible scan-action constraints from runtime requirements.

pip rejects extras in a constraints file, so the action cannot pass the root
requirements.txt to -c directly. action.yml writes this projection at run time
instead of reading a committed copy, which no dependency update could keep
current without someone regenerating it by hand.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ACTION_DIRECTORY = Path(__file__).resolve().parent
REPOSITORY_ROOT = ACTION_DIRECTORY.parents[2]
SOURCE = REPOSITORY_ROOT / "requirements.txt"

PINNED_REQUIREMENT = re.compile(
    r"^(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)"
    r"(?:\[[^]]+\])?"
    r"(?P<pin>\s*==\s*[^\s;]+.*)$"
)
SKIPPED_OPTIONS = (
    "-r",
    "--requirement",
    "-c",
    "--constraint",
    "-e",
    "--editable",
)
HEADER = "# Generated from requirements.txt by generate-constraints.py.\n"


def project_requirements(source: Path) -> list[str]:
    """Return all pinned requirements with any extras removed."""
    projected: list[str] = []

    for line_number, raw_line in enumerate(source.read_text().splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith(SKIPPED_OPTIONS):
            continue

        match = PINNED_REQUIREMENT.fullmatch(line)
        if match is None:
            raise ValueError(
                f"{source}:{line_number}: expected a requirement pinned with ==: "
                f"{raw_line!r}"
            )
        projected.append(f"{match.group('name')}{match.group('pin')}")

    if not projected:
        raise ValueError(f"{source}: no pinned requirements found")

    return projected


def main(argv: list[str]) -> int:
    """Write the deterministic constraints projection to the given path."""
    if len(argv) != 1:
        print("usage: generate-constraints.py OUTPUT", file=sys.stderr)
        return 2

    requirements = project_requirements(SOURCE)
    Path(argv[0]).write_text(HEADER + "\n".join(requirements) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
