"""Unit tests for XML serialization decorators."""

import pytest
from armodel2.serialization.decorators import polymorphic


class TestPolymorphicDecorator:
    """Test @polymorphic decorator."""

    def test_polymorphic_decorator_sets_markers(self):
        """Test that @polymorphic decorator sets the correct markers."""
        @polymorphic({"VALUE-SPEC": "ValueSpecification"})
        def test_attr():
            pass

        assert hasattr(test_attr, '_is_polymorphic')
        assert test_attr._is_polymorphic is True
        assert hasattr(test_attr, '_polymorphic_mapping')
        assert test_attr._polymorphic_mapping == {"VALUE-SPEC": "ValueSpecification"}

    def test_polymorphic_with_multiple_mappings(self):
        """Test @polymorphic with multiple wrapper mappings."""
        @polymorphic({
            "COMPU-INTERNAL-TO-PHYS": "CompuContent",
            "COMPU-PHYS-TO-INTERNAL": "CompuContent"
        })
        def test_attr():
            pass

        assert test_attr._polymorphic_mapping == {
            "COMPU-INTERNAL-TO-PHYS": "CompuContent",
            "COMPU-PHYS-TO-INTERNAL": "CompuContent"
        }

    def test_polymorphic_decorator_returns_original_function(self):
        """Test that @polymorphic decorator returns the original function."""
        @polymorphic({"VALUE-SPEC": "ValueSpecification"})
        def test_func():
            return "test"

        assert test_func() == "test"

    def test_polymorphic_with_property(self):
        """Test @polymorphic decorator works with properties."""
        class TestClass:
            def __init__(self):
                self._value = None

            @property
            @polymorphic({"VALUE-SPEC": "ValueSpecification"})
            def test_prop(self):
                return self._value

            @test_prop.setter
            def test_prop(self, value):
                self._value = value

        obj = TestClass()

        # Verify the property getter has the polymorphic markers
        assert hasattr(TestClass.test_prop.fget, '_is_polymorphic')
        assert TestClass.test_prop.fget._is_polymorphic is True
        assert TestClass.test_prop.fget._polymorphic_mapping == {"VALUE-SPEC": "ValueSpecification"}
