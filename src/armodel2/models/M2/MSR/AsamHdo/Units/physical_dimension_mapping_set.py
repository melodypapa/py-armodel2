"""PhysicalDimensionMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 399)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PhysicalDimensionMappingSet(ARElement):
    """AUTOSAR PhysicalDimensionMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PHYSICAL-DIMENSION-MAPPING-SET"


    physicals: list[PhysicalDimension]
    _DESERIALIZE_DISPATCH = {
        "PHYSICALS": lambda obj, elem: obj.physicals.append(PhysicalDimension.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize PhysicalDimensionMappingSet."""
        super().__init__()
        self.physicals: list[PhysicalDimension] = []

    def serialize(self) -> ET.Element:
        """Serialize PhysicalDimensionMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PhysicalDimensionMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize physicals (list to container "PHYSICALS")
        if self.physicals:
            wrapper = ET.Element("PHYSICALS")
            for item in self.physicals:
                serialized = SerializationHelper.serialize_item(item, "PhysicalDimension")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalDimensionMappingSet":
        """Deserialize XML element to PhysicalDimensionMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysicalDimensionMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PhysicalDimensionMappingSet, cls).deserialize(element)

        # Parse physicals (list from container "PHYSICALS")
        obj.physicals = []
        container = SerializationHelper.find_child_element(element, "PHYSICALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physicals.append(child_value)

        return obj



class PhysicalDimensionMappingSetBuilder(ARElementBuilder):
    """Builder for PhysicalDimensionMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PhysicalDimensionMappingSet = PhysicalDimensionMappingSet()


    def with_physicals(self, items: list[PhysicalDimension]) -> "PhysicalDimensionMappingSetBuilder":
        """Set physicals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.physicals = list(items) if items else []
        return self


    def add_physical(self, item: PhysicalDimension) -> "PhysicalDimensionMappingSetBuilder":
        """Add a single item to physicals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.physicals.append(item)
        return self

    def clear_physicals(self) -> "PhysicalDimensionMappingSetBuilder":
        """Clear all items from physicals list.

        Returns:
            self for method chaining
        """
        self._obj.physicals = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> PhysicalDimensionMappingSet:
        """Build and return the PhysicalDimensionMappingSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj