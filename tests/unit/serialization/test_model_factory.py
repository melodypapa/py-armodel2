"""Unit tests for ModelFactory."""

import pytest
from armodel2.serialization.model_factory import ModelFactory


class TestModelFactory:
    """Unit tests for ModelFactory."""

    def test_singleton_pattern(self) -> None:
        """Test that ModelFactory follows singleton pattern."""
        factory1 = ModelFactory()
        factory2 = ModelFactory()
        assert factory1 is factory2

    def test_load_mappings(self) -> None:
        """Test loading mappings from YAML file."""
        factory = ModelFactory()
        factory.load_mappings()
        assert factory.is_initialized()

    def test_get_class_by_xml_tag(self) -> None:
        """Test getting class by XML tag."""
        factory = ModelFactory()
        factory.load_mappings()

        cls = factory.get_class("SW-BASE-TYPE")
        assert cls is not None
        assert cls.__name__ == "SwBaseType"

    def test_get_class_by_xml_tag_ar_package(self) -> None:
        """Test getting ARPackage class by XML tag."""
        factory = ModelFactory()
        factory.load_mappings()

        cls = factory.get_class("AR-PACKAGE")
        assert cls is not None
        assert cls.__name__ == "ARPackage"

    def test_get_class_caching(self) -> None:
        """Test that class lookups are cached."""
        factory = ModelFactory()
        factory.load_mappings()

        # First call
        cls1 = factory.get_class("SW-BASE-TYPE")
        # Second call should use cache
        cls2 = factory.get_class("SW-BASE-TYPE")

        assert cls1 is cls2

    def test_polymorphic_implementations(self) -> None:
        """Test getting polymorphic implementations."""
        factory = ModelFactory()
        factory.load_mappings()

        implementations = factory.get_polymorphic_implementations("PackageableElement")
        assert len(implementations) > 0
        # PackageableElement has ARElement, EnumerationMappingTable, FibexElement as direct subclasses
        assert "ARElement" in implementations

    def test_resolve_polymorphic_type(self) -> None:
        """Test resolving polymorphic type from XML tag."""
        factory = ModelFactory()
        factory.load_mappings()

        # Test with a known polymorphic relationship
        cls = factory.resolve_polymorphic_type("AR-ELEMENT", "PackageableElement")
        assert cls is not None
        assert cls.__name__ == "ARElement"

    def test_clear_cache(self) -> None:
        """Test clearing class import cache."""
        factory = ModelFactory()
        factory.load_mappings()

        # Get class to populate cache
        cls1 = factory.get_class("SW-BASE-TYPE")
        assert cls1 is not None

        # Clear cache
        factory.clear_cache()

        # Get class again - should still work
        cls2 = factory.get_class("SW-BASE-TYPE")
        assert cls2 is not None
        assert cls2.__name__ == "SwBaseType"

    def test_nonexistent_class(self) -> None:
        """Test getting a nonexistent class returns None when raise_on_failure=False."""
        factory = ModelFactory()
        factory.load_mappings()

        cls = factory.get_class("NONEXISTENT-TAG", raise_on_failure=False)
        assert cls is None

    def test_nonexistent_class_raises(self) -> None:
        """Test getting a nonexistent class raises ImportError by default."""
        factory = ModelFactory()
        factory.load_mappings()

        with pytest.raises(ImportError):
            factory.get_class("NONEXISTENT-TAG")