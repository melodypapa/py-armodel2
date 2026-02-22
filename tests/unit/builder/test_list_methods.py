"""Unit tests for Builder list-specific methods."""

import pytest

from armodel.models import (
    ImplementationDataType,
    ImplementationDataTypeBuilder,
    SwBaseType,
    SwBaseTypeBuilder,
)
from armodel.core import GlobalSettingsManager, BuilderValidationMode


class TestListMethods:
    """Test list-specific builder methods."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures."""
        self.settings = GlobalSettingsManager()
        self.settings.builder_validation = BuilderValidationMode.DISABLED

    def test_with_items_method(self):
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
        assert data_type.sub_elements[1].short_name == "Elem2"

    def test_with_items_empty_list(self):
        """Test with_items() method with empty list."""
        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_sub_elements([])
            .build()
        )

        assert len(data_type.sub_elements) == 0

    def test_add_item_method(self):
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

    def test_add_item_multiple_times(self):
        """Test adding multiple items with add_item() method."""
        elem1 = ImplementationDataTypeBuilder().with_short_name("Elem1").build()
        elem2 = ImplementationDataTypeBuilder().with_short_name("Elem2").build()
        elem3 = ImplementationDataTypeBuilder().with_short_name("Elem3").build()

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .add_sub_element(elem1)
            .add_sub_element(elem2)
            .add_sub_element(elem3)
            .build()
        )

        assert len(data_type.sub_elements) == 3

    def test_clear_items_method(self):
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

    def test_clear_items_then_add(self):
        """Test clearing items then adding new ones."""
        elem1 = ImplementationDataTypeBuilder().with_short_name("Elem1").build()
        elem2 = ImplementationDataTypeBuilder().with_short_name("Elem2").build()

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_sub_elements([elem1])
            .clear_sub_elements()
            .add_sub_element(elem2)
            .build()
        )

        assert len(data_type.sub_elements) == 1
        assert data_type.sub_elements[0].short_name == "Elem2"

    def test_with_items_overwrites_existing(self):
        """Test that with_items() overwrites existing list."""
        elem1 = ImplementationDataTypeBuilder().with_short_name("Elem1").build()
        elem2 = ImplementationDataTypeBuilder().with_short_name("Elem2").build()
        elem3 = ImplementationDataTypeBuilder().with_short_name("Elem3").build()

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_sub_elements([elem1, elem2])
            .with_sub_elements([elem3])
            .build()
        )

        assert len(data_type.sub_elements) == 1
        assert data_type.sub_elements[0].short_name == "Elem3"

    def test_multiple_list_attributes(self):
        """Test handling multiple list attributes."""
        elem1 = ImplementationDataTypeBuilder().with_short_name("Elem1").build()
        elem2 = ImplementationDataTypeBuilder().with_short_name("Elem2").build()

        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_sub_elements([elem1])
            .add_sub_element(elem2)
            .with_annotations([])  # Another list attribute
            .build()
        )

        assert len(data_type.sub_elements) == 2
        assert len(data_type.annotations) == 0

    def test_list_methods_return_builder(self):
        """Test that list methods return builder for chaining."""
        builder = ImplementationDataTypeBuilder()
        result = builder.with_sub_elements([])

        assert result is builder

    def test_with_items_none_handling(self):
        """Test that with_items() handles None gracefully."""
        # Should accept None and treat as empty list
        data_type = (
            ImplementationDataTypeBuilder()
            .with_short_name("MyType")
            .with_sub_elements(None)
            .build()
        )

        # Behavior depends on implementation - should handle gracefully
        assert data_type is not None