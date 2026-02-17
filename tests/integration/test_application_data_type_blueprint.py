"""Integration test for loading AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml"""

import pytest
from pathlib import Path
from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR


class TestApplicationDataTypeBlueprint:
    """Test reading and writing Application Data Type Blueprint ARXML file"""

    @pytest.fixture
    def arxml_file_path(self) -> Path:
        """Get path to the ARXML file"""
        return Path("demos/arxml/AUTOSAR_MOD_AISpecification_ApplicationDataType_Blueprint.arxml")

    @pytest.mark.skip(reason="deserialize() method not yet implemented in generated code")
    def test_load_file(self, arxml_file_path: Path):
        """Test loading the ARXML file"""
        if not arxml_file_path.exists():
            pytest.skip(f"ARXML file not found: {arxml_file_path}")

        reader = ARXMLReader()

        # Detect schema version
        version = reader.get_schema_version(arxml_file_path)
        print(f"Schema version: {version}")

        # Load the file
        autosar = reader.load_arxml(arxml_file_path)

        assert autosar is not None
        assert isinstance(autosar, AUTOSAR)
        assert hasattr(autosar, 'ar_packages')
        assert len(autosar.ar_packages) > 0

        print(f"Number of top-level packages: {len(autosar.ar_packages)}")

        # Navigate to AISpecification/ApplicationDataTypes_Blueprint
        for pkg in autosar.ar_packages:
            print(f"Package: {pkg.short_name} (category: {pkg.category or 'N/A'})")
            assert pkg.short_name == "AUTOSAR"

            for sub_pkg in pkg.ar_packages:
                print(f"  Sub-package: {sub_pkg.short_name} (category: {sub_pkg.category or 'N/A'})")
                assert sub_pkg.short_name == "AISpecification"

                for sub_sub_pkg in sub_pkg.ar_packages:
                    print(f"    Sub-sub-package: {sub_sub_pkg.short_name} (category: {sub_sub_pkg.category or 'N/A'})")

                    if sub_sub_pkg.short_name == "ApplicationDataTypes_Blueprint":
                        print(f"      Has reference bases: {len(sub_sub_pkg.reference_bases) > 0}")
                        print(f"      Has elements: {len(sub_sub_pkg.elements) > 0}")
                        print(f"      Has sub-packages: {len(sub_sub_pkg.ar_packages) > 0}")
                        print(f"      Number of elements: {len(sub_sub_pkg.elements) if hasattr(sub_sub_pkg, 'elements') and sub_sub_pkg.elements else 0}")
                        print(f"      Number of sub-packages: {len(sub_sub_pkg.ar_packages) if hasattr(sub_sub_pkg, 'ar_packages') else 0}")

    @pytest.mark.skip(reason="Round-trip test - needs deserialize() and get_schema_version() methods")
    def test_round_trip(self, arxml_file_path: Path, tmp_path):
        """Test reading and writing back the file"""
        if not arxml_file_path.exists():
            pytest.skip(f"ARXML file not found: {arxml_file_path}")

        reader = ARXMLReader()
        writer = ARXMLWriter(pretty_print=True)

        # Load original
        original = reader.load_arxml(arxml_file_path)

        # Write to temp file
        output_path = tmp_path / "output.arxml"
        writer.save_arxml(original, output_path)

        # Load roundtrip
        roundtrip = reader.load_arxml(output_path)

        # Verify structure is preserved
        assert original is not None
        assert roundtrip is not None
        assert len(original.ar_packages) == len(roundtrip.ar_packages)
