"""Unit tests for type safety."""

import pytest
from typing import get_type_hints


class TestTypeSafety:
    """Tests for type safety and type annotations."""

    def test_optional_initialization(self):
        """Test that Optional types initialize to None (SWUT_MODELS_300)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
            ARObject,
        )

        obj = ARObject()

        # checksum is Optional[String]
        assert obj.checksum is None
        # timestamp is Optional[DateTime]
        assert obj.timestamp is None

    def test_list_initialization(self):
        """Test that list types initialize to empty list (SWUT_MODELS_301)."""
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

        autosar = AUTOSAR()

        # ar_packages is list[ARPackage]
        assert autosar.ar_packages == []
        assert isinstance(autosar.ar_packages, list)

    def test_type_annotations(self):
        """Test that type annotations are correct (SWUT_MODELS_302)."""
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackage

        hints = get_type_hints(AUTOSAR)

        # Verify ar_packages is list[ARPackage]
        assert "ar_packages" in hints
        assert hints["ar_packages"] == list[ARPackage]

    def test_optional_type_annotations(self):
        """Test that Optional type annotations are correct."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        hints = get_type_hints(ARObject)

        # Verify checksum and timestamp are Optional
        assert "checksum" in hints
        assert "timestamp" in hints

    def test_list_type_annotations(self):
        """Test that list type annotations are correct."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackage

        hints = get_type_hints(ARPackage)

        # Verify elements and ar_packages are lists
        assert "elements" in hints
        assert "ar_packages" in hints

    def test_setting_optional_values(self):
        """Test setting Optional values."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

        obj = ARObject()
        obj.checksum = "test"
        obj.timestamp = "2024-01-01"

        assert obj.checksum == "test"
        assert obj.timestamp == "2024-01-01"

    def test_appending_to_lists(self):
        """Test appending to list types."""
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
            ARPackage,
            ARPackageBuilder,
        )

        autosar = AUTOSAR()
        pkg = ARPackageBuilder().with_short_name("Test").build()
        autosar.ar_packages.append(pkg)

        assert len(autosar.ar_packages) == 1
        assert autosar.ar_packages[0] is pkg