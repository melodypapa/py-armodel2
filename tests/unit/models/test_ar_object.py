"""Unit tests for ARObject base class."""

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
    ARObject,
)


class TestARObject:
    """Unit tests for ARObject base class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.ar_object = ARObject()

    def test_ar_object_instantiation(self):
        """Test that ARObject can be instantiated (SWUT_MODELS_001)."""
        obj = ARObject()
        assert obj is not None
        assert isinstance(obj, ARObject)

    def test_ar_object_creation(self):
        """Test that ARObject can be instantiated."""
        obj = ARObject()
        assert obj is not None

    def test_ar_object_serialize(self):
        """Test that ARObject can be serialized to XML (SWUT_MODELS_002)."""
        obj = ARObject()
        obj.checksum = "test_checksum"
        namespace = "http://autosar.org/schema/r4.0"

        element = obj.serialize(namespace)

        assert element is not None
        assert isinstance(element, ET.Element)
        assert element.tag == "AROBJECT"
        # checksum is serialized as a child element, not attribute
        checksum_elem = element.find("CHECKSUM")
        assert checksum_elem is not None
        assert checksum_elem.text == "test_checksum"

    def test_ar_object_serialize_with_timestamp(self):
        """Test ARObject serialization with both attributes."""
        obj = ARObject()
        obj.checksum = "test_checksum"
        obj.timestamp = "2024-01-01T00:00:00Z"
        namespace = "http://autosar.org/schema/r4.0"

        element = obj.serialize(namespace)

        checksum_elem = element.find("CHECKSUM")
        assert checksum_elem is not None
        assert checksum_elem.text == "test_checksum"

        timestamp_elem = element.find("TIMESTAMP")
        assert timestamp_elem is not None
        assert timestamp_elem.text == "2024-01-01T00:00:00Z"

    def test_ar_object_deserialize(self):
        """Test that ARObject can be deserialized from XML (SWUT_MODELS_003)."""
        element = ET.Element("AROBJECT")
        checksum_elem = ET.Element("CHECKSUM")
        checksum_elem.text = "test_checksum"
        element.append(checksum_elem)
        obj = ARObject.deserialize(element)
        assert obj is not None
        assert isinstance(obj, ARObject)
        assert obj.checksum == "test_checksum"

    def test_ar_object_deserialize_with_timestamp(self):
        """Test ARObject deserialization with both attributes."""
        element = ET.Element("AROBJECT")
        checksum_elem = ET.Element("CHECKSUM")
        checksum_elem.text = "test_checksum"
        timestamp_elem = ET.Element("TIMESTAMP")
        timestamp_elem.text = "2024-01-01T00:00:00Z"
        element.append(checksum_elem)
        element.append(timestamp_elem)
        obj = ARObject.deserialize(element)

        assert obj.checksum == "test_checksum"
        assert obj.timestamp == "2024-01-01T00:00:00Z"

    def test_member_to_xml_tag(self):
        """Test the NameConverter for XML tag conversion."""
        from armodel.serialization.name_converter import NameConverter
        assert NameConverter.to_xml_tag("short_name") == "SHORT-NAME"
        assert NameConverter.to_xml_tag("category") == "CATEGORY"
        assert NameConverter.to_xml_tag("ar_packages") == "AR-PACKAGES"

    def test_optional_initialization(self):
        """Test that Optional types initialize to None (SWUT_MODELS_300)."""
        obj = ARObject()

        # checksum is Optional[String]
        assert obj.checksum is None
        # timestamp is Optional[DateTime]
        assert obj.timestamp is None

    def test_serialize_with_different_namespaces(self):
        """Test serialization with different schema versions."""
        obj = ARObject()
        obj.checksum = "test_checksum"

        # Test with 00046 namespace
        namespace_46 = "http://autosar.org/schema/r4.0"
        element_46 = obj.serialize(namespace_46)
        assert element_46.tag == "AROBJECT"

        # Test with 00052 namespace
        namespace_52 = "http://autosar.org/schema/r5.0"
        element_52 = obj.serialize(namespace_52)
        assert element_52.tag == "AROBJECT"

    def test_deserialize_with_different_namespaces(self):
        """Test deserialization with different schema versions."""
        for namespace in [
            "http://autosar.org/schema/r4.0",
            "http://autosar.org/schema/r5.0",
            "http://autosar.org/3.0.4",
        ]:
            element = ET.Element("AROBJECT")
            checksum_elem = ET.Element("CHECKSUM")
            checksum_elem.text = "test_checksum"
            element.append(checksum_elem)
            obj = ARObject.deserialize(element)
            assert obj.checksum == "test_checksum"

    def test_invalid_xml_deserialization(self):
        """Test that invalid XML is handled gracefully (SWUT_MODELS_500)."""
        element = ET.Element("AROBJECT")

        # Element with invalid child - should be ignored since it's not in type hints
        invalid_elem = ET.Element("INVALID_ATTR")
        invalid_elem.text = "value"
        element.append(invalid_elem)

        obj = ARObject.deserialize(element)
        assert obj is not None
        assert isinstance(obj, ARObject)