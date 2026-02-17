"""Unit tests for primitive types."""

import pytest


class TestPrimitiveTypes:
    """Tests for AUTOSAR primitive types."""

    def test_primitive_types_defined(self):
        """Test that all primitive types are defined (SWUT_MODELS_200)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            String,
            Integer,
            Float,
            Boolean,
        )

        # Verify types are defined
        assert String is not None
        assert Integer is not None
        assert Float is not None
        assert Boolean is not None

        # Verify they map to Python types
        assert String == str
        assert Integer == int
        assert Float == float
        assert Boolean == bool

    def test_string_primitive_usage(self):
        """Test that String primitive can be used (SWUT_MODELS_201)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
            ARObject,
        )
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String

        obj = ARObject()
        obj.checksum = String("test_checksum")

        assert obj.checksum == "test_checksum"
        assert isinstance(obj.checksum, str)

    @pytest.mark.skip(reason="Builder methods with_with_category and with_base_type_size not yet implemented")
    def test_integer_primitive_usage(self):
        """Test that Integer primitive can be used."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.PrimitiveTypes.sw_base_type import (
            SwBaseType,
            SwBaseTypeBuilder,
        )

        obj = SwBaseTypeBuilder().with_short_name("TestType").with_base_type_size(
            "32"
        ).build()

        assert obj.base_type_size == "32"

    @pytest.mark.skip(reason="Builder method with_short_name not yet implemented")
    def test_boolean_primitive_usage(self):
        """Test that Boolean primitive can be used."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.PrimitiveTypes.boolean_type import (
            BooleanType,
            BooleanTypeBuilder,
        )

        obj = BooleanTypeBuilder().with_short_name("TestBool").build()

        assert obj is not None
        assert isinstance(obj, BooleanType)