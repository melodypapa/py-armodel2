#!/usr/bin/env python3
"""Identify attributes with xml_element_name decorator.

This script scans all JSON package files and reports attributes that use
the xml_element_name decorator, which indicates they need pre-computed
XML tag mappings.
"""
import json
from pathlib import Path


def find_xml_element_name_decorators(json_path: Path) -> list[dict]:
    """Find all attributes using xml_element_name decorator.

    Args:
        json_path: Path to JSON file

    Returns:
        List of dictionaries with class, attribute, xml_tag, and decorator info
    """
    with open(json_path) as f:
        data = json.load(f)

    results = []

    for class_data in data.get("classes", []):
        class_name = class_data["name"]

        for attr_name, attr_data in class_data.get("attributes", {}).items():
            decorator = attr_data.get("decorator", "")
            if "xml_element_name:" in decorator:
                # Extract the tag from decorator
                # Handle: "xml_element_name:TAG" or "decorator1:val1:xml_element_name:TAG"
                parts = decorator.split(":")
                for i, part in enumerate(parts):
                    if part == "xml_element_name" and i + 1 < len(parts):
                        tag = parts[i + 1]
                        results.append({
                            "class": class_name,
                            "attribute": attr_name,
                            "xml_tag": tag,
                            "decorator": decorator
                        })
                        break

    return results


if __name__ == "__main__":
    packages_dir = Path("docs/json/packages")
    total = 0
    unique_tags = set()

    print("Scanning for xml_element_name decorator usage...\n")
    print("=" * 80)

    for json_file in sorted(packages_dir.glob("*.classes.json")):
        decorators = find_xml_element_name_decorators(json_file)
        if decorators:
            print(f"\n{json_file.name}:")
            for dec in decorators:
                print(f"  {dec['class']}.{dec['attribute']} → {dec['xml_tag']}")
                unique_tags.add(dec['xml_tag'])
                total += 1

    print("\n" + "=" * 80)
    print("\nSummary:")
    print(f"  Total attributes with xml_element_name: {total}")
    print(f"  Unique XML tags: {len(unique_tags)}")

    if unique_tags:
        print(f"\n  Unique tags: {sorted(unique_tags)}")
