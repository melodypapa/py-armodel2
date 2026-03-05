"""
Integration tests for ARXML reader encoding detection.

This test module validates that the ARXMLReader correctly handles
files with different encodings, respecting the encoding declaration
in the XML header.

Test Strategy:
- Test reading ISO-8859-1 encoded files
- Test reading UTF-8 encoded files
- Test reading files without encoding declaration
- Validate round-trip serialization preserves encoding

Traceability:
- Test Documentation: docs/tests/integration/test_reader_encoding.md
- SWITS IDs: SWITS-INT-0300 through SWITS-INT-0399
"""
import pytest
from pathlib import Path

from armodel2.reader import ARXMLReader
from armodel2.writer import ARXMLWriter
from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR


class TestReaderEncoding:
    """Test ARXML reader encoding detection and handling.

    Test IDs: SWITS-INT-0300 to SWITS-INT-0399
    """

    @pytest.fixture
    def reader(self) -> ARXMLReader:
        """ARXML reader instance."""
        return ARXMLReader()

    @pytest.fixture
    def writer(self) -> ARXMLWriter:
        """ARXML writer instance."""
        return ARXMLWriter(pretty_print=True, encoding="UTF-8")

    def test_read_iso_8859_1_file(self, reader: ARXMLReader) -> None:
        """Test reading an ISO-8859-1 encoded ARXML file.

        Validates that the reader correctly detects and reads
        files with ISO-8859-1 encoding from the XML declaration.

        Test ID: SWITS-INT-0301
        """
        # Adc_Bswmd.arxml uses ISO-8859-1 encoding
        arxml_file = Path("demos/arxml/Adc_Bswmd.arxml")
        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        AUTOSAR.reset()
        autosar = AUTOSAR()

        # Should not raise UnicodeDecodeError
        reader.load_arxml(str(arxml_file), autosar)

        # Validate that data was loaded
        assert autosar.ar_packages is not None
        assert len(autosar.ar_packages) > 0

    def test_read_utf_8_file(self, reader: ARXMLReader) -> None:
        """Test reading a UTF-8 encoded ARXML file.

        Validates that the reader correctly handles UTF-8 encoded files.

        Test ID: SWITS-INT-0302
        """
        # AUTOSAR_Datatypes.arxml uses UTF-8 encoding
        arxml_file = Path("demos/validated/AUTOSAR_Datatypes.arxml")
        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        AUTOSAR.reset()
        autosar = AUTOSAR()

        # Should read successfully
        reader.load_arxml(str(arxml_file), autosar)

        # Validate that data was loaded
        assert autosar.ar_packages is not None
        assert len(autosar.ar_packages) > 0

        # Verify encoding was detected and stored
        assert autosar.encoding == "UTF-8"

    def test_iso_8859_1_round_trip(self, reader: ARXMLReader, writer: ARXMLWriter, tmp_path: Path) -> None:
        """Test round-trip serialization of ISO-8859-1 file.

        Validates that reading an ISO-8859-1 file and writing it back
        produces a valid ARXML file with ISO-8859-1 encoding preserved.

        Test ID: SWITS-INT-0303
        """
        arxml_file = Path("demos/arxml/Adc_Bswmd.arxml")
        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        AUTOSAR.reset()
        autosar = AUTOSAR()

        # Read ISO-8859-1 file
        reader.load_arxml(str(arxml_file), autosar)

        # Verify encoding was detected and stored
        assert autosar.encoding == "ISO-8859-1"

        # Write back (should preserve ISO-8859-1 encoding)
        output_file = tmp_path / "Adc_Bswmd_output.arxml"
        writer.save_arxml(str(output_file), autosar)

        # Validate output file exists and is valid XML
        assert output_file.exists()
        content = output_file.read_text(encoding="ISO-8859-1")
        assert "<?xml" in content
        assert "AUTOSAR" in content

        # Verify the XML declaration preserves the encoding
        assert 'encoding="ISO-8859-1"' in content

    def test_read_multiple_iso_8859_1_files(self, reader: ARXMLReader) -> None:
        """Test reading multiple ISO-8859-1 encoded files.

        Validates that the reader can handle various ISO-8859-1 files
        from the demos directory.

        Test ID: SWITS-INT-0304
        """
        # List of ISO-8859-1 files to test
        iso_8859_1_files = [
            "Adc_Bswmd.arxml",
            "Atomics_Bswmd.arxml",
            "Base_Bswmd.arxml",
        ]

        for filename in iso_8859_1_files:
            arxml_file = Path("demos/arxml") / filename
            if not arxml_file.exists():
                pytest.skip(f"File not found: {arxml_file}")

            AUTOSAR.reset()
            autosar = AUTOSAR()

            # Should read successfully
            reader.load_arxml(str(arxml_file), autosar)

            # Validate that data was loaded
            assert autosar.ar_packages is not None
            assert len(autosar.ar_packages) > 0

    def test_load_arxml_with_clear_iso_8859_1(self, reader: ARXMLReader) -> None:
        """Test load_arxml_with_clear with ISO-8859-1 file.

        Validates that the convenience method load_arxml_with_clear
        correctly handles ISO-8859-1 encoded files.

        Test ID: SWITS-INT-0305
        """
        arxml_file = Path("demos/arxml/Adc_Bswmd.arxml")
        if not arxml_file.exists():
            pytest.skip(f"File not found: {arxml_file}")

        # Load with clear
        autosar = reader.load_arxml_with_clear(str(arxml_file))

        # Validate that data was loaded
        assert autosar.ar_packages is not None
        assert len(autosar.ar_packages) > 0

        # Load again - should have fresh state
        autosar2 = reader.load_arxml_with_clear(str(arxml_file))
        assert autosar2 is autosar  # Same singleton instance
        assert len(autosar2.ar_packages) == len(autosar.ar_packages)