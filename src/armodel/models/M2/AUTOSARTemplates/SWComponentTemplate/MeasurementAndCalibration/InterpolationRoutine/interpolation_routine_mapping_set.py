"""InterpolationRoutineMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 429)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 46)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_InterpolationRoutine.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine import (
    InterpolationRoutine,
)


class InterpolationRoutineMappingSet(ARElement):
    """AUTOSAR InterpolationRoutineMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    interpolation_routines: list[InterpolationRoutine]
    def __init__(self) -> None:
        """Initialize InterpolationRoutineMappingSet."""
        super().__init__()
        self.interpolation_routines: list[InterpolationRoutine] = []

    def serialize(self) -> ET.Element:
        """Serialize InterpolationRoutineMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InterpolationRoutineMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize interpolation_routines (list to container "INTERPOLATION-ROUTINES")
        if self.interpolation_routines:
            wrapper = ET.Element("INTERPOLATION-ROUTINES")
            for item in self.interpolation_routines:
                serialized = SerializationHelper.serialize_item(item, "InterpolationRoutine")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InterpolationRoutineMappingSet":
        """Deserialize XML element to InterpolationRoutineMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InterpolationRoutineMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InterpolationRoutineMappingSet, cls).deserialize(element)

        # Parse interpolation_routines (list from container "INTERPOLATION-ROUTINES")
        obj.interpolation_routines = []
        container = SerializationHelper.find_child_element(element, "INTERPOLATION-ROUTINES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.interpolation_routines.append(child_value)

        return obj



class InterpolationRoutineMappingSetBuilder(ARElementBuilder):
    """Builder for InterpolationRoutineMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InterpolationRoutineMappingSet = InterpolationRoutineMappingSet()


    def with_interpolation_routines(self, items: list[InterpolationRoutine]) -> "InterpolationRoutineMappingSetBuilder":
        """Set interpolation_routines list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routines = list(items) if items else []
        return self


    def add_interpolation_routine(self, item: InterpolationRoutine) -> "InterpolationRoutineMappingSetBuilder":
        """Add a single item to interpolation_routines list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routines.append(item)
        return self

    def clear_interpolation_routines(self) -> "InterpolationRoutineMappingSetBuilder":
        """Clear all items from interpolation_routines list.

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routines = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> InterpolationRoutineMappingSet:
        """Build and return the InterpolationRoutineMappingSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj