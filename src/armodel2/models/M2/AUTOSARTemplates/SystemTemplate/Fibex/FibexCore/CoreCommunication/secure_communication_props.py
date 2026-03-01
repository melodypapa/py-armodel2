"""SecureCommunicationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 369)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecureCommunicationProps(ARObject):
    """AUTOSAR SecureCommunicationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURE-COMMUNICATION-PROPS"


    auth_data: Optional[PositiveInteger]
    authentication: Optional[PositiveInteger]
    data_id: Optional[PositiveInteger]
    freshness_value: Optional[PositiveInteger]
    message_link: Optional[PositiveInteger]
    secondary: Optional[PositiveInteger]
    secured_area: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "AUTH-DATA": lambda obj, elem: setattr(obj, "auth_data", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "AUTHENTICATION": lambda obj, elem: setattr(obj, "authentication", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "DATA-ID": lambda obj, elem: setattr(obj, "data_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "FRESHNESS-VALUE": lambda obj, elem: setattr(obj, "freshness_value", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MESSAGE-LINK": lambda obj, elem: setattr(obj, "message_link", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SECONDARY": lambda obj, elem: setattr(obj, "secondary", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SECURED-AREA": lambda obj, elem: setattr(obj, "secured_area", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize SecureCommunicationProps."""
        super().__init__()
        self.auth_data: Optional[PositiveInteger] = None
        self.authentication: Optional[PositiveInteger] = None
        self.data_id: Optional[PositiveInteger] = None
        self.freshness_value: Optional[PositiveInteger] = None
        self.message_link: Optional[PositiveInteger] = None
        self.secondary: Optional[PositiveInteger] = None
        self.secured_area: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SecureCommunicationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecureCommunicationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auth_data
        if self.auth_data is not None:
            serialized = SerializationHelper.serialize_item(self.auth_data, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTH-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize authentication
        if self.authentication is not None:
            serialized = SerializationHelper.serialize_item(self.authentication, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTHENTICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_id
        if self.data_id is not None:
            serialized = SerializationHelper.serialize_item(self.data_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize freshness_value
        if self.freshness_value is not None:
            serialized = SerializationHelper.serialize_item(self.freshness_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRESHNESS-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_link
        if self.message_link is not None:
            serialized = SerializationHelper.serialize_item(self.message_link, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-LINK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize secondary
        if self.secondary is not None:
            serialized = SerializationHelper.serialize_item(self.secondary, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECONDARY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize secured_area
        if self.secured_area is not None:
            serialized = SerializationHelper.serialize_item(self.secured_area, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURED-AREA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationProps":
        """Deserialize XML element to SecureCommunicationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecureCommunicationProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AUTH-DATA":
                setattr(obj, "auth_data", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "AUTHENTICATION":
                setattr(obj, "authentication", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "DATA-ID":
                setattr(obj, "data_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "FRESHNESS-VALUE":
                setattr(obj, "freshness_value", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MESSAGE-LINK":
                setattr(obj, "message_link", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SECONDARY":
                setattr(obj, "secondary", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SECURED-AREA":
                setattr(obj, "secured_area", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class SecureCommunicationPropsBuilder(BuilderBase):
    """Builder for SecureCommunicationProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecureCommunicationProps = SecureCommunicationProps()


    def with_auth_data(self, value: Optional[PositiveInteger]) -> "SecureCommunicationPropsBuilder":
        """Set auth_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.auth_data = value
        return self

    def with_authentication(self, value: Optional[PositiveInteger]) -> "SecureCommunicationPropsBuilder":
        """Set authentication attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.authentication = value
        return self

    def with_data_id(self, value: Optional[PositiveInteger]) -> "SecureCommunicationPropsBuilder":
        """Set data_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_id = value
        return self

    def with_freshness_value(self, value: Optional[PositiveInteger]) -> "SecureCommunicationPropsBuilder":
        """Set freshness_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.freshness_value = value
        return self

    def with_message_link(self, value: Optional[PositiveInteger]) -> "SecureCommunicationPropsBuilder":
        """Set message_link attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.message_link = value
        return self

    def with_secondary(self, value: Optional[PositiveInteger]) -> "SecureCommunicationPropsBuilder":
        """Set secondary attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.secondary = value
        return self

    def with_secured_area(self, value: Optional[PositiveInteger]) -> "SecureCommunicationPropsBuilder":
        """Set secured_area attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.secured_area = value
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


    def build(self) -> SecureCommunicationProps:
        """Build and return the SecureCommunicationProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj