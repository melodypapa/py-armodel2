"""EthernetCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetMacLayerTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    MacAddressString,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


@atp_variant()

class EthernetCommunicationController(ARObject):
    """AUTOSAR EthernetCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    can_xl_config_ref: Optional[Any]
    coupling_ports: list[CouplingPort]
    mac_layer_type: Optional[EthernetMacLayerTypeEnum]
    mac_unicast: Optional[MacAddressString]
    maximum: Optional[Integer]
    slave_act_as: Optional[Boolean]
    slave_qualified: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize EthernetCommunicationController."""
        super().__init__()
        self.can_xl_config_ref: Optional[Any] = None
        self.coupling_ports: list[CouplingPort] = []
        self.mac_layer_type: Optional[EthernetMacLayerTypeEnum] = None
        self.mac_unicast: Optional[MacAddressString] = None
        self.maximum: Optional[Integer] = None
        self.slave_act_as: Optional[Boolean] = None
        self.slave_qualified: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize EthernetCommunicationController to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetCommunicationController, self).serialize()

        # Copy all attributes from parent element to outer element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to outer element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Copy parent's children: metadata to outer element, others to inner element
        metadata_tags = {'SHORT-NAME', 'LONG-NAME', 'DESC', 'ADMIN-DATA'}
        for child in parent_elem:
            tag = SerializationHelper.strip_namespace(child.tag)
            if tag in metadata_tags:
                # Metadata elements stay outside the atp_variant wrapper
                elem.append(child)
            else:
                # Other elements go inside the atp_variant wrapper
                inner_elem.append(child)

        # Serialize can_xl_config_ref
        if self.can_xl_config_ref is not None:
            serialized = SerializationHelper.serialize_item(self.can_xl_config_ref, "Any")
            if serialized is not None:
                wrapped = ET.Element("CAN-XL-CONFIG-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize coupling_ports (list from container "COUPLING-PORTS")
        if self.coupling_ports:
            container = ET.Element("COUPLING-PORTS")
            for item in self.coupling_ports:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("CouplingPort", package_data):
                    # Simple primitive type
                    child = ET.Element("COUPLING-PORT")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("CouplingPort", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize mac_layer_type
        if self.mac_layer_type is not None:
            serialized = SerializationHelper.serialize_item(self.mac_layer_type, "EthernetMacLayerTypeEnum")
            if serialized is not None:
                wrapped = ET.Element("MAC-LAYER-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize mac_unicast
        if self.mac_unicast is not None:
            serialized = SerializationHelper.serialize_item(self.mac_unicast, "MacAddressString")
            if serialized is not None:
                wrapped = ET.Element("MAC-UNICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize maximum
        if self.maximum is not None:
            serialized = SerializationHelper.serialize_item(self.maximum, "Integer")
            if serialized is not None:
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize slave_act_as
        if self.slave_act_as is not None:
            serialized = SerializationHelper.serialize_item(self.slave_act_as, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("SLAVE-ACT-AS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize slave_qualified
        if self.slave_qualified is not None:
            serialized = SerializationHelper.serialize_item(self.slave_qualified, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("SLAVE-QUALIFIED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "EthernetCommunicationController")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCommunicationController":
        """Deserialize XML element to EthernetCommunicationController object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetCommunicationController object
        """
        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "EthernetCommunicationController")
        if inner_elem is None:
            # No wrapper structure found, create instance with default values
            obj = cls.__new__(cls)
            obj.__init__()
            return obj

        # Temporarily copy children from inner element to outer element
        # so parent's deserialize can find inherited attributes
        for child in list(inner_elem):
            element.append(child)

        # Call parent's deserialize with outer element (now contains parent's children)
        obj = super(EthernetCommunicationController, cls).deserialize(element)

        # Clean up: remove the temporarily copied children from outer element
        # (they are now in obj, so we don't need them in element anymore)
        for child in list(inner_elem):
            element.remove(child)

        # Parse can_xl_config_ref
        child = SerializationHelper.find_child_element(inner_elem, "CAN-XL-CONFIG-REF")
        if child is not None:
            can_xl_config_ref_value = ARRef.deserialize(child)
            obj.can_xl_config_ref = can_xl_config_ref_value

        # Parse coupling_ports (list from container "COUPLING-PORTS")
        obj.coupling_ports = []
        container = SerializationHelper.find_child_element(inner_elem, "COUPLING-PORTS")
        if container is not None:
            for child in container:
                if is_ref:
                    # Use the child_tag from decorator if specified to match specific child tag
                    if child_tag:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag == "None":
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                    else:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("CouplingPort", package_data):
                    child_value = child.text
                elif is_enum_type("CouplingPort", package_data):
                    child_value = CouplingPort.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.coupling_ports.append(child_value)

        # Parse mac_layer_type
        child = SerializationHelper.find_child_element(inner_elem, "MAC-LAYER-TYPE")
        if child is not None:
            mac_layer_type_value = EthernetMacLayerTypeEnum.deserialize(child)
            obj.mac_layer_type = mac_layer_type_value

        # Parse mac_unicast
        child = SerializationHelper.find_child_element(inner_elem, "MAC-UNICAST")
        if child is not None:
            mac_unicast_value = child.text
            obj.mac_unicast = mac_unicast_value

        # Parse maximum
        child = SerializationHelper.find_child_element(inner_elem, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        # Parse slave_act_as
        child = SerializationHelper.find_child_element(inner_elem, "SLAVE-ACT-AS")
        if child is not None:
            slave_act_as_value = child.text
            obj.slave_act_as = slave_act_as_value

        # Parse slave_qualified
        child = SerializationHelper.find_child_element(inner_elem, "SLAVE-QUALIFIED")
        if child is not None:
            slave_qualified_value = child.text
            obj.slave_qualified = slave_qualified_value

        return obj



class EthernetCommunicationControllerBuilder(BuilderBase):
    """Builder for EthernetCommunicationController with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthernetCommunicationController = EthernetCommunicationController()


    def with_can_xl_config(self, value: Optional[any (AbstractCan)]) -> "EthernetCommunicationControllerBuilder":
        """Set can_xl_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.can_xl_config = value
        return self

    def with_coupling_ports(self, items: list[CouplingPort]) -> "EthernetCommunicationControllerBuilder":
        """Set coupling_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.coupling_ports = list(items) if items else []
        return self

    def with_mac_layer_type(self, value: Optional[EthernetMacLayerTypeEnum]) -> "EthernetCommunicationControllerBuilder":
        """Set mac_layer_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mac_layer_type = value
        return self

    def with_mac_unicast(self, value: Optional[MacAddressString]) -> "EthernetCommunicationControllerBuilder":
        """Set mac_unicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mac_unicast = value
        return self

    def with_maximum(self, value: Optional[Integer]) -> "EthernetCommunicationControllerBuilder":
        """Set maximum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum = value
        return self

    def with_slave_act_as(self, value: Optional[Boolean]) -> "EthernetCommunicationControllerBuilder":
        """Set slave_act_as attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.slave_act_as = value
        return self

    def with_slave_qualified(self, value: Optional[TimeValue]) -> "EthernetCommunicationControllerBuilder":
        """Set slave_qualified attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.slave_qualified = value
        return self


    def add_coupling_port(self, item: CouplingPort) -> "EthernetCommunicationControllerBuilder":
        """Add a single item to coupling_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.coupling_ports.append(item)
        return self

    def clear_coupling_ports(self) -> "EthernetCommunicationControllerBuilder":
        """Clear all items from coupling_ports list.

        Returns:
            self for method chaining
        """
        self._obj.coupling_ports = []
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


    def build(self) -> EthernetCommunicationController:
        """Build and return the EthernetCommunicationController instance with validation."""
        self._validate_instance()
        pass
        return self._obj