#!/usr/bin/env python3
"""Test script to debug PortPrototypeBlueprint Figure issue."""

from pathlib import Path
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter
import tempfile

arxml_file = Path("demos/arxml/AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_Blueprint.arxml")

# Read original
original_bytes = arxml_file.read_bytes()

# Round-trip
autosar = AUTOSAR()
reader = ARXMLReader()
reader.load_arxml(autosar, str(arxml_file))

with tempfile.TemporaryDirectory() as tmp_dir:
    output_file = Path(tmp_dir) / "output.arxml"
    writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")
    writer.save_arxml(autosar, str(output_file))

    # Read serialized
    serialized_bytes = output_file.read_bytes()

    # Binary comparison
    if original_bytes == serialized_bytes:
        print("SUCCESS: Binary comparison passed!")
    else:
        print(f"FAILURE: Binary comparison failed!")
        print(f"Original:    {len(original_bytes):,} bytes")
        print(f"Serialized:  {len(serialized_bytes):,} bytes")
        print(f"Difference:  {abs(len(serialized_bytes) - len(original_bytes)):,} bytes")

        # Find differences
        original_lines = original_bytes.decode('utf-8').split('\n')
        serialized_lines = serialized_bytes.decode('utf-8').split('\n')

        print(f"\nOriginal lines: {len(original_lines):,}")
        print(f"Serialized lines: {len(serialized_lines):,}")

        # Find first few differences
        diff_count = 0
        for i, (orig, ser) in enumerate(zip(original_lines, serialized_lines)):
            if orig != ser:
                diff_count += 1
                if diff_count <= 10:
                    print(f"\nDifference at line {i+1}:")
                    print(f"  Original:  {orig[:100]}")
                    print(f"  Serialized: {ser[:100]}")

        print(f"\nTotal differences found: {diff_count}")