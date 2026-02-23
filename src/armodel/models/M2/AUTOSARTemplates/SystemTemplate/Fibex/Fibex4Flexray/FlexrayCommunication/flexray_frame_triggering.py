"""FlexrayFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 422)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import FrameTriggeringBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication.flexray_absolutely_scheduled_timing import (
    FlexrayAbsolutelyScheduledTiming,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class FlexrayFrameTriggering(FrameTriggering):
    """AUTOSAR FlexrayFrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _absolutelies: list[FlexrayAbsolutelyScheduledTiming]
    allow_dynamic: Optional[Boolean]
    message_id: Optional[PositiveInteger]
    payload_preamble: Optional[Any]
    def __init__(self) -> None:
        """Initialize FlexrayFrameTriggering."""
        super().__init__()
        self._absolutelies: list[FlexrayAbsolutelyScheduledTiming] = []
        self.allow_dynamic: Optional[Boolean] = None
        self.message_id: Optional[PositiveInteger] = None
        self.payload_preamble: Optional[Any] = None
    @property
    @xml_element_name("ABSOLUTELYS")
    def absolutelies(self) -> list[FlexrayAbsolutelyScheduledTiming]:
        """Get absolutelies with custom XML element name."""
        return self._absolutelies

    @absolutelies.setter
    def absolutelies(self, value: list[FlexrayAbsolutelyScheduledTiming]) -> None:
        """Set absolutelies with custom XML element name."""
        self._absolutelies = value


    def serialize(self) -> ET.Element:
        """Serialize FlexrayFrameTriggering to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayFrameTriggering, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize absolutelies (list to container "ABSOLUTELYS")
        if self.absolutelies:
            wrapper = ET.Element("ABSOLUTELYS")
            for item in self.absolutelies:
                serialized = SerializationHelper.serialize_item(item, "FlexrayAbsolutelyScheduledTiming")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize allow_dynamic
        if self.allow_dynamic is not None:
            serialized = SerializationHelper.serialize_item(self.allow_dynamic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALLOW-DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_id
        if self.message_id is not None:
            serialized = SerializationHelper.serialize_item(self.message_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize payload_preamble
        if self.payload_preamble is not None:
            serialized = SerializationHelper.serialize_item(self.payload_preamble, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PAYLOAD-PREAMBLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFrameTriggering":
        """Deserialize XML element to FlexrayFrameTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayFrameTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayFrameTriggering, cls).deserialize(element)

        # Parse absolutelies (list from container "ABSOLUTELYS")
        obj.absolutelies = []
        container = SerializationHelper.find_child_element(element, "ABSOLUTELYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.absolutelies.append(child_value)

        # Parse allow_dynamic
        child = SerializationHelper.find_child_element(element, "ALLOW-DYNAMIC")
        if child is not None:
            allow_dynamic_value = child.text
            obj.allow_dynamic = allow_dynamic_value

        # Parse message_id
        child = SerializationHelper.find_child_element(element, "MESSAGE-ID")
        if child is not None:
            message_id_value = child.text
            obj.message_id = message_id_value

        # Parse payload_preamble
        child = SerializationHelper.find_child_element(element, "PAYLOAD-PREAMBLE")
        if child is not None:
            payload_preamble_value = child.text
            obj.payload_preamble = payload_preamble_value

        return obj



class FlexrayFrameTriggeringBuilder(FrameTriggeringBuilder):
    """Builder for FlexrayFrameTriggering with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayFrameTriggering = FlexrayFrameTriggering()


    def with_absolutelies(self, items: list[FlexrayAbsolutelyScheduledTiming]) -> "FlexrayFrameTriggeringBuilder":
        """Set absolutelies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.absolutelies = list(items) if items else []
        return self

    def with_allow_dynamic(self, value: Optional[Boolean]) -> "FlexrayFrameTriggeringBuilder":
        """Set allow_dynamic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.allow_dynamic = value
        return self

    def with_message_id(self, value: Optional[PositiveInteger]) -> "FlexrayFrameTriggeringBuilder":
        """Set message_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.message_id = value
        return self

    def with_payload_preamble(self, value: Optional[any (BooleanIndicator)]) -> "FlexrayFrameTriggeringBuilder":
        """Set payload_preamble attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.payload_preamble = value
        return self


    def add_absolutelie(self, item: FlexrayAbsolutelyScheduledTiming) -> "FlexrayFrameTriggeringBuilder":
        """Add a single item to absolutelies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.absolutelies.append(item)
        return self

    def clear_absolutelies(self) -> "FlexrayFrameTriggeringBuilder":
        """Clear all items from absolutelies list.

        Returns:
            self for method chaining
        """
        self._obj.absolutelies = []
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


    def build(self) -> FlexrayFrameTriggering:
        """Build and return the FlexrayFrameTriggering instance with validation."""
        self._validate_instance()
        pass
        return self._obj