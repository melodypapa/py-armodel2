"""Unit tests for AUTOSAR class."""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import (
    AUTOSAR,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
    ARPackage,
    ARPackageBuilder,
)


class TestAUTOSAR:
    """Unit tests for AUTOSAR class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        AUTOSAR.reset()  # Reset singleton before each test
        self.autosar = AUTOSAR()

    def test_autosar_package_management(self):
        """Test that AUTOSAR can manage packages (SWUT_MODELS_006)."""
        autosar = AUTOSAR()
        pkg = ARPackageBuilder().build()
        autosar.ar_packages.append(pkg)

        assert len(autosar.ar_packages) == 1
        assert isinstance(autosar.ar_packages[0], ARPackage)

    def test_list_initialization(self):
        """Test that list types initialize to empty list (SWUT_MODELS_301)."""
        autosar = AUTOSAR()

        # ar_packages is list[ARPackage]
        assert autosar.ar_packages == []
        assert isinstance(autosar.ar_packages, list)

    def test_autosar_arobject_inheritance(self):
        """Test that AUTOSAR inherits from ARObject (SWUT_MODELS_400)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        autosar = AUTOSAR()
        assert isinstance(autosar, ARObject)

    def test_singleton_pattern(self):
        """Test that AUTOSAR implements singleton pattern."""
        autosar1 = AUTOSAR()
        autosar2 = AUTOSAR()

        assert autosar1 is autosar2  # Same instance

    def test_clear_method(self):
        """Test that clear() resets instance state."""
        autosar = AUTOSAR()
        pkg = ARPackageBuilder().build()
        autosar.ar_packages.append(pkg)
        autosar.schema_location = "test.xsd"

        # Verify state is set
        assert len(autosar.ar_packages) == 1
        assert autosar.schema_location == "test.xsd"

        # Clear state
        autosar.clear()

        # Verify state is cleared
        assert len(autosar.ar_packages) == 0
        assert autosar.schema_location is None

    def test_reset_method(self):
        """Test that reset() creates new singleton instance."""
        autosar1 = AUTOSAR()
        autosar1.ar_packages.append(ARPackageBuilder().build())

        AUTOSAR.reset()

        autosar2 = AUTOSAR()

        # New instance should be created
        assert autosar1 is not autosar2
        # New instance should have empty state
        assert len(autosar2.ar_packages) == 0