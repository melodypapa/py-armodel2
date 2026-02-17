"""Unit tests for AUTOSAR class."""

import pytest
import xml.etree.ElementTree as ET

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
        self.autosar = AUTOSAR()

    @pytest.mark.skip(reason="AUTOSAR is not implemented as a singleton")
    def test_autosar_singleton(self):
        """Test that AUTOSAR is a singleton (SWUT_MODELS_005)."""
        obj1 = AUTOSAR()
        obj2 = AUTOSAR()
        assert obj1 is obj2

    @pytest.mark.skip(reason="get_splitable_elements() method not yet implemented")
    def test_autosar_get_splitable_elements(self):
        """Test getting splitable elements (SWUT_MODELS_008)."""
        autosar = AUTOSAR()
        splitable = autosar.get_splitable_elements()
        assert isinstance(splitable, list)
        assert splitable is not None

    def test_autosar_package_management(self):
        """Test that AUTOSAR can manage packages (SWUT_MODELS_006)."""
        autosar = AUTOSAR()
        pkg = ARPackageBuilder().build()
        autosar.ar_packages.append(pkg)

        assert len(autosar.ar_packages) == 1
        assert isinstance(autosar.ar_packages[0], ARPackage)

    @pytest.mark.skip(reason="serialize() method not yet implemented in generated code")
    def test_autosar_serialize(self):
        """Test that AUTOSAR can serialize with packages (SWUT_MODELS_007)."""
        autosar = AUTOSAR()
        pkg = ARPackageBuilder().build()
        autosar.ar_packages.append(pkg)

        namespace = "http://autosar.org/schema/r4.0"
        element = autosar.serialize(namespace)

        assert element is not None
        assert isinstance(element, ET.Element)
        # Verify AR-PACKAGES element exists
        ar_packages_elements = element.findall(f"{{{namespace}}}AR-PACKAGES")
        assert len(ar_packages_elements) == 1

    @pytest.mark.skip(reason="serialize() method not yet implemented in generated code")
    def test_autosar_serialize_empty(self):
        """Test AUTOSAR serialization with no packages."""
        autosar = AUTOSAR()
        namespace = "http://autosar.org/schema/r4.0"
        element = autosar.serialize(namespace)

        assert element is not None
        assert element.tag == f"{{{namespace}}}AUTOSAR"

    def test_list_initialization(self):
        """Test that list types initialize to empty list (SWUT_MODELS_301)."""
        autosar = AUTOSAR()

        # ar_packages is list[ARPackage]
        assert autosar.ar_packages == []
        assert isinstance(autosar.ar_packages, list)

    @pytest.mark.skip(reason="AdminDataBuilder not yet fully implemented")
    def test_autosar_with_admin_data(self):
        """Test AUTOSAR with admin_data."""
        from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (
            AdminData,
            AdminDataBuilder,
        )

        autosar = AUTOSAR()
        admin_data = AdminDataBuilder().build()
        autosar.admin_data = admin_data

        assert autosar.admin_data is not None

    def test_autosar_arobject_inheritance(self):
        """Test that AUTOSAR inherits from ARObject (SWUT_MODELS_400)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        autosar = AUTOSAR()
        assert isinstance(autosar, ARObject)

    @pytest.mark.skip(reason="serialize() and deserialize() methods not yet implemented")
    def test_autosar_serialize_round_trip(self):
        """Test serialization/deserialization round trip."""
        autosar = AUTOSAR()
        pkg = ARPackageBuilder().build()
        autosar.ar_packages.append(pkg)

        namespace = "http://autosar.org/schema/r4.0"
        element = autosar.serialize(namespace)
        restored = AUTOSAR.deserialize(element)

        assert isinstance(restored, AUTOSAR)
        # Note: Full round-trip testing requires implementation details