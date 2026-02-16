import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class TestARObject:
    """Unit tests for ARObject base class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.ar_object = ARObject()

    def test_ar_object_creation(self):
        """Test that ARObject can be instantiated."""
        obj = ARObject()
        assert obj is not None

    def test_ar_object_serialize(self):
        """Test that ARObject can be serialized to XML."""
        namespace = "http://autosar.org/schema/r4.0"
        element = self.ar_object.serialize(namespace)
        assert element is not None
        assert isinstance(element, ET.Element)
        assert element.tag == f"{{{namespace}}}AROBJECT"

    def test_ar_object_deserialize(self):
        """Test that ARObject can be deserialized from XML."""
        namespace = "http://autosar.org/schema/r4.0"
        element = ET.Element(f"{{{namespace}}}AROBJECT")
        element.set("CHECKSUM", "test_checksum")
        obj = ARObject.deserialize(element)
        assert obj is not None
        assert isinstance(obj, ARObject)
        assert obj.checksum == "test_checksum"
