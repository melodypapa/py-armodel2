import pytest

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

    def test_ar_object_serialization_not_implemented(self):
        """Test that serialize raises NotImplementedError by default."""
        with pytest.raises(NotImplementedError):
            self.ar_object.serialize()
