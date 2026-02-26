"""TDLETZoneClock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import TimingClockBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDLETZoneClock(TimingClock):
    """AUTOSAR TDLETZoneClock."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accuracy_ext: Optional[MultidimensionalTime]
    accuracy_int: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize TDLETZoneClock."""
        super().__init__()
        self.accuracy_ext: Optional[MultidimensionalTime] = None
        self.accuracy_int: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize TDLETZoneClock to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDLETZoneClock, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accuracy_ext
        if self.accuracy_ext is not None:
            serialized = SerializationHelper.serialize_item(self.accuracy_ext, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCURACY-EXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize accuracy_int
        if self.accuracy_int is not None:
            serialized = SerializationHelper.serialize_item(self.accuracy_int, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCURACY-INT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDLETZoneClock":
        """Deserialize XML element to TDLETZoneClock object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDLETZoneClock object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDLETZoneClock, cls).deserialize(element)

        # Parse accuracy_ext
        child = SerializationHelper.find_child_element(element, "ACCURACY-EXT")
        if child is not None:
            accuracy_ext_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.accuracy_ext = accuracy_ext_value

        # Parse accuracy_int
        child = SerializationHelper.find_child_element(element, "ACCURACY-INT")
        if child is not None:
            accuracy_int_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.accuracy_int = accuracy_int_value

        return obj



class TDLETZoneClockBuilder(TimingClockBuilder):
    """Builder for TDLETZoneClock with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDLETZoneClock = TDLETZoneClock()


    def with_accuracy_ext(self, value: Optional[MultidimensionalTime]) -> "TDLETZoneClockBuilder":
        """Set accuracy_ext attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.accuracy_ext = value
        return self

    def with_accuracy_int(self, value: Optional[MultidimensionalTime]) -> "TDLETZoneClockBuilder":
        """Set accuracy_int attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.accuracy_int = value
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


    def build(self) -> TDLETZoneClock:
        """Build and return the TDLETZoneClock instance with validation."""
        self._validate_instance()
        pass
        return self._obj