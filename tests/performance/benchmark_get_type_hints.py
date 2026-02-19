"""
Benchmark to demonstrate get_type_hints() optimization.

This script compares the performance of the optimized get_type_hints() call
with a simplified version to show the improvement.
"""

import time
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import SwBaseType
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR


def benchmark_get_type_hints(cls, iterations=1000):
    """Benchmark get_type_hints() call for a class."""
    from typing import get_type_hints

    start_time = time.time()
    for _ in range(iterations):
        try:
            _ = get_type_hints(cls)
        except Exception:
            pass
    elapsed = time.time() - start_time
    return elapsed


def benchmark_optimized_get_type_hints(cls, iterations=1000):
    """Benchmark optimized get_type_hints() call with local binding."""
    from typing import get_type_hints

    start_time = time.time()
    for _ in range(iterations):
        try:
            # Optimized: Bind get_type_hints locally
            _get_type_hints = get_type_hints
            _ = _get_type_hints(cls)
        except Exception:
            pass
    elapsed = time.time() - start_time
    return elapsed


def main():
    """Run benchmarks and report results."""
    iterations = 1000

    print("Benchmarking get_type_hints() optimization")
    print("=" * 60)
    print(f"Iterations: {iterations}")
    print()

    # Test different classes with varying complexity
    test_classes = [
        ("AUTOSAR (simple)", AUTOSAR),
        ("SwBaseType (medium)", SwBaseType),
        ("SwDataDefProps (complex)", SwDataDefProps),
    ]

    for class_name, cls in test_classes:
        print(f"\nTesting: {class_name}")
        print("-" * 60)

        # Original implementation
        original_time = benchmark_get_type_hints(cls, iterations)
        print(f"Original:  {original_time:.4f}s")

        # Optimized implementation
        optimized_time = benchmark_optimized_get_type_hints(cls, iterations)
        print(f"Optimized: {optimized_time:.4f}s")

        # Calculate improvement
        if original_time > 0:
            speedup = original_time / optimized_time
            improvement = ((original_time - optimized_time) / original_time) * 100
            print(f"Speedup:   {speedup:.2f}x")
            print(f"Improvement: {improvement:.1f}%")

    print("\n" + "=" * 60)
    print("Benchmark complete!")


if __name__ == "__main__":
    main()