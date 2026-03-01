"""IEEE1722TpAcfCan AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 661)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import IEEE1722TpAcfBusBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpAcfCan(IEEE1722TpAcfBus):
    """AUTOSAR IEEE1722TpAcfCan."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-E-E-E1722-TP-ACF-CAN"


    message_type_message_type_enum: Optional[IEEE1722TpAcfCan]
    _DESERIALIZE_DISPATCH = {
        "MESSAGE-TYPE-MESSAGE-TYPE-ENUM": lambda obj, elem: setattr(obj, "message_type_message_type_enum", SerializationHelper.deserialize_by_tag(elem, "IEEE1722TpAcfCan")),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfCan."""
        super().__init__()
        self.message_type_message_type_enum: Optional[IEEE1722TpAcfCan] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfCan to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfCan, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize message_type_message_type_enum
        if self.message_type_message_type_enum is not None:
            serialized = SerializationHelper.serialize_item(self.message_type_message_type_enum, "IEEE1722TpAcfCan")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-TYPE-MESSAGE-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfCan":
        """Deserialize XML element to IEEE1722TpAcfCan object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfCan object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfCan, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "MESSAGE-TYPE-MESSAGE-TYPE-ENUM":
                setattr(obj, "message_type_message_type_enum", SerializationHelper.deserialize_by_tag(child, "IEEE1722TpAcfCan"))

        return obj



class IEEE1722TpAcfCanBuilder(IEEE1722TpAcfBusBuilder):
    """Builder for IEEE1722TpAcfCan with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpAcfCan = IEEE1722TpAcfCan()


    def with_message_type_message_type_enum(self, value: Optional[IEEE1722TpAcfCan]) -> "IEEE1722TpAcfCanBuilder":
        """Set message_type_message_type_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.message_type_message_type_enum = value
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


    def build(self) -> IEEE1722TpAcfCan:
        """Build and return the IEEE1722TpAcfCan instance with validation."""
        self._validate_instance()
        pass
        return self._obj