"""Example: Using the new ARXML Reader/Writer API.

This example demonstrates how to:
1. Create an AUTOSAR instance
2. Load ARXML files into it
3. Save to ARXML files

The new API allows reusing the same AUTOSAR instance for multiple operations.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter

# ========================================================================
# Create AUTOSAR instance
# ========================================================================
autosar = AUTOSAR()

# ========================================================================
# Load ARXML files into the instance
# ========================================================================
reader = ARXMLReader()

# Load a file into the existing AUTOSAR instance
reader.load_arxml(autosar, "demos/arxml/AUTOSAR_Datatypes.arxml")

# You can load multiple files into the same instance
# reader.load_arxml(autosar, "demos/arxml/another_file.arxml")
# Packages from multiple files will be merged into autosar.ar_packages

# ========================================================================
# Save AUTOSAR instance to file
# ========================================================================
writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")

# Save to a new file
writer.save_arxml(autosar, "output.arxml")

# You can save the same instance to multiple files
# writer.save_arxml(autosar, "output_copy.arxml")

print("✓ Successfully loaded AUTOSAR_Datatypes.arxml")
print(f"✓ Total packages: {len(autosar.ar_packages)}")
if autosar.ar_packages:
    root_pkg = autosar.ar_packages[0]
    if hasattr(root_pkg, 'ar_packages'):
        print(f"✓ Nested packages: {len(root_pkg.ar_packages)}")
        for pkg in root_pkg.ar_packages:
            print(f"  - {pkg.short_name}: {len(pkg.elements) if hasattr(pkg, 'elements') else 0} elements")
