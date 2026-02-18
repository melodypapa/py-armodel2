"""Unit tests for ARObject deserialization."""

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class TestARObject(ARObject):
    """Test ARObject subclass for deserialization tests."""

    # Class-level type annotations (required for get_type_hints)
    short_name: str
    category: str
    sw_data_def_props: str


class TestARObjectDeserialize:
    """Unit tests for ARObject deserialize functionality."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.test_xml_with_name_and_category = '''<TESTAROBJECT>
            <SHORT-NAME>test_name</SHORT-NAME>
            <CATEGORY>STANDARD</CATEGORY>
        </TESTAROBJECT>'''

        self.test_xml_with_sw_data_def_props = '''<TESTAROBJECT>
            <SW-DATA-DEF-PROPS>value</SW-DATA-DEF-PROPS>
        </TESTAROBJECT>'''

    def test_deserialize_from_xml(self):
        """Test deserializing ARObject from XML element."""
        elem = ET.fromstring(self.test_xml_with_name_and_category)
        obj = TestARObject.deserialize(elem)

        assert obj.short_name == "test_name"
        assert obj.category == "STANDARD"

    def test_deserialize_converts_names(self):
        """Test that deserialize converts XML tags to snake_case attribute names."""
        elem = ET.fromstring(self.test_xml_with_sw_data_def_props)
        obj = TestARObject.deserialize(elem)

        assert hasattr(obj, 'sw_data_def_props')
        assert obj.sw_data_def_props == "value"
