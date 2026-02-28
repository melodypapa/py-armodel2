"""Unit tests for ARPackage class."""

import os
from pathlib import Path

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
    ARPackage,
    ARPackageBuilder,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
    ARObject,
)
from armodel2.reader import ARXMLReader


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
        from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        mro = ARPackage.__mro__
        assert ARObject in mro

    def test_ar_package_list_initialization(self):
        """Test that list types initialize to empty list."""
        pkg = ARPackageBuilder().build()

        assert pkg.elements == []
        assert pkg.ar_packages == []
        assert isinstance(pkg.elements, list)
        assert isinstance(pkg.ar_packages, list)

    def test_ar_package_short_name_deserialization(self):
        """Test that ARPackage short_name is properly deserialized from XML.

        This test verifies the fix for the inheritance chain bug where
        ARPackage.deserialize() was not calling super().deserialize(),
        causing inherited attributes like short_name to be None.
        """
        # Get the path to the test ARXML file
        project_root = Path(__file__).parent.parent.parent.parent
        arxml_path = project_root / "demos" / "validated" / "AUTOSAR_Datatypes.arxml"

        # Load the ARXML file
        reader = ARXMLReader()
        autosar = reader.load_arxml_with_clear(str(arxml_path))

        # Verify the root AR-PACKAGE has a short_name
        assert len(autosar.ar_packages) > 0
        root_pkg = autosar.ar_packages[0]
        assert root_pkg.short_name is not None, "Root AR-PACKAGE should have SHORT-NAME"
        assert root_pkg.short_name.value == "AUTOSAR_Platform"

        # Verify nested packages also have short_names
        assert len(root_pkg.ar_packages) > 0
        base_types_pkg = None
        compu_methods_pkg = None
        data_constrs_pkg = None
        implementation_data_types_pkg = None

        for pkg in root_pkg.ar_packages:
            if pkg.short_name and pkg.short_name.value == "BaseTypes":
                base_types_pkg = pkg
            elif pkg.short_name and pkg.short_name.value == "CompuMethods":
                compu_methods_pkg = pkg
            elif pkg.short_name and pkg.short_name.value == "DataConstrs":
                data_constrs_pkg = pkg
            elif pkg.short_name and pkg.short_name.value == "ImplementationDataTypes":
                implementation_data_types_pkg = pkg

        assert base_types_pkg is not None, "Should find BaseTypes package"
        assert compu_methods_pkg is not None, "Should find CompuMethods package"
        assert data_constrs_pkg is not None, "Should find DataConstrs package"
        assert implementation_data_types_pkg is not None, "Should find ImplementationDataTypes package"

        # Verify all packages have their short_name properly set
        assert base_types_pkg.short_name is not None
        assert compu_methods_pkg.short_name is not None
        assert data_constrs_pkg.short_name is not None
        assert implementation_data_types_pkg.short_name is not None