#!/usr/bin/env python3
"""Code generator for AUTOSAR model classes."""

import json
from pathlib import Path
from typing import Any, Dict


def parse_mapping_json(mapping_file: Path) -> Dict[str, Any]:
    """Parse mapping.json file.

    Args:
        mapping_file: Path to mapping.json file

    Returns:
        Parsed JSON data as dictionary
    """
    with open(mapping_file, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: generate_models.py <mapping.json> <output_dir>")
        sys.exit(1)

    mapping_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    # Parse mapping
    data = parse_mapping_json(mapping_file)
    print(f"Loaded {len(data.get('types', []))} type definitions")
