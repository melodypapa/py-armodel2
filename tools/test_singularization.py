#!/usr/bin/env python3
"""Test singularization and pluralization functions."""

import sys
from pathlib import Path

# Directly import from the _common module without __init__.py
sys.path.insert(0, str(Path(__file__).parent / "generate_models"))
import _common

to_singular = _common.to_singular
to_plural = _common.to_plural


def test_singularization():
    """Test singularization function."""
    test_cases = [
        ("entities", "entity"),
        ("packages", "package"),
        ("values", "value"),
        ("elements", "element"),
        ("arPackages", "arPackage"),
        ("sdgs", "sdg"),
        ("buses", "bus"),
        ("types", "type"),
        ("axes", "axis"),
        ("indices", "index"),
        ("variables", "variable"),
        ("libraries", "library"),
        ("locations", "location"),
        ("entries", "entry"),
        ("items", "item"),
        ("sections", "section"),
        ("descriptors", "descriptor"),
        ("bodies", "body"),
        ("bases", "base"),
        ("classes", "class"),
        # Additional edge cases
        ("houses", "house"),
        ("boxes", "box"),
        ("watches", "watch"),
        ("bushes", "bush"),
    ]

    for plural, expected in test_cases:
        result = to_singular(plural)
        if result != expected:
            print(f"FAIL: to_singular('{plural}') = '{result}' (expected '{expected}')")
            return False

    print("All singularization tests passed!")
    return True


def test_pluralization():
    """Test pluralization function."""
    test_cases = [
        ("entity", "entities"),
        ("package", "packages"),
        ("value", "values"),
        ("element", "elements"),
        ("arPackage", "arPackages"),
        ("sdg", "sdgs"),
        ("bus", "buses"),
        ("type", "types"),
        ("axis", "axes"),
        ("index", "indices"),
        ("variable", "variables"),
        ("library", "libraries"),
        ("location", "locations"),
        ("item", "items"),
        ("section", "sections"),
        ("descriptor", "descriptors"),
        ("body", "bodies"),
        ("base", "bases"),
        ("class", "classes"),
        # Additional edge cases
        ("house", "houses"),
        ("box", "boxes"),
        ("watch", "watches"),
        ("bush", "bushes"),
    ]

    for singular, expected in test_cases:
        result = to_plural(singular)
        if result != expected:
            print(f"FAIL: to_plural('{singular}') = '{result}' (expected '{expected}')")
            return False

    print("All pluralization tests passed!")
    return True


def test_round_trip():
    """Test that singularize + pluralize preserves original (or close to it)."""
    test_cases = [
        "entities", "packages", "values", "elements", "entries", "bodies",
        "variables", "libraries", "items", "sections", "bases", "classes",
    ]

    for original in test_cases:
        singular = to_singular(original)
        plural = to_plural(singular)
        if plural != original:
            print(f"FAIL: Round-trip '{original}' -> '{singular}' -> '{plural}'")
            return False

    print("All round-trip tests passed!")
    return True


def main():
    """Run all tests."""
    print("Testing singularization and pluralization functions...\n")

    all_passed = True
    all_passed &= test_singularization()
    all_passed &= test_pluralization()
    all_passed &= test_round_trip()

    if all_passed:
        print("\n[OK] All tests passed!")
        return 0
    else:
        print("\n[FAIL] Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
