"""CanNmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 684)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import NmNodeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanNmNode(NmNode):
    """AUTOSAR CanNmNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-NM-NODE"


    all_nm_messages: Optional[Boolean]
    nm_car_wake_up: Optional[Boolean]
    nm_msg_cycle: Optional[TimeValue]
    nm_msg: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "ALL-NM-MESSAGES": lambda obj, elem: setattr(obj, "all_nm_messages", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "NM-CAR-WAKE-UP": lambda obj, elem: setattr(obj, "nm_car_wake_up", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "NM-MSG-CYCLE": lambda obj, elem: setattr(obj, "nm_msg_cycle", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "NM-MSG": lambda obj, elem: setattr(obj, "nm_msg", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize CanNmNode."""
        super().__init__()
        self.all_nm_messages: Optional[Boolean] = None
        self.nm_car_wake_up: Optional[Boolean] = None
        self.nm_msg_cycle: Optional[TimeValue] = None
        self.nm_msg: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize CanNmNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanNmNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize all_nm_messages
        if self.all_nm_messages is not None:
            serialized = SerializationHelper.serialize_item(self.all_nm_messages, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALL-NM-MESSAGES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_car_wake_up
        if self.nm_car_wake_up is not None:
            serialized = SerializationHelper.serialize_item(self.nm_car_wake_up, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CAR-WAKE-UP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_msg_cycle
        if self.nm_msg_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.nm_msg_cycle, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-MSG-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_msg
        if self.nm_msg is not None:
            serialized = SerializationHelper.serialize_item(self.nm_msg, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-MSG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanNmNode":
        """Deserialize XML element to CanNmNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanNmNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanNmNode, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALL-NM-MESSAGES":
                setattr(obj, "all_nm_messages", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "NM-CAR-WAKE-UP":
                setattr(obj, "nm_car_wake_up", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "NM-MSG-CYCLE":
                setattr(obj, "nm_msg_cycle", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "NM-MSG":
                setattr(obj, "nm_msg", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class CanNmNodeBuilder(NmNodeBuilder):
    """Builder for CanNmNode with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanNmNode = CanNmNode()


    def with_all_nm_messages(self, value: Optional[Boolean]) -> "CanNmNodeBuilder":
        """Set all_nm_messages attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.all_nm_messages = value
        return self

    def with_nm_car_wake_up(self, value: Optional[Boolean]) -> "CanNmNodeBuilder":
        """Set nm_car_wake_up attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_car_wake_up = value
        return self

    def with_nm_msg_cycle(self, value: Optional[TimeValue]) -> "CanNmNodeBuilder":
        """Set nm_msg_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_msg_cycle = value
        return self

    def with_nm_msg(self, value: Optional[TimeValue]) -> "CanNmNodeBuilder":
        """Set nm_msg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_msg = value
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


    def build(self) -> CanNmNode:
        """Build and return the CanNmNode instance with validation."""
        self._validate_instance()
        pass
        return self._obj