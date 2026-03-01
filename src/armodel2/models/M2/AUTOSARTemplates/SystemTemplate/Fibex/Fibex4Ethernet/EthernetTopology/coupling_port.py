"""CouplingPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortRoleEnum,
    EthernetConnectionNegotiationEnum,
    EthernetMacLayerTypeEnum,
    EthernetPhysicalLayerTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_details import (
    CouplingPortDetails,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_props import (
    MacSecProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.plca_props import (
    PlcaProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
    PncMappingIdent,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.vlan_membership import (
    VlanMembership,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CouplingPort(Identifiable):
    """AUTOSAR CouplingPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COUPLING-PORT"


    connection: Optional[EthernetConnectionNegotiationEnum]
    coupling_port_details: Optional[CouplingPortDetails]
    coupling_port_role_enum: Optional[CouplingPortRoleEnum]
    default_vlan_ref: Optional[Any]
    mac_layer_type_enum: Optional[EthernetMacLayerTypeEnum]
    mac_multicast_group_refs: list[ARRef]
    mac_sec_propses: list[MacSecProps]
    physical_layer: Optional[EthernetPhysicalLayerTypeEnum]
    plca_props: Optional[PlcaProps]
    pnc_mapping_ident_refs: list[ARRef]
    receive_activity: Optional[Any]
    vlans: list[VlanMembership]
    vlan_modifier_ref: Optional[Any]
    wakeup_sleep_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "CONNECTION": lambda obj, elem: setattr(obj, "connection", EthernetConnectionNegotiationEnum.deserialize(elem)),
        "COUPLING-PORT-DETAILS": lambda obj, elem: setattr(obj, "coupling_port_details", SerializationHelper.deserialize_by_tag(elem, "CouplingPortDetails")),
        "COUPLING-PORT-ROLE-ENUM": lambda obj, elem: setattr(obj, "coupling_port_role_enum", CouplingPortRoleEnum.deserialize(elem)),
        "DEFAULT-VLAN-REF": lambda obj, elem: setattr(obj, "default_vlan_ref", ARRef.deserialize(elem)),
        "MAC-LAYER-TYPE-ENUM": lambda obj, elem: setattr(obj, "mac_layer_type_enum", EthernetMacLayerTypeEnum.deserialize(elem)),
        "MAC-MULTICAST-GROUPS": lambda obj, elem: obj.mac_multicast_group_refs.append(ARRef.deserialize(elem)),
        "MAC-SEC-PROPSES": lambda obj, elem: obj.mac_sec_propses.append(SerializationHelper.deserialize_by_tag(elem, "MacSecProps")),
        "PHYSICAL-LAYER": lambda obj, elem: setattr(obj, "physical_layer", EthernetPhysicalLayerTypeEnum.deserialize(elem)),
        "PLCA-PROPS": lambda obj, elem: setattr(obj, "plca_props", SerializationHelper.deserialize_by_tag(elem, "PlcaProps")),
        "PNC-MAPPING-IDENTS": lambda obj, elem: obj.pnc_mapping_ident_refs.append(ARRef.deserialize(elem)),
        "RECEIVE-ACTIVITY": lambda obj, elem: setattr(obj, "receive_activity", SerializationHelper.deserialize_by_tag(elem, "any (EthernetSwitchVlan)")),
        "VLANS": lambda obj, elem: obj.vlans.append(SerializationHelper.deserialize_by_tag(elem, "VlanMembership")),
        "VLAN-MODIFIER-REF": lambda obj, elem: setattr(obj, "vlan_modifier_ref", ARRef.deserialize(elem)),
        "WAKEUP-SLEEP-REF": lambda obj, elem: setattr(obj, "wakeup_sleep_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CouplingPort."""
        super().__init__()
        self.connection: Optional[EthernetConnectionNegotiationEnum] = None
        self.coupling_port_details: Optional[CouplingPortDetails] = None
        self.coupling_port_role_enum: Optional[CouplingPortRoleEnum] = None
        self.default_vlan_ref: Optional[Any] = None
        self.mac_layer_type_enum: Optional[EthernetMacLayerTypeEnum] = None
        self.mac_multicast_group_refs: list[ARRef] = []
        self.mac_sec_propses: list[MacSecProps] = []
        self.physical_layer: Optional[EthernetPhysicalLayerTypeEnum] = None
        self.plca_props: Optional[PlcaProps] = None
        self.pnc_mapping_ident_refs: list[ARRef] = []
        self.receive_activity: Optional[Any] = None
        self.vlans: list[VlanMembership] = []
        self.vlan_modifier_ref: Optional[Any] = None
        self.wakeup_sleep_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize CouplingPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connection
        if self.connection is not None:
            serialized = SerializationHelper.serialize_item(self.connection, "EthernetConnectionNegotiationEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize coupling_port_details
        if self.coupling_port_details is not None:
            serialized = SerializationHelper.serialize_item(self.coupling_port_details, "CouplingPortDetails")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUPLING-PORT-DETAILS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize coupling_port_role_enum
        if self.coupling_port_role_enum is not None:
            serialized = SerializationHelper.serialize_item(self.coupling_port_role_enum, "CouplingPortRoleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUPLING-PORT-ROLE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default_vlan_ref
        if self.default_vlan_ref is not None:
            serialized = SerializationHelper.serialize_item(self.default_vlan_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VLAN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mac_layer_type_enum
        if self.mac_layer_type_enum is not None:
            serialized = SerializationHelper.serialize_item(self.mac_layer_type_enum, "EthernetMacLayerTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAC-LAYER-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mac_multicast_group_refs (list to container "MAC-MULTICAST-GROUP-REFS")
        if self.mac_multicast_group_refs:
            wrapper = ET.Element("MAC-MULTICAST-GROUP-REFS")
            for item in self.mac_multicast_group_refs:
                serialized = SerializationHelper.serialize_item(item, "MacMulticastGroup")
                if serialized is not None:
                    child_elem = ET.Element("MAC-MULTICAST-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mac_sec_propses (list to container "MAC-SEC-PROPSES")
        if self.mac_sec_propses:
            wrapper = ET.Element("MAC-SEC-PROPSES")
            for item in self.mac_sec_propses:
                serialized = SerializationHelper.serialize_item(item, "MacSecProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_layer
        if self.physical_layer is not None:
            serialized = SerializationHelper.serialize_item(self.physical_layer, "EthernetPhysicalLayerTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-LAYER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize plca_props
        if self.plca_props is not None:
            serialized = SerializationHelper.serialize_item(self.plca_props, "PlcaProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PLCA-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_mapping_ident_refs (list to container "PNC-MAPPING-IDENT-REFS")
        if self.pnc_mapping_ident_refs:
            wrapper = ET.Element("PNC-MAPPING-IDENT-REFS")
            for item in self.pnc_mapping_ident_refs:
                serialized = SerializationHelper.serialize_item(item, "PncMappingIdent")
                if serialized is not None:
                    child_elem = ET.Element("PNC-MAPPING-IDENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize receive_activity
        if self.receive_activity is not None:
            serialized = SerializationHelper.serialize_item(self.receive_activity, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RECEIVE-ACTIVITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlans (list to container "VLANS")
        if self.vlans:
            wrapper = ET.Element("VLANS")
            for item in self.vlans:
                serialized = SerializationHelper.serialize_item(item, "VlanMembership")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize vlan_modifier_ref
        if self.vlan_modifier_ref is not None:
            serialized = SerializationHelper.serialize_item(self.vlan_modifier_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN-MODIFIER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup_sleep_ref
        if self.wakeup_sleep_ref is not None:
            serialized = SerializationHelper.serialize_item(self.wakeup_sleep_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP-SLEEP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPort":
        """Deserialize XML element to CouplingPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPort, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONNECTION":
                setattr(obj, "connection", EthernetConnectionNegotiationEnum.deserialize(child))
            elif tag == "COUPLING-PORT-DETAILS":
                setattr(obj, "coupling_port_details", SerializationHelper.deserialize_by_tag(child, "CouplingPortDetails"))
            elif tag == "COUPLING-PORT-ROLE-ENUM":
                setattr(obj, "coupling_port_role_enum", CouplingPortRoleEnum.deserialize(child))
            elif tag == "DEFAULT-VLAN-REF":
                setattr(obj, "default_vlan_ref", ARRef.deserialize(child))
            elif tag == "MAC-LAYER-TYPE-ENUM":
                setattr(obj, "mac_layer_type_enum", EthernetMacLayerTypeEnum.deserialize(child))
            elif tag == "MAC-MULTICAST-GROUPS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mac_multicast_group_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "MacMulticastGroup"))
            elif tag == "MAC-SEC-PROPSES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mac_sec_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "MacSecProps"))
            elif tag == "PHYSICAL-LAYER":
                setattr(obj, "physical_layer", EthernetPhysicalLayerTypeEnum.deserialize(child))
            elif tag == "PLCA-PROPS":
                setattr(obj, "plca_props", SerializationHelper.deserialize_by_tag(child, "PlcaProps"))
            elif tag == "PNC-MAPPING-IDENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.pnc_mapping_ident_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "PncMappingIdent"))
            elif tag == "RECEIVE-ACTIVITY":
                setattr(obj, "receive_activity", SerializationHelper.deserialize_by_tag(child, "any (EthernetSwitchVlan)"))
            elif tag == "VLANS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.vlans.append(SerializationHelper.deserialize_by_tag(item_elem, "VlanMembership"))
            elif tag == "VLAN-MODIFIER-REF":
                setattr(obj, "vlan_modifier_ref", ARRef.deserialize(child))
            elif tag == "WAKEUP-SLEEP-REF":
                setattr(obj, "wakeup_sleep_ref", ARRef.deserialize(child))

        return obj



class CouplingPortBuilder(IdentifiableBuilder):
    """Builder for CouplingPort with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CouplingPort = CouplingPort()


    def with_connection(self, value: Optional[EthernetConnectionNegotiationEnum]) -> "CouplingPortBuilder":
        """Set connection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.connection = value
        return self

    def with_coupling_port_details(self, value: Optional[CouplingPortDetails]) -> "CouplingPortBuilder":
        """Set coupling_port_details attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.coupling_port_details = value
        return self

    def with_coupling_port_role_enum(self, value: Optional[CouplingPortRoleEnum]) -> "CouplingPortBuilder":
        """Set coupling_port_role_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.coupling_port_role_enum = value
        return self

    def with_default_vlan(self, value: Optional[any (EthernetPhysical)]) -> "CouplingPortBuilder":
        """Set default_vlan attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_vlan = value
        return self

    def with_mac_layer_type_enum(self, value: Optional[EthernetMacLayerTypeEnum]) -> "CouplingPortBuilder":
        """Set mac_layer_type_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mac_layer_type_enum = value
        return self

    def with_mac_multicast_groups(self, items: list[MacMulticastGroup]) -> "CouplingPortBuilder":
        """Set mac_multicast_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mac_multicast_groups = list(items) if items else []
        return self

    def with_mac_sec_propses(self, items: list[MacSecProps]) -> "CouplingPortBuilder":
        """Set mac_sec_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mac_sec_propses = list(items) if items else []
        return self

    def with_physical_layer(self, value: Optional[EthernetPhysicalLayerTypeEnum]) -> "CouplingPortBuilder":
        """Set physical_layer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.physical_layer = value
        return self

    def with_plca_props(self, value: Optional[PlcaProps]) -> "CouplingPortBuilder":
        """Set plca_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.plca_props = value
        return self

    def with_pnc_mapping_idents(self, items: list[PncMappingIdent]) -> "CouplingPortBuilder":
        """Set pnc_mapping_idents list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pnc_mapping_idents = list(items) if items else []
        return self

    def with_receive_activity(self, value: Optional[any (EthernetSwitchVlan)]) -> "CouplingPortBuilder":
        """Set receive_activity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.receive_activity = value
        return self

    def with_vlans(self, items: list[VlanMembership]) -> "CouplingPortBuilder":
        """Set vlans list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.vlans = list(items) if items else []
        return self

    def with_vlan_modifier(self, value: Optional[any (EthernetPhysical)]) -> "CouplingPortBuilder":
        """Set vlan_modifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vlan_modifier = value
        return self

    def with_wakeup_sleep(self, value: Optional[any (EthernetWakeupSleep)]) -> "CouplingPortBuilder":
        """Set wakeup_sleep attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wakeup_sleep = value
        return self


    def add_mac_multicast_group(self, item: MacMulticastGroup) -> "CouplingPortBuilder":
        """Add a single item to mac_multicast_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mac_multicast_groups.append(item)
        return self

    def clear_mac_multicast_groups(self) -> "CouplingPortBuilder":
        """Clear all items from mac_multicast_groups list.

        Returns:
            self for method chaining
        """
        self._obj.mac_multicast_groups = []
        return self

    def add_mac_sec_props(self, item: MacSecProps) -> "CouplingPortBuilder":
        """Add a single item to mac_sec_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mac_sec_propses.append(item)
        return self

    def clear_mac_sec_propses(self) -> "CouplingPortBuilder":
        """Clear all items from mac_sec_propses list.

        Returns:
            self for method chaining
        """
        self._obj.mac_sec_propses = []
        return self

    def add_pnc_mapping_ident(self, item: PncMappingIdent) -> "CouplingPortBuilder":
        """Add a single item to pnc_mapping_idents list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pnc_mapping_idents.append(item)
        return self

    def clear_pnc_mapping_idents(self) -> "CouplingPortBuilder":
        """Clear all items from pnc_mapping_idents list.

        Returns:
            self for method chaining
        """
        self._obj.pnc_mapping_idents = []
        return self

    def add_vlan(self, item: VlanMembership) -> "CouplingPortBuilder":
        """Add a single item to vlans list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.vlans.append(item)
        return self

    def clear_vlans(self) -> "CouplingPortBuilder":
        """Clear all items from vlans list.

        Returns:
            self for method chaining
        """
        self._obj.vlans = []
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


    def build(self) -> CouplingPort:
        """Build and return the CouplingPort instance with validation."""
        self._validate_instance()
        pass
        return self._obj