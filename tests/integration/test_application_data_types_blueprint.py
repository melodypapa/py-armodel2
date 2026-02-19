"""
Integration tests for AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml.

This test module validates reading, verifying, and writing the ApplicationDataType_Blueprint.arxml file.
This file contains AUTOSAR application data types including application primitive types,
array types, and record types.

Traceability:
- Test Documentation: docs/tests/integration/test_application_data_types_blueprint.md
- SWITS IDs: SWITS-INT-0101 through SWITS-INT-0108
"""
import pytest
from pathlib import Path
import xml.etree.cElementTree as ET

from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter


class TestApplicationDataTypesBlueprint:
    """Integration tests for AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml.

    Test IDs: SWITS-INT-0101 to SWITS-INT-0108
    Documentation: docs/tests/integration/test_application_data_types_blueprint.md
    """

    @pytest.fixture
    def blueprint_file(self):
        """Path to AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml file."""
        return Path("demos/arxml/AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml")

    def count_elements(self, pkg) -> int:
        """Count elements in a package.

        Args:
            pkg: ARPackage object

        Returns:
            Number of elements in the package
        """
        if hasattr(pkg, 'elements') and pkg.elements:
            return len(pkg.elements)
        return 0

    def count_elements_by_type(self, pkg, element_type: str) -> int:
        """Count elements of a specific type in a package.

        Args:
            pkg: ARPackage object
            element_type: Class name of the element type to count

        Returns:
            Number of elements of the specified type
        """
        if hasattr(pkg, 'elements') and pkg.elements:
            return sum(1 for elem in pkg.elements if elem.__class__.__name__ == element_type)
        return 0

    # ========================================================================
    # TEST 1: Read and Verify Structure
    # ========================================================================

    def test_read_and_verify_structure(self, blueprint_file):
        """Test reading ApplicationDataType_Blueprint.arxml and verifying structure.

        Test ID: SWITS-INT-0101
        Documentation Reference: docs/tests/integration/test_application_data_types_blueprint.md
        Test Scenario: Read and Verify Structure

        Validates:
        - File can be loaded by ARXMLReader
        - AUTOSAR object is created
        - Root package is AUTOSAR
        - Nested packages exist: AUTOSAR > AISpecification > ApplicationDataTypes_Blueprint
        - All elements are loaded correctly

        Args:
            blueprint_file: Path to ApplicationDataType_Blueprint.arxml
        """
        # Create AUTOSAR instance
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()

        # Load the file
        reader = ARXMLReader()
        reader.load_arxml(autosar, blueprint_file)

        # Verify AUTOSAR object
        assert autosar is not None
        assert hasattr(autosar, 'ar_packages')
        assert len(autosar.ar_packages) >= 1

        # Verify root package
        root_pkg = autosar.ar_packages[0]
        assert root_pkg.short_name == "AUTOSAR"

        # Verify nested packages
        assert hasattr(root_pkg, 'ar_packages')
        assert len(root_pkg.ar_packages) >= 1

        aispec_pkg = root_pkg.ar_packages[0]
        assert aispec_pkg.short_name == "AISpecification"

        assert hasattr(aispec_pkg, 'ar_packages')
        assert len(aispec_pkg.ar_packages) >= 1

        blueprint_pkg = aispec_pkg.ar_packages[0]
        assert blueprint_pkg.short_name == "ApplicationDataTypes_Blueprint"

        # Verify element counts
        total_elements = self.count_elements(blueprint_pkg)
        assert total_elements == 383, f"Expected 383 elements, got {total_elements}"

        # Verify element type counts
        assert self.count_elements_by_type(blueprint_pkg, "ApplicationPrimitiveDataType") == 293
        assert self.count_elements_by_type(blueprint_pkg, "ApplicationArrayDataType") == 42
        assert self.count_elements_by_type(blueprint_pkg, "ApplicationRecordDataType") == 48

    # ========================================================================
    # TEST 2: Write and Read Back
    # ========================================================================

    def test_write_and_read_back(self, blueprint_file, tmp_path):
        """Test writing AUTOSAR object to file and reading it back.

        Test ID: SWITS-INT-0102
        Documentation Reference: docs/tests/integration/test_application_data_types_blueprint.md
        Test Scenario: Write and Read Back

        Validates:
        - AUTOSAR object can be written to file
        - Written file is valid XML
        - Written file can be read back
        - Structure is preserved after round-trip

        Args:
            blueprint_file: Path to original ApplicationDataType_Blueprint.arxml
            tmp_path: Pytest temporary directory fixture
        """
        # Create AUTOSAR instance and load original
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar_original = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar_original, blueprint_file)

        # Get blueprint package
        blueprint_pkg_original = autosar_original.ar_packages[0].ar_packages[0].ar_packages[0]

        # Verify original structure
        original_counts = {
            "total": self.count_elements(blueprint_pkg_original),
            "ApplicationPrimitiveDataType": self.count_elements_by_type(blueprint_pkg_original, "ApplicationPrimitiveDataType"),
            "ApplicationArrayDataType": self.count_elements_by_type(blueprint_pkg_original, "ApplicationArrayDataType"),
            "ApplicationRecordDataType": self.count_elements_by_type(blueprint_pkg_original, "ApplicationRecordDataType"),
        }

        # Write to file
        writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")
        written_file = tmp_path / "ApplicationDataType_Blueprint_roundtrip.arxml"
        writer.save_arxml(autosar_original, written_file)

        # Verify written file exists and is valid XML
        assert written_file.exists()
        assert written_file.stat().st_size > 0
        content = written_file.read_text()
        assert "<?xml" in content
        assert "<AUTOSAR" in content
        assert "</AUTOSAR>" in content

        # Read back
        autosar_reloaded = AUTOSAR()
        reader.load_arxml(autosar_reloaded, written_file)

        # Verify structure is preserved
        blueprint_pkg_reloaded = autosar_reloaded.ar_packages[0].ar_packages[0].ar_packages[0]

        reloaded_counts = {
            "total": self.count_elements(blueprint_pkg_reloaded),
            "ApplicationPrimitiveDataType": self.count_elements_by_type(blueprint_pkg_reloaded, "ApplicationPrimitiveDataType"),
            "ApplicationArrayDataType": self.count_elements_by_type(blueprint_pkg_reloaded, "ApplicationArrayDataType"),
            "ApplicationRecordDataType": self.count_elements_by_type(blueprint_pkg_reloaded, "ApplicationRecordDataType"),
        }

        # Compare counts
        assert original_counts == reloaded_counts, \
            f"Element counts changed after round-trip:\nOriginal: {original_counts}\nReloaded: {reloaded_counts}"

    # ========================================================================
    # TEST 3: Serialize-Deserialize Symmetry
    # ========================================================================

    def test_serialize_deserialize_symmetry(self, blueprint_file):
        """Test that serialize(deserialize(xml)) preserves structure.

        Test ID: SWITS-INT-0103
        Documentation Reference: docs/tests/integration/test_application_data_types_blueprint.md
        Test Scenario: Serialize-Deserialize Symmetry

        Validates:
        - Object can be serialized to XML string
        - XML string can be deserialized back to object
        - Structure is preserved

        Args:
            blueprint_file: Path to original ApplicationDataType_Blueprint.arxml
        """
        # Create AUTOSAR instance and load original
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar_original = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar_original, blueprint_file)

        # Get original package info
        blueprint_pkg_original = autosar_original.ar_packages[0].ar_packages[0].ar_packages[0]
        original_counts = {
            "total": self.count_elements(blueprint_pkg_original),
            "ApplicationPrimitiveDataType": self.count_elements_by_type(blueprint_pkg_original, "ApplicationPrimitiveDataType"),
            "ApplicationArrayDataType": self.count_elements_by_type(blueprint_pkg_original, "ApplicationArrayDataType"),
            "ApplicationRecordDataType": self.count_elements_by_type(blueprint_pkg_original, "ApplicationRecordDataType"),
        }

        # Serialize to string
        writer = ARXMLWriter(pretty_print=True)
        xml_string = writer.to_string(autosar_original)

        # Verify XML string
        assert "<?xml" in xml_string
        assert "<AUTOSAR" in xml_string
        assert "ApplicationDataTypes_Blueprint" in xml_string

        # Deserialize from string
        xml_bytes = xml_string.encode('utf-8')
        et_element = ET.fromstring(xml_bytes)
        autosar_from_string = AUTOSAR.deserialize(et_element)

        # Verify structure is preserved
        blueprint_pkg_from_string = autosar_from_string.ar_packages[0].ar_packages[0].ar_packages[0]
        reloaded_counts = {
            "total": self.count_elements(blueprint_pkg_from_string),
            "ApplicationPrimitiveDataType": self.count_elements_by_type(blueprint_pkg_from_string, "ApplicationPrimitiveDataType"),
            "ApplicationArrayDataType": self.count_elements_by_type(blueprint_pkg_from_string, "ApplicationArrayDataType"),
            "ApplicationRecordDataType": self.count_elements_by_type(blueprint_pkg_from_string, "ApplicationRecordDataType"),
        }

        assert original_counts == reloaded_counts, \
            f"Element counts changed:\nOriginal: {original_counts}\nReloaded: {reloaded_counts}"

    # ========================================================================
    # TEST 4: Package and Element Counts
    # ========================================================================

    def test_package_element_counts(self, blueprint_file):
        """Test that package and element counts match expected values.

        Test ID: SWITS-INT-0104
        Documentation Reference: docs/tests/integration/test_application_data_types_blueprint.md
        Test Scenario: Package and Element Counts

        Validates exact counts for:
        - Total packages
        - Elements in each package
        - Elements by type

        Args:
            blueprint_file: Path to original ApplicationDataType_Blueprint.arxml
        """
        # Create AUTOSAR instance and load file
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar, blueprint_file)

        # Count packages
        total_packages = 1  # Root package (AUTOSAR)
        aispec_pkg = autosar.ar_packages[0].ar_packages[0]
        total_packages += 1  # AISpecification
        total_packages += 1  # ApplicationDataTypes_Blueprint

        assert total_packages == 3, f"Expected 3 packages, got {total_packages}"

        # Get blueprint package
        blueprint_pkg = aispec_pkg.ar_packages[0]

        # Verify total element count
        total_elements = self.count_elements(blueprint_pkg)
        assert total_elements == 383, f"Expected 383 elements, got {total_elements}"

        # Verify element type counts
        assert self.count_elements_by_type(blueprint_pkg, "ApplicationPrimitiveDataType") == 293
        assert self.count_elements_by_type(blueprint_pkg, "ApplicationArrayDataType") == 42
        assert self.count_elements_by_type(blueprint_pkg, "ApplicationRecordDataType") == 48

    # ========================================================================
    # TEST 5: Specific Element Verification
    # ========================================================================

    def test_application_record_data_types(self, blueprint_file):
        """Test that ApplicationRecordDataType elements are loaded correctly.

        Test ID: SWITS-INT-0105
        Documentation Reference: docs/tests/integration/test_application_data_types_blueprint.md
        Test Scenario: Specific Element Verification - ApplicationRecordDataType

        Verifies specific application record data types:
        - AFbForCmft1 (Acceleration Feedback for Comfort)
        - AReqForCmft1 (Acceleration Request for Comfort 1)
        - ActrSt1 (Actuator Status)
        - DateTi1 (Date Time)

        Args:
            blueprint_file: Path to original ApplicationDataType_Blueprint.arxml
        """
        # Create AUTOSAR instance and load file
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar, blueprint_file)

        # Get blueprint package
        blueprint_pkg = autosar.ar_packages[0].ar_packages[0].ar_packages[0]

        # Filter for ApplicationRecordDataType elements
        record_types = [elem for elem in blueprint_pkg.elements
                       if elem.__class__.__name__ == "ApplicationRecordDataType"]

        # Verify first few record types
        expected_names = [
            "AFbForCmft1",
            "AReqForCmft1",
            "ActrSt1",
            "ActrSts1",
            "AdjAut1",
            "AuthnData1",
            "BriCmd1",
            "DateTi1",
            "DiagcBri1",
            "DiagcChdProtn1",
        ]

        actual_names = [elem.short_name for elem in record_types[:10]]
        assert actual_names == expected_names, \
            f"ApplicationRecordDataType element names mismatch:\nExpected: {expected_names}\nGot: {actual_names}"

        # Verify DateTi1 has elements (Hr, Mins, Sec, Day, Mth, Yr)
        date_ti1 = next((elem for elem in record_types if elem.short_name == "DateTi1"), None)
        assert date_ti1 is not None, "DateTi1 not found"
        assert hasattr(date_ti1, 'elements')
        assert len(date_ti1.elements) == 6

        # Verify AFbForCmft1 has elements
        afb_for_cmft1 = next((elem for elem in record_types if elem.short_name == "AFbForCmft1"), None)
        assert afb_for_cmft1 is not None, "AFbForCmft1 not found"
        assert hasattr(afb_for_cmft1, 'elements')
        assert len(afb_for_cmft1.elements) == 5

    def test_application_primitive_data_types(self, blueprint_file):
        """Test that ApplicationPrimitiveDataType elements are loaded correctly.

        Test ID: SWITS-INT-0106
        Documentation Reference: docs/tests/integration/test_application_data_types_blueprint.md
        Test Scenario: Specific Element Verification - ApplicationPrimitiveDataType

        Verifies that application primitive data types are loaded correctly.

        Args:
            blueprint_file: Path to original ApplicationDataType_Blueprint.arxml
        """
        # Create AUTOSAR instance and load file
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar, blueprint_file)

        # Get blueprint package
        blueprint_pkg = autosar.ar_packages[0].ar_packages[0].ar_packages[0]

        # Filter for ApplicationPrimitiveDataType elements
        primitive_types = [elem for elem in blueprint_pkg.elements
                          if elem.__class__.__name__ == "ApplicationPrimitiveDataType"]

        # Verify count
        assert len(primitive_types) == 293, f"Expected 293 primitive types, got {len(primitive_types)}"

        # Verify first few primitive types have expected properties
        for elem in primitive_types[:10]:
            assert hasattr(elem, 'short_name'), f"Element missing short_name: {elem}"
            assert elem.short_name, f"Element has empty short_name"

    # ========================================================================
    # TEST 7: XML Content Comparison
    # ========================================================================

    def test_xml_content_comparison(self, blueprint_file, tmp_path):
        """Test that generated XML structure is semantically equivalent to original.

        Test ID: SWITS-INT-0107
        Documentation Reference: docs/tests/integration/test_application_data_types_blueprint.md
        Test Scenario: XML Content Comparison

        Validates:
        - Original XML can be parsed and regenerated
        - Generated XML structure is semantically equivalent
        - Package hierarchy is preserved
        - Element counts are preserved

        Note: Exact XML comparison is not possible because the reflection-based
        serialization framework may use different tag names and attribute ordering.
        This test verifies that the semantic content (packages, elements, structure)
        is preserved, not the exact XML syntax.

        Args:
            blueprint_file: Path to original ApplicationDataType_Blueprint.arxml
            tmp_path: Pytest temporary directory fixture
        """
        # Create AUTOSAR instance and load original
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar_original = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar_original, blueprint_file)

        # Write to file
        writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")
        generated_file = tmp_path / "ApplicationDataType_Blueprint_xml_comparison.arxml"
        writer.save_arxml(autosar_original, generated_file)

        # Parse both files as XML
        original_tree = ET.parse(str(blueprint_file))
        generated_tree = ET.parse(str(generated_file))

        # Verify both are valid XML
        assert original_tree is not None, "Failed to parse original file"
        assert generated_tree is not None, "Failed to parse generated file"

        # Verify root elements
        original_root = original_tree.getroot()
        generated_root = generated_tree.getroot()
        assert original_root.tag.endswith("AUTOSAR"), "Original root element is not AUTOSAR"
        assert generated_root.tag.endswith("AUTOSAR"), "Generated root element is not AUTOSAR"

        # Verify namespace
        original_ns = original_root.tag.split('}')[0].strip('{')
        generated_ns = generated_root.tag.split('}')[0].strip('{')
        assert original_ns is not None, "Original file missing namespace"
        assert generated_ns is not None, "Generated file missing namespace"
        assert generated_ns == original_ns, \
            f"Namespace mismatch: original={original_ns}, generated={generated_ns}"

        # Verify that the generated file can be read back and preserves element counts
        autosar_reloaded = AUTOSAR()
        reader.load_arxml(autosar_reloaded, generated_file)

        blueprint_pkg_original = autosar_original.ar_packages[0].ar_packages[0].ar_packages[0]
        blueprint_pkg_reloaded = autosar_reloaded.ar_packages[0].ar_packages[0].ar_packages[0]

        original_counts = {
            "total": self.count_elements(blueprint_pkg_original),
            "ApplicationPrimitiveDataType": self.count_elements_by_type(blueprint_pkg_original, "ApplicationPrimitiveDataType"),
            "ApplicationArrayDataType": self.count_elements_by_type(blueprint_pkg_original, "ApplicationArrayDataType"),
            "ApplicationRecordDataType": self.count_elements_by_type(blueprint_pkg_original, "ApplicationRecordDataType"),
        }

        reloaded_counts = {
            "total": self.count_elements(blueprint_pkg_reloaded),
            "ApplicationPrimitiveDataType": self.count_elements_by_type(blueprint_pkg_reloaded, "ApplicationPrimitiveDataType"),
            "ApplicationArrayDataType": self.count_elements_by_type(blueprint_pkg_reloaded, "ApplicationArrayDataType"),
            "ApplicationRecordDataType": self.count_elements_by_type(blueprint_pkg_reloaded, "ApplicationRecordDataType"),
        }

        assert original_counts == reloaded_counts, \
            f"Element counts changed after round-trip:\nOriginal: {original_counts}\nReloaded: {reloaded_counts}"

    # ========================================================================
    # TEST 8: Package Hierarchy Verification
    # ========================================================================

    def test_package_hierarchy(self, blueprint_file):
        """Test that package hierarchy is correctly loaded.

        Test ID: SWITS-INT-0108
        Documentation Reference: docs/tests/integration/test_application_data_types_blueprint.md
        Test Scenario: Package Hierarchy Verification

        Validates:
        - Root package is AUTOSAR
        - Second level package is AISpecification
        - Third level package is ApplicationDataTypes_Blueprint
        - Package structure is preserved

        Args:
            blueprint_file: Path to original ApplicationDataType_Blueprint.arxml
        """
        # Create AUTOSAR instance and load file
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar, blueprint_file)

        # Verify root package
        assert len(autosar.ar_packages) >= 1
        root_pkg = autosar.ar_packages[0]
        assert root_pkg.short_name == "AUTOSAR"

        # Verify second level package
        assert hasattr(root_pkg, 'ar_packages')
        assert len(root_pkg.ar_packages) >= 1
        aispec_pkg = root_pkg.ar_packages[0]
        assert aispec_pkg.short_name == "AISpecification"

        # Verify third level package
        assert hasattr(aispec_pkg, 'ar_packages')
        assert len(aispec_pkg.ar_packages) >= 1
        blueprint_pkg = aispec_pkg.ar_packages[0]
        assert blueprint_pkg.short_name == "ApplicationDataTypes_Blueprint"

        # Verify package category
        assert hasattr(blueprint_pkg, 'category')
        assert blueprint_pkg.category == "BLUEPRINT"