"""CommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 54)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    PncGatewayTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_controller import (
    CommunicationController,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CommunicationConnector(Identifiable, ABC):
    """AUTOSAR CommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    comm_controller_ref: Optional[ARRef]
    create_ecu_wakeup_source: Optional[Boolean]
    dynamic_pnc_to_channel_mapping_enabled: Optional[Boolean]
    ecu_comm_port_instances: list[CommConnectorPort]
    pnc_filter_array_masks: list[PositiveInteger]
    pnc_gateway_type: Optional[PncGatewayTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "COMM-CONTROLLER-REF": ("_POLYMORPHIC", "comm_controller_ref", ["AbstractCanCommunicationController", "EthernetCommunicationController", "FlexrayCommunicationController", "LinCommunicationController", "UserDefinedCommunicationController"]),
        "CREATE-ECU-WAKEUP-SOURCE": lambda obj, elem: setattr(obj, "create_ecu_wakeup_source", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED": lambda obj, elem: setattr(obj, "dynamic_pnc_to_channel_mapping_enabled", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "ECU-COMM-PORT-INSTANCES": ("_POLYMORPHIC_LIST", "ecu_comm_port_instances", ["FramePort", "IPduPort", "ISignalPort"]),
        "PNC-FILTER-ARRAY-MASKS": lambda obj, elem: obj.pnc_filter_array_masks.append(SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PNC-GATEWAY-TYPE": lambda obj, elem: setattr(obj, "pnc_gateway_type", PncGatewayTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CommunicationConnector."""
        super().__init__()
        self.comm_controller_ref: Optional[ARRef] = None
        self.create_ecu_wakeup_source: Optional[Boolean] = None
        self.dynamic_pnc_to_channel_mapping_enabled: Optional[Boolean] = None
        self.ecu_comm_port_instances: list[CommConnectorPort] = []
        self.pnc_filter_array_masks: list[PositiveInteger] = []
        self.pnc_gateway_type: Optional[PncGatewayTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommunicationConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize comm_controller_ref
        if self.comm_controller_ref is not None:
            serialized = SerializationHelper.serialize_item(self.comm_controller_ref, "CommunicationController")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMM-CONTROLLER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize create_ecu_wakeup_source
        if self.create_ecu_wakeup_source is not None:
            serialized = SerializationHelper.serialize_item(self.create_ecu_wakeup_source, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CREATE-ECU-WAKEUP-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dynamic_pnc_to_channel_mapping_enabled
        if self.dynamic_pnc_to_channel_mapping_enabled is not None:
            serialized = SerializationHelper.serialize_item(self.dynamic_pnc_to_channel_mapping_enabled, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_comm_port_instances (list to container "ECU-COMM-PORT-INSTANCES")
        if self.ecu_comm_port_instances:
            wrapper = ET.Element("ECU-COMM-PORT-INSTANCES")
            for item in self.ecu_comm_port_instances:
                serialized = SerializationHelper.serialize_item(item, "CommConnectorPort")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_filter_array_masks (list to container "PNC-FILTER-ARRAY-MASKS")
        if self.pnc_filter_array_masks:
            wrapper = ET.Element("PNC-FILTER-ARRAY-MASKS")
            for item in self.pnc_filter_array_masks:
                serialized = SerializationHelper.serialize_item(item, "PositiveInteger")
                if serialized is not None:
                    child_elem = ET.Element("PNC-FILTER-ARRAY-MASK")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_gateway_type
        if self.pnc_gateway_type is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_gateway_type, "PncGatewayTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-GATEWAY-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationConnector":
        """Deserialize XML element to CommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommunicationConnector, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "COMM-CONTROLLER-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-CAN-COMMUNICATION-CONTROLLER":
                        setattr(obj, "comm_controller_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractCanCommunicationController"))
                    elif concrete_tag == "ETHERNET-COMMUNICATION-CONTROLLER":
                        setattr(obj, "comm_controller_ref", SerializationHelper.deserialize_by_tag(child[0], "EthernetCommunicationController"))
                    elif concrete_tag == "FLEXRAY-COMMUNICATION-CONTROLLER":
                        setattr(obj, "comm_controller_ref", SerializationHelper.deserialize_by_tag(child[0], "FlexrayCommunicationController"))
                    elif concrete_tag == "LIN-COMMUNICATION-CONTROLLER":
                        setattr(obj, "comm_controller_ref", SerializationHelper.deserialize_by_tag(child[0], "LinCommunicationController"))
                    elif concrete_tag == "USER-DEFINED-COMMUNICATION-CONTROLLER":
                        setattr(obj, "comm_controller_ref", SerializationHelper.deserialize_by_tag(child[0], "UserDefinedCommunicationController"))
            elif tag == "CREATE-ECU-WAKEUP-SOURCE":
                setattr(obj, "create_ecu_wakeup_source", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED":
                setattr(obj, "dynamic_pnc_to_channel_mapping_enabled", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "ECU-COMM-PORT-INSTANCES":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "FRAME-PORT":
                        obj.ecu_comm_port_instances.append(SerializationHelper.deserialize_by_tag(child[0], "FramePort"))
                    elif concrete_tag == "I-PDU-PORT":
                        obj.ecu_comm_port_instances.append(SerializationHelper.deserialize_by_tag(child[0], "IPduPort"))
                    elif concrete_tag == "I-SIGNAL-PORT":
                        obj.ecu_comm_port_instances.append(SerializationHelper.deserialize_by_tag(child[0], "ISignalPort"))
            elif tag == "PNC-FILTER-ARRAY-MASKS":
                obj.pnc_filter_array_masks.append(SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PNC-GATEWAY-TYPE":
                setattr(obj, "pnc_gateway_type", PncGatewayTypeEnum.deserialize(child))

        return obj



class CommunicationConnectorBuilder(IdentifiableBuilder):
    """Builder for CommunicationConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CommunicationConnector = CommunicationConnector()


    def with_comm_controller(self, value: Optional[CommunicationController]) -> "CommunicationConnectorBuilder":
        """Set comm_controller attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.comm_controller = value
        return self

    def with_create_ecu_wakeup_source(self, value: Optional[Boolean]) -> "CommunicationConnectorBuilder":
        """Set create_ecu_wakeup_source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.create_ecu_wakeup_source = value
        return self

    def with_dynamic_pnc_to_channel_mapping_enabled(self, value: Optional[Boolean]) -> "CommunicationConnectorBuilder":
        """Set dynamic_pnc_to_channel_mapping_enabled attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamic_pnc_to_channel_mapping_enabled = value
        return self

    def with_ecu_comm_port_instances(self, items: list[CommConnectorPort]) -> "CommunicationConnectorBuilder":
        """Set ecu_comm_port_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecu_comm_port_instances = list(items) if items else []
        return self

    def with_pnc_filter_array_masks(self, items: list[PositiveInteger]) -> "CommunicationConnectorBuilder":
        """Set pnc_filter_array_masks list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pnc_filter_array_masks = list(items) if items else []
        return self

    def with_pnc_gateway_type(self, value: Optional[PncGatewayTypeEnum]) -> "CommunicationConnectorBuilder":
        """Set pnc_gateway_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_gateway_type = value
        return self


    def add_ecu_comm_port_instance(self, item: CommConnectorPort) -> "CommunicationConnectorBuilder":
        """Add a single item to ecu_comm_port_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecu_comm_port_instances.append(item)
        return self

    def clear_ecu_comm_port_instances(self) -> "CommunicationConnectorBuilder":
        """Clear all items from ecu_comm_port_instances list.

        Returns:
            self for method chaining
        """
        self._obj.ecu_comm_port_instances = []
        return self

    def add_pnc_filter_array_mask(self, item: PositiveInteger) -> "CommunicationConnectorBuilder":
        """Add a single item to pnc_filter_array_masks list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pnc_filter_array_masks.append(item)
        return self

    def clear_pnc_filter_array_masks(self) -> "CommunicationConnectorBuilder":
        """Clear all items from pnc_filter_array_masks list.

        Returns:
            self for method chaining
        """
        self._obj.pnc_filter_array_masks = []
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
    def build(self) -> CommunicationConnector:
        """Build and return the CommunicationConnector instance (abstract)."""
        raise NotImplementedError