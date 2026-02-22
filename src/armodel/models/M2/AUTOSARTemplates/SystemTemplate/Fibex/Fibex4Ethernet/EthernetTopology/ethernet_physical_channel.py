"""EthernetPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 314)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_ad_config import (
    SoAdConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.vlan_config import (
    VlanConfig,
)


class EthernetPhysicalChannel(PhysicalChannel):
    """AUTOSAR EthernetPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    network_endpoints: list[NetworkEndpoint]
    so_ad_config: Optional[SoAdConfig]
    vlan: Optional[VlanConfig]
    def __init__(self) -> None:
        """Initialize EthernetPhysicalChannel."""
        super().__init__()
        self.network_endpoints: list[NetworkEndpoint] = []
        self.so_ad_config: Optional[SoAdConfig] = None
        self.vlan: Optional[VlanConfig] = None

    def serialize(self) -> ET.Element:
        """Serialize EthernetPhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetPhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize network_endpoints (list to container "NETWORK-ENDPOINTS")
        if self.network_endpoints:
            wrapper = ET.Element("NETWORK-ENDPOINTS")
            for item in self.network_endpoints:
                serialized = SerializationHelper.serialize_item(item, "NetworkEndpoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize so_ad_config
        if self.so_ad_config is not None:
            serialized = SerializationHelper.serialize_item(self.so_ad_config, "SoAdConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SO-AD-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan
        if self.vlan is not None:
            serialized = SerializationHelper.serialize_item(self.vlan, "VlanConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetPhysicalChannel":
        """Deserialize XML element to EthernetPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetPhysicalChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetPhysicalChannel, cls).deserialize(element)

        # Parse network_endpoints (list from container "NETWORK-ENDPOINTS")
        obj.network_endpoints = []
        container = SerializationHelper.find_child_element(element, "NETWORK-ENDPOINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.network_endpoints.append(child_value)

        # Parse so_ad_config
        child = SerializationHelper.find_child_element(element, "SO-AD-CONFIG")
        if child is not None:
            so_ad_config_value = SerializationHelper.deserialize_by_tag(child, "SoAdConfig")
            obj.so_ad_config = so_ad_config_value

        # Parse vlan
        child = SerializationHelper.find_child_element(element, "VLAN")
        if child is not None:
            vlan_value = SerializationHelper.deserialize_by_tag(child, "VlanConfig")
            obj.vlan = vlan_value

        return obj



class EthernetPhysicalChannelBuilder:
    """Builder for EthernetPhysicalChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: EthernetPhysicalChannel = EthernetPhysicalChannel()


    def with_short_name(self, value: Identifier) -> "EthernetPhysicalChannelBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "EthernetPhysicalChannelBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "EthernetPhysicalChannelBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "EthernetPhysicalChannelBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "EthernetPhysicalChannelBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "EthernetPhysicalChannelBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "EthernetPhysicalChannelBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "EthernetPhysicalChannelBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "EthernetPhysicalChannelBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_comm_connectors(self, items: list[CommunicationConnector]) -> "EthernetPhysicalChannelBuilder":
        """Set comm_connectors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.comm_connectors = list(items) if items else []
        return self

    def with_frame_triggerings(self, items: list[FrameTriggering]) -> "EthernetPhysicalChannelBuilder":
        """Set frame_triggerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.frame_triggerings = list(items) if items else []
        return self

    def with_i_signals(self, items: list[ISignalTriggering]) -> "EthernetPhysicalChannelBuilder":
        """Set i_signals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_signals = list(items) if items else []
        return self

    def with_manageds(self, items: list[PhysicalChannel]) -> "EthernetPhysicalChannelBuilder":
        """Set manageds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.manageds = list(items) if items else []
        return self

    def with_pdu_triggerings(self, items: list[PduTriggering]) -> "EthernetPhysicalChannelBuilder":
        """Set pdu_triggerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings = list(items) if items else []
        return self

    def with_network_endpoints(self, items: list[NetworkEndpoint]) -> "EthernetPhysicalChannelBuilder":
        """Set network_endpoints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.network_endpoints = list(items) if items else []
        return self

    def with_so_ad_config(self, value: Optional[SoAdConfig]) -> "EthernetPhysicalChannelBuilder":
        """Set so_ad_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.so_ad_config = value
        return self

    def with_vlan(self, value: Optional[VlanConfig]) -> "EthernetPhysicalChannelBuilder":
        """Set vlan attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vlan = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "EthernetPhysicalChannelBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "EthernetPhysicalChannelBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "EthernetPhysicalChannelBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "EthernetPhysicalChannelBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_comm_connector(self, item: CommunicationConnector) -> "EthernetPhysicalChannelBuilder":
        """Add a single item to comm_connectors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.comm_connectors.append(item)
        return self

    def clear_comm_connectors(self) -> "EthernetPhysicalChannelBuilder":
        """Clear all items from comm_connectors list.

        Returns:
            self for method chaining
        """
        self._obj.comm_connectors = []
        return self

    def add_frame_triggering(self, item: FrameTriggering) -> "EthernetPhysicalChannelBuilder":
        """Add a single item to frame_triggerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.frame_triggerings.append(item)
        return self

    def clear_frame_triggerings(self) -> "EthernetPhysicalChannelBuilder":
        """Clear all items from frame_triggerings list.

        Returns:
            self for method chaining
        """
        self._obj.frame_triggerings = []
        return self

    def add_i_signal(self, item: ISignalTriggering) -> "EthernetPhysicalChannelBuilder":
        """Add a single item to i_signals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_signals.append(item)
        return self

    def clear_i_signals(self) -> "EthernetPhysicalChannelBuilder":
        """Clear all items from i_signals list.

        Returns:
            self for method chaining
        """
        self._obj.i_signals = []
        return self

    def add_managed(self, item: PhysicalChannel) -> "EthernetPhysicalChannelBuilder":
        """Add a single item to manageds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.manageds.append(item)
        return self

    def clear_manageds(self) -> "EthernetPhysicalChannelBuilder":
        """Clear all items from manageds list.

        Returns:
            self for method chaining
        """
        self._obj.manageds = []
        return self

    def add_pdu_triggering(self, item: PduTriggering) -> "EthernetPhysicalChannelBuilder":
        """Add a single item to pdu_triggerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings.append(item)
        return self

    def clear_pdu_triggerings(self) -> "EthernetPhysicalChannelBuilder":
        """Clear all items from pdu_triggerings list.

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings = []
        return self

    def add_network_endpoint(self, item: NetworkEndpoint) -> "EthernetPhysicalChannelBuilder":
        """Add a single item to network_endpoints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.network_endpoints.append(item)
        return self

    def clear_network_endpoints(self) -> "EthernetPhysicalChannelBuilder":
        """Clear all items from network_endpoints list.

        Returns:
            self for method chaining
        """
        self._obj.network_endpoints = []
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


    def build(self) -> EthernetPhysicalChannel:
        """Build and return the EthernetPhysicalChannel instance with validation."""
        self._validate_instance()
        pass
        return self._obj