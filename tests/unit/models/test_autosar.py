import pytest

from armodel.models.M2.AUTOSARTemplates.autosar import AUTOSAR


class TestAUTOSAR:
    """Unit tests for AUTOSAR class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.autosar = AUTOSAR()

    def test_autosar_singleton(self):
        """Test that AUTOSAR is a singleton."""
        obj1 = AUTOSAR()
        obj2 = AUTOSAR()
        assert obj1 is obj2

    def test_autosar_get_splitable_elements(self):
        """Test getting splitable elements."""
        splitable = self.autosar.get_splitable_elements()
        assert isinstance(splitable, list)
