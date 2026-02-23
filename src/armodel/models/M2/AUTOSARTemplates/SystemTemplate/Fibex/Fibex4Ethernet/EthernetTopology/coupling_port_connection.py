"""CouplingPortConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 112)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class CouplingPortConnection(ARObject):
    """AUTOSAR CouplingPortConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_port_ref: Optional[ARRef]
    node_port_refs: list[ARRef]
    plca_local_node: Optional[PositiveInteger]
    plca_transmit: Optional[PositiveInteger]
    second_port_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize CouplingPortConnection."""
        super().__init__()
        self.first_port_ref: Optional[ARRef] = None
        self.node_port_refs: list[ARRef] = []
        self.plca_local_node: Optional[PositiveInteger] = None
        self.plca_transmit: Optional[PositiveInteger] = None
        self.second_port_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_port_ref
        if self.first_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_port_ref, "CouplingPort")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize node_port_refs (list to container "NODE-PORT-REFS")
        if self.node_port_refs:
            wrapper = ET.Element("NODE-PORT-REFS")
            for item in self.node_port_refs:
                serialized = SerializationHelper.serialize_item(item, "CouplingPort")
                if serialized is not None:
                    child_elem = ET.Element("NODE-PORT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize plca_local_node
        if self.plca_local_node is not None:
            serialized = SerializationHelper.serialize_item(self.plca_local_node, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PLCA-LOCAL-NODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize plca_transmit
        if self.plca_transmit is not None:
            serialized = SerializationHelper.serialize_item(self.plca_transmit, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PLCA-TRANSMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_port_ref
        if self.second_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_port_ref, "CouplingPort")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortConnection":
        """Deserialize XML element to CouplingPortConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortConnection, cls).deserialize(element)

        # Parse first_port_ref
        child = SerializationHelper.find_child_element(element, "FIRST-PORT-REF")
        if child is not None:
            first_port_ref_value = ARRef.deserialize(child)
            obj.first_port_ref = first_port_ref_value

        # Parse node_port_refs (list from container "NODE-PORT-REFS")
        obj.node_port_refs = []
        container = SerializationHelper.find_child_element(element, "NODE-PORT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.node_port_refs.append(child_value)

        # Parse plca_local_node
        child = SerializationHelper.find_child_element(element, "PLCA-LOCAL-NODE")
        if child is not None:
            plca_local_node_value = child.text
            obj.plca_local_node = plca_local_node_value

        # Parse plca_transmit
        child = SerializationHelper.find_child_element(element, "PLCA-TRANSMIT")
        if child is not None:
            plca_transmit_value = child.text
            obj.plca_transmit = plca_transmit_value

        # Parse second_port_ref
        child = SerializationHelper.find_child_element(element, "SECOND-PORT-REF")
        if child is not None:
            second_port_ref_value = ARRef.deserialize(child)
            obj.second_port_ref = second_port_ref_value

        return obj



class CouplingPortConnectionBuilder:
    """Builder for CouplingPortConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: CouplingPortConnection = CouplingPortConnection()


    def with_first_port(self, value: Optional[CouplingPort]) -> "CouplingPortConnectionBuilder":
        """Set first_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.first_port = value
        return self

    def with_node_ports(self, items: list[CouplingPort]) -> "CouplingPortConnectionBuilder":
        """Set node_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.node_ports = list(items) if items else []
        return self

    def with_plca_local_node(self, value: Optional[PositiveInteger]) -> "CouplingPortConnectionBuilder":
        """Set plca_local_node attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.plca_local_node = value
        return self

    def with_plca_transmit(self, value: Optional[PositiveInteger]) -> "CouplingPortConnectionBuilder":
        """Set plca_transmit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.plca_transmit = value
        return self

    def with_second_port(self, value: Optional[CouplingPort]) -> "CouplingPortConnectionBuilder":
        """Set second_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.second_port = value
        return self


    def add_node_port(self, item: CouplingPort) -> "CouplingPortConnectionBuilder":
        """Add a single item to node_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.node_ports.append(item)
        return self

    def clear_node_ports(self) -> "CouplingPortConnectionBuilder":
        """Clear all items from node_ports list.

        Returns:
            self for method chaining
        """
        self._obj.node_ports = []
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


    def build(self) -> CouplingPortConnection:
        """Build and return the CouplingPortConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj