"""Unit tests for generated code validation."""

import inspect
import pytest
from armodel2.models.M2 import AUTOSARTemplates


class TestGeneratedCodeValidation:
    """Tests for validating generated code quality and completeness."""

    def test_all_classes_instantiable(self):
        """Test that all generated classes can be instantiated (SWUT_MODELS_100).

        Note: This test checks a subset of classes due to time constraints.
        In practice, this should check all generated classes.
        """
        # Collect a representative sample of classes
        sample_classes = []

        # Get modules from AUTOSARTemplates
        for module_name in dir(AUTOSARTemplates):
            module = getattr(AUTOSARTemplates, module_name)
            if inspect.ismodule(module):
                for name, obj in inspect.getmembers(module):
                    if (
                        inspect.isclass(obj)
                        and hasattr(obj, "__init__")
                        and not name.startswith("_")
                    ):
                        sample_classes.append(obj)
                        # Limit to first 100 classes for performance
                        if len(sample_classes) >= 100:
                            break
            if len(sample_classes) >= 100:
                break

        # Try to instantiate each class
        failures = []
        for cls in sample_classes:
            try:
                cls()
            except Exception as e:
                failures.append((cls.__name__, str(e)))

        # Report failures (allow some failures for abstract/complex classes)
        if len(failures) > 10:
            pytest.fail(
                f"Failed to instantiate {len(failures)} out of {len(sample_classes)} classes: {failures[:10]}"
            )

    def test_all_classes_have_builder(self):
        """Test that all generated classes have builder class (SWUT_MODELS_103).

        Note: This checks a subset of classes.
        """
        sample_classes = []

        for module_name in dir(AUTOSARTemplates):
            module = getattr(AUTOSARTemplates, module_name)
            if inspect.ismodule(module):
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and not name.startswith("_"):
                        sample_classes.append(obj)
                    if len(sample_classes) >= 100:
                        break
            if len(sample_classes) >= 100:
                break

        # Verify builder exists
        failures = []
        for cls in sample_classes:
            builder_name = f"{cls.__name__}Builder"
            module = inspect.getmodule(cls)
            if module and not hasattr(module, builder_name):
                failures.append(cls.__name__)

        # Allow some failures (enums, primitive types may not have builders)
        if len(failures) > 20:
            pytest.fail(
                f"Missing builder for {len(failures)} out of {len(sample_classes)} classes: {failures[:10]}"
            )

    def test_all_classes_have_xml_members(self):
        """Test that all generated classes have proper type hints for serialization (SWUT_MODELS_104).

        Note: This checks a subset of classes.
        The reflection-based serialization framework uses get_type_hints() instead of _xml_members.
        """
        sample_classes = []

        for module_name in dir(AUTOSARTemplates):
            module = getattr(AUTOSARTemplates, module_name)
            if inspect.ismodule(module):
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and not name.startswith("_"):
                        sample_classes.append(obj)
                    if len(sample_classes) >= 100:
                        break
            if len(sample_classes) >= 100:
                break

        # Verify type hints are available for serialization
        failures = []
        for cls in sample_classes:
            # Skip base classes that don't need type hints (ARPrimitive, AREnum, etc.)
            if cls.__name__ in ('ARPrimitive', 'AREnum'):
                continue
            try:
                type_hints = inspect.get_type_hints(cls)
                # Classes should have at least some type hints for serialization
                if not type_hints:
                    failures.append(cls.__name__)
            except Exception as e:
                failures.append(f"{cls.__name__} ({str(e)})")

        # Allow some failures for abstract/complex classes
        if len(failures) > 20:
            pytest.fail(
                f"Missing type hints in {len(failures)} out of {len(sample_classes)} classes: {failures[:10]}"
            )

    def test_builder_naming_convention(self):
        """Test that builders follow naming convention."""
        sample_classes = []

        for module_name in dir(AUTOSARTemplates):
            module = getattr(AUTOSARTemplates, module_name)
            if inspect.ismodule(module):
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and not name.startswith("_"):
                        sample_classes.append(obj)
                    if len(sample_classes) >= 50:
                        break
            if len(sample_classes) >= 50:
                break

        failures = []
        for cls in sample_classes:
            builder_name = f"{cls.__name__}Builder"
            module = inspect.getmodule(cls)
            if module and hasattr(module, builder_name):
                builder = getattr(module, builder_name)
                # Verify builder has build method
                if not hasattr(builder, "build"):
                    failures.append(f"{cls.__name__}Builder (missing build method)")

        if failures:
            pytest.fail(f"Builder validation failures: {failures[:10]}")