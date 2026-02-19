"""
Integration tests for binary comparison of ARXML round-trip serialization.

This test module validates that reading and writing ARXML files produces
identical binary output, ensuring the optimized serialization framework
preserves all data correctly.

Test Strategy:
- Read each ARXML file from demos/arxml/
- Deserialize to Python objects
- Serialize back to XML
- Perform binary comparison with original file
- Report any differences with detailed diagnostics

Traceability:
- Test Documentation: docs/tests/integration/test_binary_comparison.md
- SWITS IDs: SWITS-INT-0100 through SWITS-INT-0199
"""
import pytest
from pathlib import Path
import xml.etree.ElementTree as ET
from typing import List, Tuple
import difflib

from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter


class TestBinaryComparison:
    """Integration tests for binary comparison of ARXML round-trip serialization.

    Test IDs: SWITS-INT-0100 to SWITS-INT-0199
    """

    @pytest.fixture(scope="class")
    def arxml_files(self) -> List[Path]:
        """Get all ARXML files from demos/arxml directory.

        Returns:
            List of Path objects for all ARXML files
        """
        arxml_dir = Path("demos/arxml")
        return sorted(arxml_dir.glob("*.arxml"))

    @pytest.fixture(scope="class")
    def reader(self) -> ARXMLReader:
        """ARXML reader instance."""
        return ARXMLReader()

    @pytest.fixture(scope="class")
    def writer(self) -> ARXMLWriter:
        """ARXML writer instance with pretty print for easier debugging."""
        return ARXMLWriter(pretty_print=True, encoding="UTF-8")

    @pytest.fixture(autouse=True)
    def setup_test(self, arxml_files: List[Path]):
        """Print test setup information."""
        print(f"\n{'='*70}")
        print(f"Testing {len(arxml_files)} ARXML files for binary comparison")
        print(f"{'='*70}\n")

    def test_all_arxml_files_binary_comparison(
        self,
        arxml_files: List[Path],
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ):
        """Test all ARXML files for binary exact round-trip serialization.

        This is the main test that validates all ARXML files. It loads each file,
        performs round-trip serialization, and compares the binary output.

        Args:
            arxml_files: List of ARXML file paths
            reader: ARXML reader instance
            writer: ARXML writer instance
            tmp_path: Pytest temporary directory for output files

        Test ID: SWITS-INT-0100
        """
        failed_files: List[Tuple[Path, str]] = []
        passed_files: List[Path] = []

        for arxml_file in arxml_files:
            try:
                # Skip if file doesn't exist
                if not arxml_file.exists():
                    print(f"⚠️  SKIP: {arxml_file.name} (file not found)")
                    continue

                print(f"\n🔍 Testing: {arxml_file.name}")
                print(f"   Size: {arxml_file.stat().st_size:,} bytes")

                # Read original file content
                original_content = arxml_file.read_bytes()
                original_lines = arxml_file.read_text(encoding='UTF-8').splitlines(keepends=True)

                # Deserialize to Python objects
                print(f"   📖 Reading...")
                from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
                autosar = AUTOSAR()
                reader.load_arxml(autosar, str(arxml_file))
                print(f"   ✓ Loaded {len(autosar.ar_packages)} AR packages")

                # Serialize back to XML
                output_file = tmp_path / f"{arxml_file.stem}_output.arxml"
                print(f"   ✍️  Writing...")
                writer.save_arxml(autosar, str(output_file))

                # Read serialized content
                serialized_content = output_file.read_bytes()
                serialized_lines = output_file.read_text(encoding='UTF-8').splitlines(keepends=True)

                # Binary comparison
                if original_content == serialized_content:
                    print(f"   ✅ PASS: Binary comparison successful")
                    passed_files.append(arxml_file)
                else:
                    print(f"   ❌ FAIL: Binary comparison failed")
                    print(f"      Original size:    {len(original_content):,} bytes")
                    print(f"      Serialized size:  {len(serialized_content):,} bytes")
                    print(f"      Size difference:  {len(serialized_content) - len(original_content):+,d} bytes")

                    # Show line differences
                    self._show_line_differences(original_lines, serialized_lines, arxml_file.name)

                    failed_files.append((arxml_file, "Binary mismatch"))

            except Exception as e:
                print(f"   💥 ERROR: {type(e).__name__}: {e}")
                failed_files.append((arxml_file, f"{type(e).__name__}: {e}"))

        # Print summary
        print(f"\n{'='*70}")
        print(f"SUMMARY")
        print(f"{'='*70}")
        print(f"Total files:  {len(arxml_files)}")
        print(f"✅ Passed:     {len(passed_files)}")
        print(f"❌ Failed:     {len(failed_files)}")
        print(f"{'='*70}\n")

        # Assert that all files passed
        if failed_files:
            failure_details = "\n".join([
                f"  - {file.name}: {reason}"
                for file, reason in failed_files
            ])
            pytest.fail(
                f"Binary comparison failed for {len(failed_files)} file(s):\n"
                f"{failure_details}\n\n"
                f"See test output above for detailed differences."
            )

    def test_autosar_datatypes_detailed(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ):
        """Detailed test for AUTOSAR_Datatypes.arxml with comprehensive diagnostics.

        This test provides more detailed output for debugging the main datatypes file.

        Args:
            reader: ARXML reader instance
            writer: ARXML writer instance
            tmp_path: Pytest temporary directory

        Test ID: SWITS-INT-0101
        """
        arxml_file = Path("demos/arxml/AUTOSAR_Datatypes.arxml")

        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        print(f"\n{'='*70}")
        print(f"Detailed Analysis: {arxml_file.name}")
        print(f"{'='*70}\n")

        # Load original file
        original_lines = arxml_file.read_text(encoding='UTF-8').splitlines(keepends=True)
        print(f"Original file:")
        print(f"  Lines:      {len(original_lines):,}")
        print(f"  File size:  {arxml_file.stat().st_size:,} bytes")

        # Deserialize
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()
        reader.load_arxml(autosar, str(arxml_file))
        print(f"\nDeserialized:")
        print(f"  AR packages: {len(autosar.ar_packages)}")

        # Count total elements
        total_elements = 0
        for pkg in autosar.ar_packages:
            if hasattr(pkg, 'elements') and pkg.elements:
                total_elements += len(pkg.elements)
        print(f"  Total elements: {total_elements:,}")

        # Serialize
        output_file = tmp_path / "AUTOSAR_Datatypes_output.arxml"
        writer.save_arxml(autosar, str(output_file))

        # Compare
        serialized_lines = output_file.read_text(encoding='UTF-8').splitlines(keepends=True)
        print(f"\nSerialized:")
        print(f"  Lines:      {len(serialized_lines):,}")
        print(f"  File size:  {output_file.stat().st_size:,} bytes")

        # Detailed line-by-line comparison
        print(f"\nLine-by-line comparison:")
        differences = self._compare_lines_detailed(original_lines, serialized_lines)

        if differences:
            print(f"  ❌ Found {len(differences)} differences")
            print(f"\nFirst 10 differences:")
            for i, (line_num, orig_line, ser_line, orig_marker, ser_marker) in enumerate(differences[:10], 1):
                print(f"\n  Difference {i} at line {line_num}:")
                print(f"    Original:  {orig_marker} {repr(orig_line)}")
                print(f"    Serialized:{ser_marker} {repr(ser_line)}")

            if len(differences) > 10:
                print(f"\n  ... and {len(differences) - 10} more differences")
        else:
            print(f"  ✅ No differences found")

        # Binary comparison assertion
        original_bytes = arxml_file.read_bytes()
        serialized_bytes = output_file.read_bytes()

        assert original_bytes == serialized_bytes, (
            f"Binary comparison failed for {arxml_file.name}\n"
            f"Original:    {len(original_bytes):,} bytes\n"
            f"Serialized:  {len(serialized_bytes):,} bytes\n"
            f"Differences: {len(differences)} lines"
        )

    def _show_line_differences(
        self,
        original_lines: List[str],
        serialized_lines: List[str],
        filename: str
    ) -> None:
        """Show line differences between original and serialized content.

        Args:
            original_lines: Original file lines
            serialized_lines: Serialized file lines
            filename: Name of the file being compared (for display)
        """
        # Use difflib to show differences
        diff = list(difflib.unified_diff(
            original_lines,
            serialized_lines,
            fromfile=f"{filename} (original)",
            tofile=f"{filename} (serialized)",
            lineterm=""
        ))

        if diff:
            print(f"\n   Differences (showing first 20 lines):")
            for line in diff[:20]:
                if line.startswith('+') and not line.startswith('+++'):
                    print(f"      {line}")
                elif line.startswith('-') and not line.startswith('---'):
                    print(f"      {line}")
                elif line.startswith('@@'):
                    print(f"      {line}")

            if len(diff) > 20:
                print(f"      ... ({len(diff) - 20} more lines)")

    def _compare_lines_detailed(
        self,
        original_lines: List[str],
        serialized_lines: List[str]
    ) -> List[Tuple[int, str, str, str, str]]:
        """Compare lines and return detailed differences.

        Args:
            original_lines: Original file lines
            serialized_lines: Serialized file lines

        Returns:
            List of tuples: (line_num, orig_line, ser_line, orig_marker, ser_marker)
        """
        differences = []
        max_lines = max(len(original_lines), len(serialized_lines))

        for i in range(max_lines):
            orig_line = original_lines[i] if i < len(original_lines) else "<missing>"
            ser_line = serialized_lines[i] if i < len(serialized_lines) else "<missing>"

            if orig_line != ser_line:
                # Determine markers
                if orig_line == "<missing>":
                    orig_marker = " "
                    ser_marker = "+"
                elif ser_line == "<missing>":
                    orig_marker = "-"
                    ser_marker = " "
                else:
                    orig_marker = "-"
                    ser_marker = "+"

                differences.append((i + 1, orig_line, ser_line, orig_marker, ser_marker))

        return differences


class TestIndividualFiles:
    """Test individual ARXML files with specific assertions.

    Each test validates a single ARXML file for binary exact round-trip serialization.

    Test IDs: SWITS-INT-0200 to SWITS-INT-0299
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
        """Test a single ARXML file for binary exact round-trip serialization.

        Args:
            filename: Name of the ARXML file to test
            reader: ARXML reader instance
            writer: ARXML writer instance
            tmp_path: Pytest temporary directory
        """
        arxml_file = Path("demos/arxml") / filename

        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        # Read original
        original_bytes = arxml_file.read_bytes()

        # Round-trip
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()
        reader.load_arxml(autosar, str(arxml_file))
        output_file = tmp_path / f"{arxml_file.stem}_output.arxml"
        writer.save_arxml(autosar, str(output_file))

        # Read serialized
        serialized_bytes = output_file.read_bytes()

        # Binary comparison
        assert original_bytes == serialized_bytes, (
            f"Binary comparison failed for {filename}\n"
            f"Original:    {len(original_bytes):,} bytes\n"
            f"Serialized:  {len(serialized_bytes):,} bytes\n"
            f"Difference:  {abs(len(serialized_bytes) - len(original_bytes)):,} bytes"
        )

    # Primary test - enabled first
    def test_application_data_type_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml for binary exact round-trip serialization.

        This is the primary test being enabled first for debugging.

        Test ID: SWITS-INT-0200
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    # All other tests - marked as xfail (expected to fail)
    def test_autosar_datatypes_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_Datatypes.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0201
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_Datatypes.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_application_data_type_lifecycle_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_ApplicationDataType_LifeCycle_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0202
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_ApplicationDataType_LifeCycle_Standard.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_base_types_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0203
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_BaseTypes_Standard.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_collection_body_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_Collection_Body_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0204
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_Collection_Body_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_collection_chassis_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_Collection_Chassis_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0205
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_Collection_Chassis_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_collection_mmed_telm_hmi_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_Collection_MmedTelmHmi_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0206
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_Collection_MmedTelmHmi_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_collection_occpt_ped_sfty_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_Collection_OccptPedSfty_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0207
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_Collection_OccptPedSfty_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_collection_pt_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_Collection_Pt_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0208
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_Collection_Pt_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_compu_method_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0209
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_CompuMethod_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_compu_method_lifecycle_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_CompuMethod_LifeCycle_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0210
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_CompuMethod_LifeCycle_Standard.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_data_constr_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_DataConstr_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0211
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_DataConstr_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_data_constr_lifecycle_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_DataConstr_LifeCycle_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0212
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_DataConstr_LifeCycle_Standard.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_keyword_set_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_KeywordSet_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0213
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_KeywordSet_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_keyword_lifecycle_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_Keyword_LifeCycle_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0214
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_Keyword_LifeCycle_Standard.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_physical_dimension_lifecycle_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_PhysicalDimension_LifeCycle_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0215
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_PhysicalDimension_LifeCycle_Standard.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_physical_dimension_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_PhysicalDimension_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0216
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_PhysicalDimension_Standard.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_port_interface_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_PortInterface_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0217
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_PortInterface_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_port_interface_lifecycle_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_PortInterface_LifeCycle_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0218
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_PortInterface_LifeCycle_Standard.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_port_prototype_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0219
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_port_prototype_blueprint_lifecycle_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_LifeCycle_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0220
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_PortPrototypeBlueprint_LifeCycle_Standard.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_sw_component_types_blueprint_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_SwComponentTypes_Blueprint.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0221
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_SwComponentTypes_Blueprint.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_unit_lifecycle_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_Unit_LifeCycle_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0222
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_Unit_LifeCycle_Standard.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail(reason="Binary comparison not yet passing - work in progress")
    def test_unit_standard_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test AUTOSAR_MOD_AISpecification_Unit_Standard.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0223
        """
        self._test_single_file_binary_comparison(
            "AUTOSAR_MOD_AISpecification_Unit_Standard.arxml",
            reader,
            writer,
            tmp_path
        )
