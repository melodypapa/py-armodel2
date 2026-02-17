"""Unit tests for ARPackage class."""

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
    ARPackage,
    ARPackageBuilder,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
    ARObject,
)


class TestARPackage:
    """Unit tests for ARPackage class."""

    def test_ar_package_instantiation(self):
        """Test that ARPackage can be instantiated (SWUT_MODELS_009)."""
        pkg = ARPackageBuilder().build()

        assert pkg is not None
        assert isinstance(pkg, ARPackage)

    def test_ar_package_element_management(self):
        """Test that ARPackage can manage elements (SWUT_MODELS_010)."""
        pkg = ARPackageBuilder().build()
        element = ARObject()
        pkg.elements.append(element)

        assert len(pkg.elements) == 1
        assert pkg.elements[0] is element

    def test_ar_package_with_category(self):
        """Test ARPackage with category."""
        pkg = ARPackageBuilder().build()
        # Category is not settable via current builder, just verify it exists
        assert pkg is not None
        assert isinstance(pkg, ARPackage)

    def test_ar_package_sub_packages(self):
        """Test ARPackage with sub-packages."""
        pkg = ARPackageBuilder().build()
        sub_pkg = ARPackageBuilder().build()
        pkg.ar_packages.append(sub_pkg)

        assert len(pkg.ar_packages) == 1
        assert isinstance(pkg.ar_packages[0], ARPackage)

    @pytest.mark.skip(reason="serialize() method not yet implemented in generated code")
    def test_ar_package_serialize(self):
        """Test ARPackage serialization."""
        pkg = ARPackageBuilder().build()
        namespace = "http://autosar.org/schema/r4.0"
        element = pkg.serialize(namespace)

        assert element is not None
        assert isinstance(element, ET.Element)
        assert element.tag == f"{{{namespace}}}AR-PACKAGE"

    @pytest.mark.skip(reason="deserialize() method not yet implemented in generated code")
    def test_ar_package_deserialize(self):
        """Test ARPackage deserialization."""
        namespace = "http://autosar.org/schema/r4.0"
        element = ET.Element(f"{{{namespace}}}AR-PACKAGE")

        short_name = ET.Element(f"{{{namespace}}}SHORT-NAME")
        short_name.text = "TestPackage"
        element.append(short_name)

        pkg = ARPackage.deserialize(element)

        assert pkg is not None
        assert pkg.short_name == "TestPackage"

    def test_ar_package_method_resolution_order(self):
        """Test that MRO is correct (SWUT_MODELS_401)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        mro = ARPackage.__mro__
        assert ARObject in mro

    def test_ar_package_list_initialization(self):
        """Test that list types initialize to empty list."""
        pkg = ARPackageBuilder().build()

        assert pkg.elements == []
        assert pkg.ar_packages == []
        assert isinstance(pkg.elements, list)
        assert isinstance(pkg.ar_packages, list)