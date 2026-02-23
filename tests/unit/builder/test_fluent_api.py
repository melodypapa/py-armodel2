"""Unit tests for Builder fluent API."""

import pytest

from armodel.models import (
    ImplementationDataTypeBuilder,
)
from armodel.core import GlobalSettingsManager, BuilderValidationMode


class TestFluentAPI:
    """Test fluent API method chaining."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.settings = GlobalSettingsManager()
        self.original_mode = self.settings.builder_validation
        self.settings.builder_validation = BuilderValidationMode.DISABLED

    def teardown_method(self):
        """Reset settings after tests."""
        self.settings.builder_validation = self.original_mode

    def test_basic_fluent_chaining(self):
        """Test basic method chaining."""
        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_category("VALUE")
            .with_type_emitter("BSW")
            .build()
        )

        assert data_type.short_name == "MyType"
        assert data_type.category == "VALUE"
        assert data_type.type_emitter == "BSW"

    def test_inherited_attributes_fluent_chaining(self):
        """Test fluent chaining with inherited attributes."""
        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")  # Inherited from Referrable
            .with_long_name("My Long Name")  # Inherited from MultilanguageReferrable
            .with_category("VALUE")
            .build()
        )

        assert data_type.short_name == "MyType"
        assert data_type.long_name is not None

    def test_optional_field_with_none(self):
        """Test optional field handling with None."""
        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_sw_data_def_props(None)  # Optional field
            .build()
        )

        assert data_type.sw_data_def_props is None

    def test_list_with_items_method(self):
        """Test with_items() method for list attributes."""
        elem1 = ImplementationDataTypeBuilder().with_short_name("Elem1").build()
        elem2 = ImplementationDataTypeBuilder().with_short_name("Elem2").build()

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_sub_elements([elem1, elem2])
            .build()
        )

        assert len(data_type.sub_elements) == 2
        assert data_type.sub_elements[0].short_name == "Elem1"

    def test_list_add_item_method(self):
        """Test add_item() method for list attributes."""
        elem1 = ImplementationDataTypeBuilder().with_short_name("Elem1").build()
        elem2 = ImplementationDataTypeBuilder().with_short_name("Elem2").build()

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_sub_elements([elem1])
            .add_sub_element(elem2)
            .build()
        )

        assert len(data_type.sub_elements) == 2

    def test_list_clear_items_method(self):
        """Test clear_items() method for list attributes."""
        elem1 = ImplementationDataTypeBuilder().with_short_name("Elem1").build()

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_sub_elements([elem1])
            .clear_sub_elements()
            .build()
        )

        assert len(data_type.sub_elements) == 0

    def test_multiple_chaining_calls(self):
        """Test multiple fluent method calls in sequence."""
        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_category("VALUE")
            .with_type_emitter("BSW")
            .with_symbol_props(None)
            .with_dynamic_array_size_profile("FixedSize")
            .build()
        )

        assert data_type.short_name == "MyType"
        assert data_type.category == "VALUE"
        assert data_type.type_emitter == "BSW"
        assert data_type.dynamic_array_size_profile == "FixedSize"

    def test_builder_returns_self(self):
        """Test that builder methods return self for chaining."""
        builder = ImplementationDataTypeBuilder()
        result = builder.with_short_name("MyType")

        assert result is builder

    def test_multiple_builds_from_different_builders(self):
        """Test that builder can create multiple instances from different builders."""
        # Builder pattern: create a new builder for each instance
        instance1 = (ImplementationDataTypeBuilder()
                     .with_short_name("Type1")
                     .with_category("VALUE")
                     .build())
        instance2 = (ImplementationDataTypeBuilder()
                     .with_short_name("Type2")
                     .with_category("TYPE_REFERENCE")
                     .build())

        assert instance1.short_name == "Type1"
        assert instance2.short_name == "Type2"
        assert instance1 != instance2

    def test_builder_mutable_object(self):
        """Test that builder modifies same object until reset."""
        builder = ImplementationDataTypeBuilder()

        # Set initial values
        builder.with_short_name("Type1").with_category("VALUE")
        instance1 = builder.build()

        # Modify values (affects same object)
        builder.with_short_name("Type2").with_category("TYPE_REFERENCE")
        instance2 = builder.build()

        # Both point to same object because builder reuses self._obj
        assert instance1 is instance2
        assert instance1.short_name == "Type2"  # Overwritten by second build