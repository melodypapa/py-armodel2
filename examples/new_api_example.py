"""Example: Using the ARXML Reader/Writer API.

This example demonstrates how to:
1. Load ARXML files
2. Save to ARXML files

The new API supports both explicit AUTOSAR instances and the AUTOSAR singleton.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter

# ========================================================================
# Method 1: Using AUTOSAR Singleton (Convenient)
# ========================================================================
print("=== Method 1: Using AUTOSAR Singleton ===")
print()

reader = ARXMLReader()
writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")

# Load file into singleton (no need to create AUTOSAR instance)
reader.load_arxml("demos/arxml/AUTOSAR_Datatypes.arxml")

# Access the singleton to inspect content
autosar = AUTOSAR()
print("✓ Loaded file into singleton")
print(f"✓ Total packages: {len(autosar.ar_packages)}")

# Save from singleton
writer.save_arxml("output_singleton.arxml")
print("✓ Saved to output_singleton.arxml")

# Clear singleton for next operation
autosar.clear()
print("✓ Cleared singleton state")

# ========================================================================
# Method 2: Using load_arxml_with_clear (Fresh State)
# ========================================================================
print()
print("=== Method 2: Using load_arxml_with_clear ===")
print()

# This automatically clears the singleton before loading
reader.load_arxml_with_clear("demos/arxml/AUTOSAR_Datatypes.arxml")

print("✓ Loaded file with fresh state")
print(f"✓ Total packages: {len(AUTOSAR().ar_packages)}")

writer.save_arxml("output_fresh_state.arxml")
print("✓ Saved to output_fresh_state.arxml")

# ========================================================================
# Method 3: Using Explicit AUTOSAR Instance (Backward Compatible)
# ========================================================================
print()
print("=== Method 3: Using Explicit AUTOSAR Instance ===")
print()

# Create a custom AUTOSAR instance (isolated from singleton)
custom_autosar = AUTOSAR()
reader.load_arxml("demos/arxml/AUTOSAR_Datatypes.arxml", custom_autosar)

print("✓ Loaded file into custom instance")
print(f"✓ Total packages: {len(custom_autosar.ar_packages)}")

writer.save_arxml("output_custom.arxml", custom_autosar)
print("✓ Saved to output_custom.arxml")

# The singleton is unaffected by the custom instance
print(f"✓ Singleton packages: {len(AUTOSAR().ar_packages)}")

# ========================================================================
# Multiple File Loading (Merge Behavior)
# ========================================================================
print()
print("=== Method 4: Loading Multiple Files (Merge) ===")
print()

# Clear singleton first
AUTOSAR().clear()

# Load multiple files - they will be merged into the same instance
reader.load_arxml("demos/arxml/AUTOSAR_Datatypes.arxml")
# reader.load_arxml("demos/arxml/another_file.arxml")  # Add more files

print("✓ Loaded files into singleton (merged)")
print(f"✓ Total packages: {len(AUTOSAR().ar_packages)}")

if AUTOSAR().ar_packages:
    root_pkg = AUTOSAR().ar_packages[0]
    if hasattr(root_pkg, 'ar_packages'):
        print(f"✓ Nested packages: {len(root_pkg.ar_packages)}")
        for pkg in root_pkg.ar_packages[:3]:  # Show first 3
            pkg_name = pkg.short_name if hasattr(pkg, 'short_name') else 'unknown'
            elem_count = len(pkg.elements) if hasattr(pkg, 'elements') else 0
            print(f"  - {pkg_name}: {elem_count} elements")

print()
print("✓ All operations completed successfully!")