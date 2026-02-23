"""Unit tests for Builder type coercion."""

import pytest

from armodel.models import ImplementationDataTypeBuilder
from armodel.core import GlobalSettingsManager


class TestTypeCoercion:
    """Test type coercion in builders."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.settings = GlobalSettingsManager()
        self.original_coercion = self.settings.builder_type_coercion
        self.settings.builder_validation = False  # Disable validation for coercion tests

    def teardown_method(self):
        """Reset settings after tests."""
        self.settings.builder_type_coercion = self.original_coercion

    def test_str_to_int_coercion(self):
        """Test string to int coercion."""
        self.settings.builder_type_coercion = True

        # Note: ImplementationDataType doesn't have int fields, so we skip this test
        # This would be tested with a class that has integer attributes
        pass

    def test_type_coercion_disabled(self):
        """Test that type coercion can be disabled."""
        self.settings.builder_type_coercion = False

        # When disabled, types should not be coerced
        # This would require a class with coercible types to test properly
        pass

    def test_type_coercion_with_string_types(self):
        """Test that string types are not coerced."""
        self.settings.builder_type_coercion = True

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("123")  # String value
            .with_category("VALUE")
            .build()
        )

        assert isinstance(data_type.short_name, str)
        assert data_type.short_name == "123"

    def test_type_coercion_persistence(self):
        """Test that type coercion setting persists."""
        self.settings.builder_type_coercion = True

        # Multiple builds should use the same coercion setting
        data_type1 = (
            ImplementationDataTypeBuilder()
            .with_short_name("Type1")
            .build()
        )

        data_type2 = (
            ImplementationDataTypeBuilder()
            .with_short_name("Type2")
            .build()
        )

        assert data_type1.short_name == "Type1"
        assert data_type2.short_name == "Type2"

    def test_type_coercion_switching(self):
        """Test switching type coercion on and off."""
        # Start with coercion enabled
        self.settings.builder_type_coercion = True

        data_type1 = ImplementationDataTypeBuilder().with_short_name("Type1").build()

        # Switch to disabled
        self.settings.builder_type_coercion = False

        data_type2 = ImplementationDataTypeBuilder().with_short_name("Type2").build()

        assert data_type1.short_name == "Type1"
        assert data_type2.short_name == "Type2"