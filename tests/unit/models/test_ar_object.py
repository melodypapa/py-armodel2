"""Unit tests for ARObject base class."""

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
    ARObject,
)
from armodel.serialization.metadata import XMLMember


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

    @pytest.mark.skip(reason="serialize() method not yet implemented in generated code")
    def test_ar_object_serialize(self):
        """Test that ARObject can be serialized to XML (SWUT_MODELS_002)."""
        obj = ARObject()
        obj.checksum = "test_checksum"
        namespace = "http://autosar.org/schema/r4.0"

        element = obj.serialize(namespace)

        assert element is not None
        assert isinstance(element, ET.Element)
        assert element.tag == f"{{{namespace}}}AROBJECT"
        assert element.get("CHECKSUM") == "test_checksum"

    @pytest.mark.skip(reason="serialize() method not yet implemented in generated code")
    def test_ar_object_serialize_with_timestamp(self):
        """Test ARObject serialization with both attributes."""
        obj = ARObject()
        obj.checksum = "test_checksum"
        obj.timestamp = "2024-01-01T00:00:00Z"
        namespace = "http://autosar.org/schema/r4.0"

        element = obj.serialize(namespace)

        assert element.get("CHECKSUM") == "test_checksum"
        assert element.get("TIMESTAMP") == "2024-01-01T00:00:00Z"

    @pytest.mark.skip(reason="deserialize() method not yet implemented in generated code")
    def test_ar_object_deserialize(self):
        """Test that ARObject can be deserialized from XML (SWUT_MODELS_003)."""
        namespace = "http://autosar.org/schema/r4.0"
        element = ET.Element(f"{{{namespace}}}AROBJECT")
        element.set("CHECKSUM", "test_checksum")
        obj = ARObject.deserialize(element)
        assert obj is not None
        assert isinstance(obj, ARObject)
        assert obj.checksum == "test_checksum"

    @pytest.mark.skip(reason="deserialize() method not yet implemented in generated code")
    def test_ar_object_deserialize_with_timestamp(self):
        """Test ARObject deserialization with both attributes."""
        namespace = "http://autosar.org/schema/r4.0"
        element = ET.Element(f"{{{namespace}}}AROBJECT")
        element.set("CHECKSUM", "test_checksum")
        element.set("TIMESTAMP", "2024-01-01T00:00:00Z")
        obj = ARObject.deserialize(element)

        assert obj.checksum == "test_checksum"
        assert obj.timestamp == "2024-01-01T00:00:00Z"

    def test_ar_object_xml_members(self):
        """Test that ARObject has correct XMLMember metadata (SWUT_MODELS_004)."""
        assert hasattr(ARObject, "_xml_members")
        assert isinstance(ARObject._xml_members, dict)

        # Verify checksum member
        assert "checksum" in ARObject._xml_members
        checksum_member = ARObject._xml_members["checksum"]
        assert isinstance(checksum_member, XMLMember)
        assert checksum_member.multiplicity == "0..1"
        assert checksum_member.is_attribute is True

        # Verify timestamp member
        assert "timestamp" in ARObject._xml_members
        timestamp_member = ARObject._xml_members["timestamp"]
        assert isinstance(timestamp_member, XMLMember)
        assert timestamp_member.multiplicity == "0..1"
        assert timestamp_member.is_attribute is True

    def test_member_to_xml_tag(self):
        """Test the _member_to_xml_tag static method."""
        assert ARObject._member_to_xml_tag("short_name") == "SHORT-NAME"
        assert ARObject._member_to_xml_tag("category") == "CATEGORY"
        assert ARObject._member_to_xml_tag("ar_packages") == "AR-PACKAGES"

    def test_optional_initialization(self):
        """Test that Optional types initialize to None (SWUT_MODELS_300)."""
        obj = ARObject()

        # checksum is Optional[String]
        assert obj.checksum is None
        # timestamp is Optional[DateTime]
        assert obj.timestamp is None

    @pytest.mark.skip(reason="serialize() method not yet implemented in generated code")
    def test_serialize_with_different_namespaces(self):
        """Test serialization with different schema versions."""
        obj = ARObject()
        obj.checksum = "test_checksum"

        # Test with 00046 namespace
        namespace_46 = "http://autosar.org/schema/r4.0"
        element_46 = obj.serialize(namespace_46)
        assert element_46.tag == f"{{{namespace_46}}}AROBJECT"

        # Test with 00052 namespace
        namespace_52 = "http://autosar.org/schema/r5.0"
        element_52 = obj.serialize(namespace_52)
        assert element_52.tag == f"{{{namespace_52}}}AROBJECT"

    @pytest.mark.skip(reason="deserialize() method not yet implemented in generated code")
    def test_deserialize_with_different_namespaces(self):
        """Test deserialization with different schema versions."""
        for namespace in [
            "http://autosar.org/schema/r4.0",
            "http://autosar.org/schema/r5.0",
            "http://autosar.org/3.0.4",
        ]:
            element = ET.Element(f"{{{namespace}}}AROBJECT")
            element.set("CHECKSUM", "test_checksum")
            obj = ARObject.deserialize(element)
            assert obj.checksum == "test_checksum"

    @pytest.mark.skip(reason="deserialize() method not yet implemented in generated code")
    def test_invalid_xml_deserialization(self):
        """Test that invalid XML is handled gracefully (SWUT_MODELS_500)."""
        namespace = "http://autosar.org/schema/r4.0"
        element = ET.Element(f"{{{namespace}}}AROBJECT")

        # Element with invalid attribute - should be ignored
        element.set("INVALID_ATTR", "value")

        obj = ARObject.deserialize(element)
        assert obj is not None
        assert isinstance(obj, ARObject)