"""Unit tests for error handling."""

import pytest
import xml.etree.ElementTree as ET


class TestErrorHandling:
    """Tests for error handling and edge cases."""

    def test_invalid_xml_deserialization(self):
        """Test that invalid XML is handled gracefully (SWUT_MODELS_500)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        namespace = "http://autosar.org/schema/r4.0"
        element = ET.Element(f"{{{namespace}}}AROBJECT")

        # Element with invalid attribute - should be ignored
        element.set("INVALID_ATTR", "value")

        obj = ARObject.deserialize(element)
        assert obj is not None
        assert isinstance(obj, ARObject)

    def test_missing_required_attribute(self):
        """Test behavior when required attribute is missing (SWUT_MODELS_501)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable.referrable import Referrable

        namespace = "http://autosar.org/schema/r4.0"
        element = ET.Element(f"{{{namespace}}}REFERRABLE")

        # short_name is required (multiplicity 1)
        # XML is missing SHORT-NAME element

        # Should create object with None or empty value
        obj = Referrable.deserialize(element)
        assert obj is not None
        # short_name may be None or empty string

    def test_empty_xml_element(self):
        """Test deserialization of empty XML element."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        namespace = "http://autosar.org/schema/r4.0"
        element = ET.Element(f"{{{namespace}}}AROBJECT")

        obj = ARObject.deserialize(element)
        assert obj is not None
        assert obj.checksum is None
        assert obj.timestamp is None

    def test_malformed_xml_tag(self):
        """Test handling of malformed XML tag."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        namespace = "http://autosar.org/schema/r4.0"
        # Create element with slightly different tag
        element = ET.Element(f"{{{namespace}}}AR-OBJECT")

        # Should still attempt to deserialize
        obj = ARObject.deserialize(element)
        assert obj is not None

    def test_none_namespace(self):
        """Test serialization with None namespace."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        obj = ARObject()
        # Should handle None namespace gracefully
        try:
            element = obj.serialize(None)
            # May raise error or return element without namespace
            assert element is not None
        except (AttributeError, TypeError):
            # Expected behavior - namespace is required
            pass

    def test_extra_child_elements(self):
        """Test handling of extra child elements."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        namespace = "http://autosar.org/schema/r4.0"
        element = ET.Element(f"{{{namespace}}}AROBJECT")

        # Add extra child element that's not defined
        extra = ET.Element(f"{{{namespace}}}EXTRA-ELEMENT")
        extra.text = "extra data"
        element.append(extra)

        obj = ARObject.deserialize(element)
        assert obj is not None
        # Extra element should be ignored

    def test_serialize_with_none_values(self):
        """Test serialization when attributes are None."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        obj = ARObject()
        # checksum and timestamp are None by default
        namespace = "http://autosar.org/schema/r4.0"
        element = obj.serialize(namespace)

        assert element is not None
        # Optional None values should not be serialized
        assert element.get("CHECKSUM") is None
        assert element.get("TIMESTAMP") is None