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
from typing import List, Tuple
import difflib

from armodel.reader import ARXMLReader
from armodel.writer import ARXMLWriter
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

    @pytest.mark.xfail
    def test_bswm_mode_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test BswMMode.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0224
        """
        self._test_single_file_binary_comparison(
            "BswMMode.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail
    def test_bswm_bswmd_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test BswM_Bswmd.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0225
        """
        self._test_single_file_binary_comparison(
            "BswM_Bswmd.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail
    def test_can_system_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test CanSystem.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0226
        """
        self._test_single_file_binary_comparison(
            "CanSystem.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail
    def test_software_components_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test SoftwareComponents.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0227
        """
        self._test_single_file_binary_comparison(
            "SoftwareComponents.arxml",
            reader,
            writer,
            tmp_path
        )

    @pytest.mark.xfail
    def test_sw_record_demo_binary_comparison(
        self,
        reader: ARXMLReader,
        writer: ARXMLWriter,
        tmp_path: Path
    ) -> None:
        """Test SwRecordDemo.arxml for binary exact round-trip serialization.

        Test ID: SWITS-INT-0228
        """
        self._test_single_file_binary_comparison(
            "SwRecordDemo.arxml",
            reader,
            writer,
            tmp_path
        )
