"""SocketConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2057)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ObsoleteModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import DescribableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_connection_ipdu_identifier_set import (
    SocketConnectionIpduIdentifierSet,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SocketConnection(Describable):
    """AUTOSAR SocketConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SOCKET-CONNECTION"


    client_ip_addr: Optional[Boolean]
    client_port_ref: Optional[ARRef]
    client_port_from: Optional[Boolean]
    pdus: list[SocketConnectionIpduIdentifierSet]
    pdu_collection: Optional[TimeValue]
    runtime_ip: Optional[Any]
    runtime_port: Optional[Any]
    short_label: Optional[Identifier]
    _DESERIALIZE_DISPATCH = {
        "CLIENT-IP-ADDR": lambda obj, elem: setattr(obj, "client_ip_addr", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "CLIENT-PORT-REF": lambda obj, elem: setattr(obj, "client_port_ref", ARRef.deserialize(elem)),
        "CLIENT-PORT-FROM": lambda obj, elem: setattr(obj, "client_port_from", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "PDUS": lambda obj, elem: obj.pdus.append(SerializationHelper.deserialize_by_tag(elem, "SocketConnectionIpduIdentifierSet")),
        "PDU-COLLECTION": lambda obj, elem: setattr(obj, "pdu_collection", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "RUNTIME-IP": lambda obj, elem: setattr(obj, "runtime_ip", SerializationHelper.deserialize_by_tag(elem, "any (RuntimeAddress)")),
        "RUNTIME-PORT": lambda obj, elem: setattr(obj, "runtime_port", SerializationHelper.deserialize_by_tag(elem, "any (RuntimeAddress)")),
        "SHORT-LABEL": lambda obj, elem: setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
    }


    def __init__(self) -> None:
        """Initialize SocketConnection."""
        super().__init__()
        self.client_ip_addr: Optional[Boolean] = None
        self.client_port_ref: Optional[ARRef] = None
        self.client_port_from: Optional[Boolean] = None
        self.pdus: list[SocketConnectionIpduIdentifierSet] = []
        self.pdu_collection: Optional[TimeValue] = None
        self.runtime_ip: Optional[Any] = None
        self.runtime_port: Optional[Any] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize SocketConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SocketConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_ip_addr
        if self.client_ip_addr is not None:
            serialized = SerializationHelper.serialize_item(self.client_ip_addr, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-IP-ADDR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize client_port_ref
        if self.client_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.client_port_ref, "SocketAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize client_port_from
        if self.client_port_from is not None:
            serialized = SerializationHelper.serialize_item(self.client_port_from, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-PORT-FROM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdus (list to container "PDUS")
        if self.pdus:
            wrapper = ET.Element("PDUS")
            for item in self.pdus:
                serialized = SerializationHelper.serialize_item(item, "SocketConnectionIpduIdentifierSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pdu_collection
        if self.pdu_collection is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_collection, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-COLLECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize runtime_ip
        if self.runtime_ip is not None:
            serialized = SerializationHelper.serialize_item(self.runtime_ip, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RUNTIME-IP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize runtime_port
        if self.runtime_port is not None:
            serialized = SerializationHelper.serialize_item(self.runtime_port, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RUNTIME-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketConnection":
        """Deserialize XML element to SocketConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SocketConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SocketConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CLIENT-IP-ADDR":
                setattr(obj, "client_ip_addr", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "CLIENT-PORT-REF":
                setattr(obj, "client_port_ref", ARRef.deserialize(child))
            elif tag == "CLIENT-PORT-FROM":
                setattr(obj, "client_port_from", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "PDUS":
                obj.pdus.append(SerializationHelper.deserialize_by_tag(child, "SocketConnectionIpduIdentifierSet"))
            elif tag == "PDU-COLLECTION":
                setattr(obj, "pdu_collection", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "RUNTIME-IP":
                setattr(obj, "runtime_ip", SerializationHelper.deserialize_by_tag(child, "any (RuntimeAddress)"))
            elif tag == "RUNTIME-PORT":
                setattr(obj, "runtime_port", SerializationHelper.deserialize_by_tag(child, "any (RuntimeAddress)"))
            elif tag == "SHORT-LABEL":
                setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(child, "Identifier"))

        return obj



class SocketConnectionBuilder(DescribableBuilder):
    """Builder for SocketConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SocketConnection = SocketConnection()


    def with_client_ip_addr(self, value: Optional[Boolean]) -> "SocketConnectionBuilder":
        """Set client_ip_addr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.client_ip_addr = value
        return self

    def with_client_port(self, value: Optional[SocketAddress]) -> "SocketConnectionBuilder":
        """Set client_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.client_port = value
        return self

    def with_client_port_from(self, value: Optional[Boolean]) -> "SocketConnectionBuilder":
        """Set client_port_from attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.client_port_from = value
        return self

    def with_pdus(self, items: list[SocketConnectionIpduIdentifierSet]) -> "SocketConnectionBuilder":
        """Set pdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pdus = list(items) if items else []
        return self

    def with_pdu_collection(self, value: Optional[TimeValue]) -> "SocketConnectionBuilder":
        """Set pdu_collection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdu_collection = value
        return self

    def with_runtime_ip(self, value: Optional[any (RuntimeAddress)]) -> "SocketConnectionBuilder":
        """Set runtime_ip attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.runtime_ip = value
        return self

    def with_runtime_port(self, value: Optional[any (RuntimeAddress)]) -> "SocketConnectionBuilder":
        """Set runtime_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.runtime_port = value
        return self

    def with_short_label(self, value: Optional[Identifier]) -> "SocketConnectionBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
        return self


    def add_pdu(self, item: SocketConnectionIpduIdentifierSet) -> "SocketConnectionBuilder":
        """Add a single item to pdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pdus.append(item)
        return self

    def clear_pdus(self) -> "SocketConnectionBuilder":
        """Clear all items from pdus list.

        Returns:
            self for method chaining
        """
        self._obj.pdus = []
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


    def build(self) -> SocketConnection:
        """Build and return the SocketConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj