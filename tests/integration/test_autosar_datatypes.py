"""Integration tests for AUTOSAR_Datatypes.arxml.

This test module validates reading, verifying, and writing the AUTOSAR_Datatypes.arxml file.
This file contains platform base types, computation methods, data constraints, and
implementation data types.
"""

import pytest
from pathlib import Path
from lxml import etree

from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter


class TestAUTOSARDatatypes:
    """Integration tests for AUTOSAR_Datatypes.arxml."""

    @pytest.fixture
    def datatypes_file(self):
        """Path to AUTOSAR_Datatypes.arxml file."""
        return Path("demos/arxml/AUTOSAR_Datatypes.arxml")

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

    # ========================================================================
    # TEST 1: Read and Verify Structure
    # ========================================================================

    def test_read_and_verify_structure(self, datatypes_file):
        """Test reading AUTOSAR_Datatypes.arxml and verifying structure.

        Validates:
        - File can be loaded by ARXMLReader
        - AUTOSAR object is created
        - Root package is AUTOSAR_Platform
        - 4 nested packages exist
        - All elements are loaded correctly

        Args:
            datatypes_file: Path to AUTOSAR_Datatypes.arxml
        """
        # Create AUTOSAR instance
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()

        # Load the file
        reader = ARXMLReader()
        reader.load_arxml(autosar, datatypes_file)

        # Verify AUTOSAR object
        assert autosar is not None
        assert hasattr(autosar, 'ar_packages')
        assert len(autosar.ar_packages) >= 1

        # Verify root package
        root_pkg = autosar.ar_packages[0]
        assert root_pkg.short_name == "AUTOSAR_Platform"

        # Verify nested packages
        nested_packages = root_pkg.ar_packages
        assert len(nested_packages) == 4

        expected_packages = ["BaseTypes", "CompuMethods", "DataConstrs", "ImplementationDataTypes"]
        actual_packages = [pkg.short_name for pkg in nested_packages]
        assert actual_packages == expected_packages

        # Verify BaseTypes has 15 elements
        base_types_pkg = nested_packages[0]
        assert base_types_pkg.short_name == "BaseTypes"
        assert self.count_elements(base_types_pkg) == 15
        assert base_types_pkg.elements[0].short_name == "float32"

        # Verify CompuMethods has 1 element
        compu_methods_pkg = nested_packages[1]
        assert compu_methods_pkg.short_name == "CompuMethods"
        assert self.count_elements(compu_methods_pkg) == 1
        assert compu_methods_pkg.elements[0].short_name == "boolean_Literals"

        # Verify DataConstrs has 12 elements
        data_constrs_pkg = nested_packages[2]
        assert data_constrs_pkg.short_name == "DataConstrs"
        assert self.count_elements(data_constrs_pkg) == 12
        assert data_constrs_pkg.elements[0].short_name == "sint16"

        # Verify ImplementationDataTypes has 15 elements
        impl_types_pkg = nested_packages[3]
        assert impl_types_pkg.short_name == "ImplementationDataTypes"
        assert self.count_elements(impl_types_pkg) == 15
        assert impl_types_pkg.elements[0].short_name == "boolean"

    # ========================================================================
    # TEST 2: Write and Read Back
    # ========================================================================

    def test_write_and_read_back(self, datatypes_file, tmp_path):
        """Test writing AUTOSAR object to file and reading it back.

        Validates:
        - AUTOSAR object can be written to file
        - Written file is valid XML
        - Written file can be read back
        - Structure is preserved after round-trip

        Args:
            datatypes_file: Path to original AUTOSAR_Datatypes.arxml
            tmp_path: Pytest temporary directory fixture
        """
        # Create AUTOSAR instance and load original
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar_original = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar_original, datatypes_file)

        # Verify original structure
        root_pkg_original = autosar_original.ar_packages[0]
        nested_packages_original = root_pkg_original.ar_packages
        original_counts = {
            pkg.short_name: self.count_elements(pkg)
            for pkg in nested_packages_original
        }

        # Write to file
        writer = ARXMLWriter(pretty_print=True, encoding="UTF-8")
        written_file = tmp_path / "AUTOSAR_Datatypes_roundtrip.arxml"
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
        root_pkg_reloaded = autosar_reloaded.ar_packages[0]
        nested_packages_reloaded = root_pkg_reloaded.ar_packages
        reloaded_counts = {
            pkg.short_name: self.count_elements(pkg)
            for pkg in nested_packages_reloaded
        }

        # Compare counts
        assert original_counts == reloaded_counts, \
            f"Element counts changed after round-trip:\nOriginal: {original_counts}\nReloaded: {reloaded_counts}"

    # ========================================================================
    # TEST 3: Serialize-Deserialize Symmetry
    # ========================================================================

    def test_serialize_deserialize_symmetry(self, datatypes_file):
        """Test that serialize(deserialize(xml)) preserves structure.

        Validates:
        - Object can be serialized to XML string
        - XML string can be deserialized back to object
        - Structure is preserved

        Args:
            datatypes_file: Path to original AUTOSAR_Datatypes.arxml
        """
        # Create AUTOSAR instance and load original
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar_original = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar_original, datatypes_file)

        # Get original package info
        root_pkg_original = autosar_original.ar_packages[0]
        nested_packages_original = root_pkg_original.ar_packages
        original_count = len(nested_packages_original)
        original_element_counts = {
            pkg.short_name: self.count_elements(pkg)
            for pkg in nested_packages_original
        }

        # Serialize to string
        writer = ARXMLWriter(pretty_print=True)
        xml_string = writer.to_string(autosar_original)

        # Verify XML string
        assert "<?xml" in xml_string
        assert "<AUTOSAR" in xml_string
        assert "AUTOSAR_Platform" in xml_string

        # Deserialize from string
        xml_bytes = xml_string.encode('utf-8')
        lxml_element = etree.fromstring(xml_bytes)
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar_from_string = AUTOSAR.deserialize(lxml_element)

        # Verify structure is preserved
        root_pkg_from_string = autosar_from_string.ar_packages[0]
        nested_packages_from_string = root_pkg_from_string.ar_packages
        reloaded_count = len(nested_packages_from_string)
        reloaded_element_counts = {
            pkg.short_name: self.count_elements(pkg)
            for pkg in nested_packages_from_string
        }

        assert original_count == reloaded_count, \
            f"Package count changed: original={original_count}, reloaded={reloaded_count}"
        assert original_element_counts == reloaded_element_counts, \
            f"Element counts changed:\nOriginal: {original_element_counts}\nReloaded: {reloaded_element_counts}"

    # ========================================================================
    # TEST 4: Package and Element Counts
    # ========================================================================

    def test_package_element_counts(self, datatypes_file):
        """Test that package and element counts match expected values.

        Validates exact counts for:
        - Total packages
        - Elements in each package

        Args:
            datatypes_file: Path to original AUTOSAR_Datatypes.arxml
        """
        # Create AUTOSAR instance and load file
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar, datatypes_file)

        # Count packages
        total_packages = 1  # Root package
        root_pkg = autosar.ar_packages[0]
        nested_packages = root_pkg.ar_packages
        total_packages += len(nested_packages)

        assert total_packages == 5, f"Expected 5 packages, got {total_packages}"

        # Count elements in each package
        expected_element_counts = {
            "BaseTypes": 15,
            "CompuMethods": 1,
            "DataConstrs": 12,
            "ImplementationDataTypes": 15,
        }

        for pkg in nested_packages:
            count = self.count_elements(pkg)
            expected = expected_element_counts[pkg.short_name]
            assert count == expected, \
                f"Element count mismatch for {pkg.short_name}: expected {expected}, got {count}"

    # ========================================================================
    # TEST 5: Specific Element Verification
    # ========================================================================

    def test_base_types_elements(self, datatypes_file):
        """Test that BaseTypes package has correct elements.

        Verifies specific base types:
        - float32, float64
        - sint8, sint16, sint32
        - uint8, uint16, uint32
        - void type

        Args:
            datatypes_file: Path to original AUTOSAR_Datatypes.arxml
        """
        # Create AUTOSAR instance and load file
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar, datatypes_file)

        # Get BaseTypes package
        root_pkg = autosar.ar_packages[0]
        base_types_pkg = root_pkg.ar_packages[0]
        elements = base_types_pkg.elements

        # Expected element names (in order)
        expected_names = [
            "float32", "float64",
            "sint16", "sint16_least",
            "sint32", "sint32_least",
            "sint8", "sint8_least",
            "uint16", "uint16_least",
            "uint32", "uint32_least",
            "uint8", "uint8_least",
            "void",
        ]

        actual_names = [elem.short_name for elem in elements]
        assert actual_names == expected_names, \
            f"BaseTypes element names mismatch:\nExpected: {expected_names}\nGot: {actual_names}"

    def test_implementation_data_types_elements(self, datatypes_file):
        """Test that ImplementationDataTypes package has correct elements.

        Verifies specific implementation types:
        - boolean
        - float32, float64
        - sint8, sint16, sint32 (and _least variants)
        - uint8, uint16, uint32 (and _least variants)

        Args:
            datatypes_file: Path to original AUTOSAR_Datatypes.arxml
        """
        # Create AUTOSAR instance and load file
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        autosar = AUTOSAR()
        reader = ARXMLReader()
        reader.load_arxml(autosar, datatypes_file)

        # Get ImplementationDataTypes package
        root_pkg = autosar.ar_packages[0]
        impl_types_pkg = root_pkg.ar_packages[3]
        elements = impl_types_pkg.elements

        # Expected element names (in order)
        expected_names = [
            "boolean",
            "float32", "float64",
            "sint16", "sint16_least",
            "sint32", "sint32_least",
            "sint8", "sint8_least",
            "uint16", "uint16_least",
            "uint32", "uint32_least",
            "uint8", "uint8_least",
        ]

        actual_names = [elem.short_name for elem in elements]
        assert actual_names == expected_names, \
            f"ImplementationDataTypes element names mismatch:\nExpected: {expected_names}\nGot: {actual_names}"
