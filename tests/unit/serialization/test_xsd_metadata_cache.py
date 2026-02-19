"""
Unit tests for XSD Metadata Cache Manager.
"""

import pytest

from armodel.serialization.xsd_metadata_cache import XSDBasedSchemaManager


class TestXSDBasedSchemaManager:
    """Unit tests for XSDBasedSchemaManager class."""

    @pytest.fixture
    def manager(self):
        """Get singleton instance of XSDBasedSchemaManager."""
        manager = XSDBasedSchemaManager()
        manager.clear_cache()  # Start with clean cache
        return manager

    def test_singleton_pattern(self, manager):
        """Test that manager follows singleton pattern."""
        manager2 = XSDBasedSchemaManager()
        assert manager is manager2

    def test_get_metadata(self, manager):
        """Test getting metadata for schema version."""
        metadata = manager.get_metadata("00046")

        assert metadata is not None
        assert metadata["version"] == "00046"
        assert "complex_types" in metadata
        assert "simple_types" in metadata
        assert "inheritance" in metadata
        assert "indexes" in metadata

    def test_get_metadata_caching(self, manager):
        """Test that metadata is cached after first load."""
        # First load
        metadata1 = manager.get_metadata("00046")
        assert manager.is_loaded("00046") is True

        # Second load should use cache
        metadata2 = manager.get_metadata("00046")
        assert metadata1 is metadata2  # Same object reference

    def test_get_type_info(self, manager):
        """Test getting type information."""
        type_info = manager.get_type_info("AUTOSAR", "00046")

        assert type_info is not None
        assert "base_type" in type_info
        assert "abstract" in type_info
        assert "elements" in type_info
        assert "attributes" in type_info

    def test_get_nonexistent_type_info(self, manager):
        """Test getting info for non-existent type returns None."""
        type_info = manager.get_type_info("NONEXISTENT-TYPE", "00046")
        assert type_info is None

    def test_get_elements_for_type(self, manager):
        """Test getting elements for a type."""
        elements = manager.get_elements_for_type("AUTOSAR", "00046")

        assert isinstance(elements, list)
        for elem in elements:
            assert "name" in elem
            assert "type" in elem
            assert "min_occurs" in elem
            assert "max_occurs" in elem
            assert "required" in elem

    def test_get_elements_for_ar_package(self, manager):
        """Test getting elements for AR-PACKAGE type."""
        elements = manager.get_elements_for_type("AR-PACKAGE", "00046")

        # Should include SHORT-NAME element
        short_name_found = False
        for elem in elements:
            if elem["name"] == "SHORT-NAME":
                short_name_found = True
                assert elem["required"] is True
                assert elem["min_occurs"] == 1
                assert elem["max_occurs"] == 1
                break
        assert short_name_found, "SHORT-NAME not found in AR-PACKAGE elements"

    def test_get_attributes_for_type(self, manager):
        """Test getting attributes for a type."""
        attrs = manager.get_attributes_for_type("AUTOSAR", "00046")

        assert isinstance(attrs, list)
        for attr in attrs:
            assert "name" in attr
            assert "type" in attr
            assert "required" in attr

    def test_get_simple_type_info(self, manager):
        """Test getting simple type information."""
        # Find a simple type with enum values
        metadata = manager.get_metadata("00046")
        simple_types = metadata["simple_types"]

        # Find an enum type
        enum_type = None
        for name, info in simple_types.items():
            if info.get("enum_values"):
                enum_type = name
                break

        if enum_type:
            type_info = manager.get_simple_type_info(enum_type, "00046")
            assert type_info is not None
            assert "enum_values" in type_info
            assert len(type_info["enum_values"]) > 0

    def test_get_element_types(self, manager):
        """Test getting types that contain a specific element."""
        types = manager.get_element_types("SHORT-NAME", "00046")

        assert isinstance(types, list)
        assert len(types) > 0

        # AR-PACKAGE should have SHORT-NAME
        assert "AR-PACKAGE" in types

    def test_get_inheritance_chain(self, manager):
        """Test getting inheritance chain for a type."""
        chain = manager.get_inheritance_chain("AUTOSAR", "00046")

        assert isinstance(chain, list)
        assert len(chain) >= 1
        assert "AUTOSAR" in chain

    def test_clear_cache(self, manager):
        """Test clearing the cache."""
        # Load metadata
        manager.get_metadata("00046")
        assert manager.is_loaded("00046") is True

        # Clear cache
        manager.clear_cache()
        assert manager.is_loaded("00046") is False

    def test_invalid_version_raises_error(self, manager):
        """Test that requesting non-existent version raises error."""
        with pytest.raises(FileNotFoundError):
            manager.get_metadata("99999")

    def test_validate_value_enum(self, manager):
        """Test value validation for enum types."""
        # Find an enum type
        metadata = manager.get_metadata("00046")
        simple_types = metadata["simple_types"]

        enum_type = None
        enum_values = []
        for name, info in simple_types.items():
            if info.get("enum_values"):
                enum_type = name
                enum_values = info["enum_values"]
                break

        if enum_type and enum_values:
            # Test valid value
            valid = manager.validate_value(enum_values[0], enum_type, "00046")
            assert valid is True

            # Test invalid value
            invalid = manager.validate_value("INVALID_VALUE", enum_type, "00046")
            assert invalid is False

    def test_validate_value_pattern(self, manager):
        """Test value validation for pattern types."""
        # Find a type with pattern constraint
        metadata = manager.get_metadata("00046")
        simple_types = metadata["simple_types"]

        pattern_type = None
        pattern = None
        for name, info in simple_types.items():
            if info.get("pattern"):
                pattern_type = name
                pattern = info["pattern"]
                break

        if pattern_type and pattern:
            # For IDENTIFIER pattern, test valid identifier
            if "IDENTIFIER" in pattern_type:
                valid = manager.validate_value("ValidName_123", pattern_type, "00046")
                assert valid is True

                invalid = manager.validate_value("123Invalid", pattern_type, "00046")
                assert invalid is False

    def test_validate_value_no_constraints(self, manager):
        """Test that validation passes for types without constraints."""
        # Simple string type with no constraints
        valid = manager.validate_value("any_value", "AR:STRING", "00046")
        assert valid is True

    def test_get_elements_for_nonexistent_type(self, manager):
        """Test getting elements for non-existent type returns empty list."""
        elements = manager.get_elements_for_type("NONEXISTENT-TYPE", "00046")
        assert elements == []

    def test_get_attributes_for_nonexistent_type(self, manager):
        """Test getting attributes for non-existent type returns empty list."""
        attrs = manager.get_attributes_for_type("NONEXISTENT-TYPE", "00046")
        assert attrs == []

    def test_get_element_types_for_nonexistent_element(self, manager):
        """Test getting types for non-existent element returns empty list."""
        types = manager.get_element_types("NONEXISTENT-ELEMENT", "00046")
        assert types == []