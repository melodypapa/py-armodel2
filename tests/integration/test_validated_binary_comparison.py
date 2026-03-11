"""
Integration tests for binary comparison of ARXML round-trip serialization.

This test module validates that reading and writing ARXML files produces
identical binary output, ensuring the optimized serialization framework
preserves all data correctly.

Test Strategy:
- Discover all ARXML files in demos/test_validated/ using wildcard pattern
- Read each ARXML file
- Deserialize to Python objects
- Serialize back to XML
- Perform binary comparison with original file
- Report any differences with detailed diagnostics

Traceability:
- Test Documentation: docs/tests/integration/test_validated_binary_comparison.md
- SWITS IDs: SWITS-INT-0229+ (assigned sequentially to discovered files)
"""
import pytest
import shlex
import sys
from pathlib import Path

from armodel2.reader import ARXMLReader
from armodel2.writer import ARXMLWriter


def _get_test_validated_files() -> list[str]:
    """Discover all ARXML files in demos/test_validated/.

    Returns:
        Sorted list of ARXML filenames in demos/test_validated/
    """
    test_validated_path = Path("demos/test_validated")
    if not test_validated_path.exists():
        return []
    return sorted([f.name for f in test_validated_path.glob("*.arxml")])


class TestTestValidated:
    """Test all ARXML files in demos/test_validated/ with wildcard discovery.

    Any .arxml file added to demos/test_validated/ will be automatically tested.

    Note: Files in demos/test_validated/ are for demonstration only.
    New files can be added to this directory and will be automatically
    included in tests without modifying test code.

    Test IDs: SWITS-INT-0229+
    """

    @pytest.fixture
    def reader(self) -> ARXMLReader:
        """ARXML reader instance."""
        return ARXMLReader()

    @pytest.fixture
    def writer(self) -> ARXMLWriter:
        """ARXML writer instance."""
        return ARXMLWriter(pretty_print=True, encoding="UTF-8")

    def _test_single_file_binary_comparison(
        self,
        filename: str,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test a single ARXML file from demos/test_validated/ for binary exact round-trip serialization.

        Args:
            filename: Name of the ARXML file to test
            reader: ARXML reader instance
            writer: ARXML writer instance
            tmp_path: Pytest temporary directory
        """
        # Only check demos/test_validated directory
        arxml_file = Path("demos/test_validated") / filename

        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        # Print file being tested (flush immediately for visibility)
        print(f"\nTesting: {arxml_file}", file=sys.stderr, flush=True)

        # Read original
        original_bytes = arxml_file.read_bytes()

        # Round-trip
        from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        AUTOSAR.reset()
        autosar = AUTOSAR()
        reader.load_arxml(str(arxml_file), autosar)
        output_file = tmp_path / f"{arxml_file.stem}_output.arxml"
        writer.save_arxml(str(output_file), autosar)

        # Read serialized
        serialized_bytes = output_file.read_bytes()

        # Normalize line endings (CRLF -> LF) for comparison
        # This allows tests to pass regardless of source file line endings
        original_normalized = original_bytes.replace(b'\r\n', b'\n')
        serialized_normalized = serialized_bytes.replace(b'\r\n', b'\n')

        # Binary comparison
        assert original_normalized == serialized_normalized, (
            f"Binary comparison failed for {filename}\n"
            f"Original:    {len(original_bytes):,} bytes ({len(original_normalized):,} normalized)\n"
            f"Serialized:  {len(serialized_bytes):,} bytes ({len(serialized_normalized):,} normalized)\n"
            f"Difference:  {abs(len(serialized_normalized) - len(original_normalized)):,} bytes\n\n"
            f"To reproduce the error, run:\n"
            f"  armodel format {shlex.quote(str(arxml_file))} -o data/output.arxml\n\n"
            f"To compare the differences:\n"
            f"  diff {shlex.quote(str(arxml_file))} data/output.arxml"
        )

    @pytest.mark.parametrize(
        "filename",
        _get_test_validated_files(),
        ids=lambda x: x.replace(".arxml", "")
    )
    def test_wildcard_binary_comparison(
        self,
        filename: str,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test ARXML file from demos/test_validated/ for binary exact round-trip.

        This test uses wildcard discovery - any .arxml file added to
        demos/test_validated/ will be automatically tested.

        Args:
            filename: Name of the ARXML file to test
            reader: ARXML reader instance
            writer: ARXML writer instance
            tmp_path: Pytest temporary directory
        """
        self._test_single_file_binary_comparison(
            filename,
            reader,
            writer,
            tmp_path
        )
