"""SocketConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2057)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ObsoleteModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_connection_ipdu_identifier_set import (
    SocketConnectionIpduIdentifierSet,
)


class SocketConnection(Describable):
    """AUTOSAR SocketConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_ip_addr: Optional[Boolean]
    client_port_ref: Optional[ARRef]
    client_port_from: Optional[Boolean]
    pdus: list[SocketConnectionIpduIdentifierSet]
    pdu_collection: Optional[TimeValue]
    runtime_ip: Optional[Any]
    runtime_port: Optional[Any]
    short_label: Optional[Identifier]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse client_ip_addr
        child = SerializationHelper.find_child_element(element, "CLIENT-IP-ADDR")
        if child is not None:
            client_ip_addr_value = child.text
            obj.client_ip_addr = client_ip_addr_value

        # Parse client_port_ref
        child = SerializationHelper.find_child_element(element, "CLIENT-PORT-REF")
        if child is not None:
            client_port_ref_value = ARRef.deserialize(child)
            obj.client_port_ref = client_port_ref_value

        # Parse client_port_from
        child = SerializationHelper.find_child_element(element, "CLIENT-PORT-FROM")
        if child is not None:
            client_port_from_value = child.text
            obj.client_port_from = client_port_from_value

        # Parse pdus (list from container "PDUS")
        obj.pdus = []
        container = SerializationHelper.find_child_element(element, "PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pdus.append(child_value)

        # Parse pdu_collection
        child = SerializationHelper.find_child_element(element, "PDU-COLLECTION")
        if child is not None:
            pdu_collection_value = child.text
            obj.pdu_collection = pdu_collection_value

        # Parse runtime_ip
        child = SerializationHelper.find_child_element(element, "RUNTIME-IP")
        if child is not None:
            runtime_ip_value = child.text
            obj.runtime_ip = runtime_ip_value

        # Parse runtime_port
        child = SerializationHelper.find_child_element(element, "RUNTIME-PORT")
        if child is not None:
            runtime_port_value = child.text
            obj.runtime_port = runtime_port_value

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        return obj



class SocketConnectionBuilder:
    """Builder for SocketConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: SocketConnection = SocketConnection()


    def with_admin_data(self, value: Optional[AdminData]) -> "SocketConnectionBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "SocketConnectionBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "SocketConnectionBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "SocketConnectionBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

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


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> SocketConnection:
        """Build and return the SocketConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj