"""FlexrayFifoRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayFifoRange(ARObject):
    """AUTOSAR FlexrayFifoRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-FIFO-RANGE"


    range_max: Optional[Integer]
    range_min: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "RANGE-MAX": lambda obj, elem: setattr(obj, "range_max", elem.text),
        "RANGE-MIN": lambda obj, elem: setattr(obj, "range_min", elem.text),
    }


    def __init__(self) -> None:
        """Initialize FlexrayFifoRange."""
        super().__init__()
        self.range_max: Optional[Integer] = None
        self.range_min: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayFifoRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayFifoRange, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize range_max
        if self.range_max is not None:
            serialized = SerializationHelper.serialize_item(self.range_max, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RANGE-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize range_min
        if self.range_min is not None:
            serialized = SerializationHelper.serialize_item(self.range_min, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RANGE-MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFifoRange":
        """Deserialize XML element to FlexrayFifoRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayFifoRange object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayFifoRange, cls).deserialize(element)

        # Parse range_max
        child = SerializationHelper.find_child_element(element, "RANGE-MAX")
        if child is not None:
            range_max_value = child.text
            obj.range_max = range_max_value

        # Parse range_min
        child = SerializationHelper.find_child_element(element, "RANGE-MIN")
        if child is not None:
            range_min_value = child.text
            obj.range_min = range_min_value

        return obj



class FlexrayFifoRangeBuilder(BuilderBase):
    """Builder for FlexrayFifoRange with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayFifoRange = FlexrayFifoRange()


    def with_range_max(self, value: Optional[Integer]) -> "FlexrayFifoRangeBuilder":
        """Set range_max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.range_max = value
        return self

    def with_range_min(self, value: Optional[Integer]) -> "FlexrayFifoRangeBuilder":
        """Set range_min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.range_min = value
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


    def build(self) -> FlexrayFifoRange:
        """Build and return the FlexrayFifoRange instance with validation."""
        self._validate_instance()
        pass
        return self._obj