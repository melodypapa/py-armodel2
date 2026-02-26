"""FlexrayAbsolutelyScheduledTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 423)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayAbsolutelyScheduledTiming(ARObject):
    """AUTOSAR FlexrayAbsolutelyScheduledTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication_cycle_cycle: Optional[CommunicationCycle]
    slot_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize FlexrayAbsolutelyScheduledTiming."""
        super().__init__()
        self.communication_cycle_cycle: Optional[CommunicationCycle] = None
        self.slot_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayAbsolutelyScheduledTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayAbsolutelyScheduledTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_cycle_cycle
        if self.communication_cycle_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.communication_cycle_cycle, "CommunicationCycle")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CYCLE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slot_id
        if self.slot_id is not None:
            serialized = SerializationHelper.serialize_item(self.slot_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLOT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayAbsolutelyScheduledTiming":
        """Deserialize XML element to FlexrayAbsolutelyScheduledTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayAbsolutelyScheduledTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayAbsolutelyScheduledTiming, cls).deserialize(element)

        # Parse communication_cycle_cycle
        child = SerializationHelper.find_child_element(element, "COMMUNICATION-CYCLE-CYCLE")
        if child is not None:
            communication_cycle_cycle_value = SerializationHelper.deserialize_by_tag(child, "CommunicationCycle")
            obj.communication_cycle_cycle = communication_cycle_cycle_value

        # Parse slot_id
        child = SerializationHelper.find_child_element(element, "SLOT-ID")
        if child is not None:
            slot_id_value = child.text
            obj.slot_id = slot_id_value

        return obj



class FlexrayAbsolutelyScheduledTimingBuilder(BuilderBase):
    """Builder for FlexrayAbsolutelyScheduledTiming with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayAbsolutelyScheduledTiming = FlexrayAbsolutelyScheduledTiming()


    def with_communication_cycle_cycle(self, value: Optional[CommunicationCycle]) -> "FlexrayAbsolutelyScheduledTimingBuilder":
        """Set communication_cycle_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.communication_cycle_cycle = value
        return self

    def with_slot_id(self, value: Optional[PositiveInteger]) -> "FlexrayAbsolutelyScheduledTimingBuilder":
        """Set slot_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.slot_id = value
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


    def build(self) -> FlexrayAbsolutelyScheduledTiming:
        """Build and return the FlexrayAbsolutelyScheduledTiming instance with validation."""
        self._validate_instance()
        pass
        return self._obj