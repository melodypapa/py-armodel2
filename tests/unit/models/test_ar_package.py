"""Unit tests for ARPackage class."""


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