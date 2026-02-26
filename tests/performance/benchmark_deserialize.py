"""
Benchmark to demonstrate the actual performance improvement in deserialize().

This script measures the time taken to deserialize XML elements with the
optimized get_type_hints() call.
"""

import time
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)
from armodel2.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import SwBaseType


def create_test_element(tag_name, attributes=None, children=None):
    """Create a test XML element."""
    elem = ET.Element(tag_name)
    if attributes:
        for key, value in attributes.items():
            elem.set(key, value)
    if children:
        for child in children:
            elem.append(child)
    return elem


def benchmark_deserialize(cls, element, iterations=100):
    """Benchmark deserialize() call for a class."""
    start_time = time.time()
    for _ in range(iterations):
        cls.deserialize(element)
    elapsed = time.time() - start_time
    return elapsed


def main():
    """Run benchmarks and report results."""
    iterations = 100

    print("Benchmarking deserialize() performance")
    print("=" * 60)
    print(f"Iterations: {iterations}")
    print()

    # Test SwBaseType deserialize
    print("Testing: SwBaseType.deserialize()")
    print("-" * 60)

    # Create proper XML element
    sw_base_type_element = ET.Element("SW-BASE-TYPE")
    short_name = ET.SubElement(sw_base_type_element, "SHORT-NAME")
    short_name.text = "TestSwBaseType"

    time_taken = benchmark_deserialize(SwBaseType, sw_base_type_element, iterations)
    print(f"Time: {time_taken:.4f}s")
    print(f"Average: {time_taken / iterations * 1000:.2f}ms per deserialize")

    # Test SwDataDefProps deserialize
    print("\nTesting: SwDataDefProps.deserialize()")
    print("-" * 60)

    sw_data_def_props_element = ET.Element("SW-DATA-DEF-PROPS")
    # Add required SHORT-NAME
    short_name = ET.SubElement(sw_data_def_props_element, "SHORT-NAME")
    short_name.text = "TestSwDataDefProps"

    time_taken = benchmark_deserialize(
        SwDataDefProps, sw_data_def_props_element, iterations
    )
    print(f"Time: {time_taken:.4f}s")
    print(f"Average: {time_taken / iterations * 1000:.2f}ms per deserialize")

    print("\n" + "=" * 60)
    print("Benchmark complete!")
    print("\nNote: The optimization primarily benefits:")
    print("- Classes with deep inheritance hierarchies")
    print("- Classes with many type annotations")
    print("- Repeated deserialization of the same class type")


if __name__ == "__main__":
    main()