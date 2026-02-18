"""Unit tests for ARObject serialization."""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String


class TestARObjectForSerialize(ARObject):
    """Test ARObject subclass for serialization tests."""

    def __init__(self):
        super().__init__()
        self.short_name: String = "test_name"
        self.category: str = "STANDARD"


class TestARObjectSerialize:
    """Unit tests for ARObject serialize functionality."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.test_obj = TestARObjectForSerialize()

    def test_serialize_creates_element(self):
        """Test that serialize creates XML element with correct structure."""
        elem = self.test_obj.serialize()

        assert elem.tag == "TEST-A-R-OBJECT-FOR-SERIALIZE"
        assert elem.find("SHORT-NAME") is not None
        assert elem.find("SHORT-NAME").text == "test_name"

    def test_serialize_converts_names(self):
        """Test that serialize converts snake_case to UPPER-CASE-WITH-HYPHENS."""
        elem = self.test_obj.serialize()

        # Verify snake_case → UPPER-CASE conversion
        assert elem.find("SHORT-NAME") is not None
        assert elem.find("CATEGORY") is not None
