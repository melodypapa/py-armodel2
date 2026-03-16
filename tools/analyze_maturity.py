#!/usr/bin/env python3
"""Analyze maturity status of all AUTOSAR model classes, enums, and primitives."""

import json
from pathlib import Path
from collections import defaultdict


def normalize_maturity(maturity: str) -> str:
    """Normalize maturity values to handle inconsistencies."""
    if not maturity:
        return "draft"
    maturity_lower = maturity.lower()
    if maturity_lower in ("reviewed", "reviewer"):  # "reviewer" is a typo for "reviewed"
        return "reviewed"
    return "draft"


def analyze_maturity(json_dir: Path) -> dict:
    """Analyze maturity status across all JSON files."""
    stats = {
        "classes": {"reviewed": [], "draft": [], "by_package": defaultdict(lambda: {"reviewed": 0, "draft": 0}), "invalid": []},
        "enums": {"reviewed": [], "draft": [], "by_package": defaultdict(lambda: {"reviewed": 0, "draft": 0}), "invalid": []},
        "primitives": {"reviewed": [], "draft": [], "by_package": defaultdict(lambda: {"reviewed": 0, "draft": 0}), "invalid": []},
    }

    for json_file in json_dir.glob("*.classes.json"):
        with open(json_file) as f:
            data = json.load(f)

        package = data.get("package", "Unknown")
        for cls in data.get("classes", []):
            raw_maturity = cls.get("maturity", "draft")
            maturity = normalize_maturity(raw_maturity)
            name = cls.get("name", "Unknown")
            item = {"name": name, "package": package, "raw_maturity": raw_maturity}

            if maturity == "reviewed":
                stats["classes"]["reviewed"].append(item)
            else:
                stats["classes"]["draft"].append(item)

            # Track invalid maturity values
            if raw_maturity not in ("reviewed", "draft", None, ""):
                stats["classes"]["invalid"].append(item)

            stats["classes"]["by_package"][package][maturity] += 1

    for json_file in json_dir.glob("*.enums.json"):
        with open(json_file) as f:
            data = json.load(f)

        package = data.get("package", "Unknown")
        for enum in data.get("enumerations", []):
            raw_maturity = enum.get("maturity", "draft")
            maturity = normalize_maturity(raw_maturity)
            name = enum.get("name", "Unknown")
            literals = len(enum.get("literals", []))
            item = {"name": name, "package": package, "literals": literals, "raw_maturity": raw_maturity}

            if maturity == "reviewed":
                stats["enums"]["reviewed"].append(item)
            else:
                stats["enums"]["draft"].append(item)

            # Track invalid maturity values
            if raw_maturity not in ("reviewed", "draft", None, ""):
                stats["enums"]["invalid"].append(item)

            stats["enums"]["by_package"][package][maturity] += 1

    for json_file in json_dir.glob("*.primitives.json"):
        with open(json_file) as f:
            data = json.load(f)

        package = data.get("package", "Unknown")
        for prim in data.get("primitives", []):
            raw_maturity = prim.get("maturity", "draft")
            maturity = normalize_maturity(raw_maturity)
            name = prim.get("name", "Unknown")
            item = {"name": name, "package": package, "raw_maturity": raw_maturity}

            if maturity == "reviewed":
                stats["primitives"]["reviewed"].append(item)
            else:
                stats["primitives"]["draft"].append(item)

            # Track invalid maturity values
            if raw_maturity not in ("reviewed", "draft", None, ""):
                stats["primitives"]["invalid"].append(item)

            stats["primitives"]["by_package"][package][maturity] += 1

    return stats


def print_report(stats: dict) -> None:
    """Print the maturity analysis report."""
    print("=" * 80)
    print("AUTOSAR MODEL MATURITY ANALYSIS")
    print("=" * 80)
    print()

    # Classes
    total_classes = len(stats["classes"]["reviewed"]) + len(stats["classes"]["draft"])
    reviewed_classes = len(stats["classes"]["reviewed"])
    draft_classes = len(stats["classes"]["draft"])

    print("## CLASSES")
    print("-" * 80)
    print(f"Total: {total_classes}")
    print(f"Reviewed: {reviewed_classes} ({reviewed_classes / total_classes * 100:.1f}%)")
    print(f"Draft: {draft_classes} ({draft_classes / total_classes * 100:.1f}%)")
    print()

    # Enums
    total_enums = len(stats["enums"]["reviewed"]) + len(stats["enums"]["draft"])
    reviewed_enums = len(stats["enums"]["reviewed"])
    draft_enums = len(stats["enums"]["draft"])

    print("## ENUMERATIONS")
    print("-" * 80)
    print(f"Total: {total_enums}")
    if total_enums > 0:
        print(f"Reviewed: {reviewed_enums} ({reviewed_enums / total_enums * 100:.1f}%)")
        print(f"Draft: {draft_enums} ({draft_enums / total_enums * 100:.1f}%)")
    else:
        print(f"Reviewed: {reviewed_enums} (0.0%)")
        print(f"Draft: {draft_enums} (0.0%)")
    print()

    # Primitives
    total_prims = len(stats["primitives"]["reviewed"]) + len(stats["primitives"]["draft"])
    reviewed_prims = len(stats["primitives"]["reviewed"])
    draft_prims = len(stats["primitives"]["draft"])

    print("## PRIMITIVES")
    print("-" * 80)
    print(f"Total: {total_prims}")
    if total_prims > 0:
        print(f"Reviewed: {reviewed_prims} ({reviewed_prims / total_prims * 100:.1f}%)")
        print(f"Draft: {draft_prims} ({draft_prims / total_prims * 100:.1f}%)")
    else:
        print(f"Reviewed: {reviewed_prims} (0.0%)")
        print(f"Draft: {draft_prims} (0.0%)")
    print()

    # Overall
    total_elements = total_classes + total_enums + total_prims
    total_reviewed = reviewed_classes + reviewed_enums + reviewed_prims

    print("## OVERALL")
    print("-" * 80)
    print(f"Total Elements: {total_elements}")
    print(f"Total Reviewed: {total_reviewed} ({total_reviewed / total_elements * 100:.1f}%)")
    print(f"Total Draft: {total_elements - total_reviewed} ({(total_elements - total_reviewed) / total_elements * 100:.1f}%)")
    print()

    # Reviewed Classes
    if stats["classes"]["reviewed"]:
        print("## REVIEWED CLASSES")
        print("-" * 80)
        for i, item in enumerate(sorted(stats["classes"]["reviewed"], key=lambda x: x["name"]), 1):
            print(f"{i:3}. {item['name']:50} [{item['package']}]")
        print()

    # Draft Classes
    if stats["classes"]["draft"]:
        print("## DRAFT CLASSES")
        print("-" * 80)
        for i, item in enumerate(sorted(stats["classes"]["draft"], key=lambda x: x["name"]), 1):
            print(f"{i:4}. {item['name']:50} [{item['package']}]")
        print()

    # Draft Enums
    if stats["enums"]["draft"]:
        print("## DRAFT ENUMERATIONS")
        print("-" * 80)
        for i, item in enumerate(sorted(stats["enums"]["draft"], key=lambda x: x["name"]), 1):
            print(f"{i:4}. {item['name']:50} [{item['package']}] ({item['literals']} literals)")
        print()

    # Draft Primitives
    if stats["primitives"]["draft"]:
        print("## DRAFT PRIMITIVES")
        print("-" * 80)
        for i, item in enumerate(sorted(stats["primitives"]["draft"], key=lambda x: x["name"]), 1):
            print(f"{i:4}. {item['name']:50} [{item['package']}]")
        print()


def main():
    json_dir = Path(__file__).parent.parent / "docs" / "json" / "packages"
    stats = analyze_maturity(json_dir)
    print_report(stats)


if __name__ == "__main__":
    main()
