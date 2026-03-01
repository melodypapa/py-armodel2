"""IEEE1722TpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 637)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpConnection(ARElement, ABC):
    """AUTOSAR IEEE1722TpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    destination_mac: Optional[MacAddressString]
    mac_address_string: Optional[MacAddressString]
    pdu_ref: Optional[ARRef]
    unique_stream_id: Optional[PositiveInteger]
    version: Optional[PositiveInteger]
    vlan_priority: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "DESTINATION-MAC": lambda obj, elem: setattr(obj, "destination_mac", SerializationHelper.deserialize_by_tag(elem, "MacAddressString")),
        "MAC-ADDRESS-STRING": lambda obj, elem: setattr(obj, "mac_address_string", SerializationHelper.deserialize_by_tag(elem, "MacAddressString")),
        "PDU-REF": lambda obj, elem: setattr(obj, "pdu_ref", ARRef.deserialize(elem)),
        "UNIQUE-STREAM-ID": lambda obj, elem: setattr(obj, "unique_stream_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "VERSION": lambda obj, elem: setattr(obj, "version", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "VLAN-PRIORITY": lambda obj, elem: setattr(obj, "vlan_priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpConnection."""
        super().__init__()
        self.destination_mac: Optional[MacAddressString] = None
        self.mac_address_string: Optional[MacAddressString] = None
        self.pdu_ref: Optional[ARRef] = None
        self.unique_stream_id: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None
        self.vlan_priority: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_mac
        if self.destination_mac is not None:
            serialized = SerializationHelper.serialize_item(self.destination_mac, "MacAddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-MAC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mac_address_string
        if self.mac_address_string is not None:
            serialized = SerializationHelper.serialize_item(self.mac_address_string, "MacAddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAC-ADDRESS-STRING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_ref
        if self.pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unique_stream_id
        if self.unique_stream_id is not None:
            serialized = SerializationHelper.serialize_item(self.unique_stream_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIQUE-STREAM-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize version
        if self.version is not None:
            serialized = SerializationHelper.serialize_item(self.version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan_priority
        if self.vlan_priority is not None:
            serialized = SerializationHelper.serialize_item(self.vlan_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpConnection":
        """Deserialize XML element to IEEE1722TpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DESTINATION-MAC":
                setattr(obj, "destination_mac", SerializationHelper.deserialize_by_tag(child, "MacAddressString"))
            elif tag == "MAC-ADDRESS-STRING":
                setattr(obj, "mac_address_string", SerializationHelper.deserialize_by_tag(child, "MacAddressString"))
            elif tag == "PDU-REF":
                setattr(obj, "pdu_ref", ARRef.deserialize(child))
            elif tag == "UNIQUE-STREAM-ID":
                setattr(obj, "unique_stream_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "VERSION":
                setattr(obj, "version", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "VLAN-PRIORITY":
                setattr(obj, "vlan_priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class IEEE1722TpConnectionBuilder(ARElementBuilder):
    """Builder for IEEE1722TpConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpConnection = IEEE1722TpConnection()


    def with_destination_mac(self, value: Optional[MacAddressString]) -> "IEEE1722TpConnectionBuilder":
        """Set destination_mac attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.destination_mac = value
        return self

    def with_mac_address_string(self, value: Optional[MacAddressString]) -> "IEEE1722TpConnectionBuilder":
        """Set mac_address_string attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mac_address_string = value
        return self

    def with_pdu(self, value: Optional[PduTriggering]) -> "IEEE1722TpConnectionBuilder":
        """Set pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdu = value
        return self

    def with_unique_stream_id(self, value: Optional[PositiveInteger]) -> "IEEE1722TpConnectionBuilder":
        """Set unique_stream_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unique_stream_id = value
        return self

    def with_version(self, value: Optional[PositiveInteger]) -> "IEEE1722TpConnectionBuilder":
        """Set version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.version = value
        return self

    def with_vlan_priority(self, value: Optional[PositiveInteger]) -> "IEEE1722TpConnectionBuilder":
        """Set vlan_priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vlan_priority = value
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


    @abstractmethod
    def build(self) -> IEEE1722TpConnection:
        """Build and return the IEEE1722TpConnection instance (abstract)."""
        raise NotImplementedError