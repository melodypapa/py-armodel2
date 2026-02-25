#!/usr/bin/env python3
"""Update JSON attribute names from plural to singular for multiplicity '*'."""

import json
from pathlib import Path
import sys

# Add tools/generate_models to path for imports
sys.path.insert(0, str(Path(__file__).parent / "generate_models"))
from _common import to_singular


def update_json_file(json_file: Path, dry_run: bool = False) -> int:
    """Update attribute names in a single JSON file.

    Args:
        json_file: Path to the JSON file to update
        dry_run: If True, don't actually write changes

    Returns:
        Number of attributes updated
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    updates = []

    for cls in data.get("classes", []):
        if "attributes" in cls:
            new_attributes = {}
            for attr_name, attr_info in cls["attributes"].items():
                multiplicity = attr_info.get("multiplicity", "1")
                if multiplicity in ("*", "0..*"):
                    singular_name = to_singular(attr_name)
                    if singular_name != attr_name:
                        updates.append(f"  {cls['name']}.{attr_name} -> {singular_name}")
                        attr_name = singular_name
                        updated_count += 1
                new_attributes[attr_name] = attr_info
            cls["attributes"] = new_attributes

    if updated_count > 0 and not dry_run:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')

    # Print updates for this file
    if updates:
        print(f"\n{json_file.name}:")
        for update in updates:
            print(update)

    return updated_count


def main():
    """Update all JSON files in docs/json/packages/."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Update JSON attribute names from plural to singular for multiplicity '*'"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without actually modifying files"
    )
    parser.add_argument(
        "--packages-dir",
        type=str,
        default="docs/json/packages",
        help="Path to packages directory (default: docs/json/packages)"
    )

    args = parser.parse_args()

    packages_dir = Path(args.packages_dir)
    if not packages_dir.exists():
        print(f"Error: Directory {packages_dir} does not exist")
        return 1

    if args.dry_run:
        print("DRY RUN MODE - No files will be modified\n")

    total = 0
    file_count = 0

    for json_file in sorted(packages_dir.glob("*.classes.json")):
        count = update_json_file(json_file, dry_run=args.dry_run)
        if count > 0:
            total += count
            file_count += 1

    if args.dry_run:
        print(f"\nWould update {total} attributes in {file_count} files.")
    else:
        print(f"\nUpdated {total} attributes in {file_count} files.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
