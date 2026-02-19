"""CouplingPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortRoleEnum,
    EthernetConnectionNegotiationEnum,
    EthernetMacLayerTypeEnum,
    EthernetPhysicalLayerTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_details import (
    CouplingPortDetails,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_props import (
    MacSecProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.plca_props import (
    PlcaProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
    PncMappingIdent,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.vlan_membership import (
    VlanMembership,
)


class CouplingPort(Identifiable):
    """AUTOSAR CouplingPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connection: Optional[EthernetConnectionNegotiationEnum]
    coupling_port_details: Optional[CouplingPortDetails]
    coupling_port_role_enum: Optional[CouplingPortRoleEnum]
    default_vlan: Optional[Any]
    mac_layer_type_enum: Optional[EthernetMacLayerTypeEnum]
    mac_multicast_group_refs: list[ARRef]
    mac_sec_propses: list[MacSecProps]
    physical_layer: Optional[EthernetPhysicalLayerTypeEnum]
    plca_props: Optional[PlcaProps]
    pnc_mapping_ident_refs: list[ARRef]
    receive_activity: Optional[Any]
    vlans: list[VlanMembership]
    vlan_modifier: Optional[Any]
    wakeup_sleep: Optional[Any]
    def __init__(self) -> None:
        """Initialize CouplingPort."""
        super().__init__()
        self.connection: Optional[EthernetConnectionNegotiationEnum] = None
        self.coupling_port_details: Optional[CouplingPortDetails] = None
        self.coupling_port_role_enum: Optional[CouplingPortRoleEnum] = None
        self.default_vlan: Optional[Any] = None
        self.mac_layer_type_enum: Optional[EthernetMacLayerTypeEnum] = None
        self.mac_multicast_group_refs: list[ARRef] = []
        self.mac_sec_propses: list[MacSecProps] = []
        self.physical_layer: Optional[EthernetPhysicalLayerTypeEnum] = None
        self.plca_props: Optional[PlcaProps] = None
        self.pnc_mapping_ident_refs: list[ARRef] = []
        self.receive_activity: Optional[Any] = None
        self.vlans: list[VlanMembership] = []
        self.vlan_modifier: Optional[Any] = None
        self.wakeup_sleep: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize CouplingPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connection
        if self.connection is not None:
            serialized = ARObject._serialize_item(self.connection, "EthernetConnectionNegotiationEnum")
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
            serialized = ARObject._serialize_item(self.coupling_port_details, "CouplingPortDetails")
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
            serialized = ARObject._serialize_item(self.coupling_port_role_enum, "CouplingPortRoleEnum")
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

        # Serialize default_vlan
        if self.default_vlan is not None:
            serialized = ARObject._serialize_item(self.default_vlan, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VLAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mac_layer_type_enum
        if self.mac_layer_type_enum is not None:
            serialized = ARObject._serialize_item(self.mac_layer_type_enum, "EthernetMacLayerTypeEnum")
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

        # Serialize mac_multicast_group_refs (list to container "MAC-MULTICAST-GROUPS")
        if self.mac_multicast_group_refs:
            wrapper = ET.Element("MAC-MULTICAST-GROUPS")
            for item in self.mac_multicast_group_refs:
                serialized = ARObject._serialize_item(item, "MacMulticastGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mac_sec_propses (list to container "MAC-SEC-PROPSES")
        if self.mac_sec_propses:
            wrapper = ET.Element("MAC-SEC-PROPSES")
            for item in self.mac_sec_propses:
                serialized = ARObject._serialize_item(item, "MacSecProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_layer
        if self.physical_layer is not None:
            serialized = ARObject._serialize_item(self.physical_layer, "EthernetPhysicalLayerTypeEnum")
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
            serialized = ARObject._serialize_item(self.plca_props, "PlcaProps")
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

        # Serialize pnc_mapping_ident_refs (list to container "PNC-MAPPING-IDENTS")
        if self.pnc_mapping_ident_refs:
            wrapper = ET.Element("PNC-MAPPING-IDENTS")
            for item in self.pnc_mapping_ident_refs:
                serialized = ARObject._serialize_item(item, "PncMappingIdent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize receive_activity
        if self.receive_activity is not None:
            serialized = ARObject._serialize_item(self.receive_activity, "Any")
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
                serialized = ARObject._serialize_item(item, "VlanMembership")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize vlan_modifier
        if self.vlan_modifier is not None:
            serialized = ARObject._serialize_item(self.vlan_modifier, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN-MODIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup_sleep
        if self.wakeup_sleep is not None:
            serialized = ARObject._serialize_item(self.wakeup_sleep, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP-SLEEP")
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

        # Parse connection
        child = ARObject._find_child_element(element, "CONNECTION")
        if child is not None:
            connection_value = EthernetConnectionNegotiationEnum.deserialize(child)
            obj.connection = connection_value

        # Parse coupling_port_details
        child = ARObject._find_child_element(element, "COUPLING-PORT-DETAILS")
        if child is not None:
            coupling_port_details_value = ARObject._deserialize_by_tag(child, "CouplingPortDetails")
            obj.coupling_port_details = coupling_port_details_value

        # Parse coupling_port_role_enum
        child = ARObject._find_child_element(element, "COUPLING-PORT-ROLE-ENUM")
        if child is not None:
            coupling_port_role_enum_value = CouplingPortRoleEnum.deserialize(child)
            obj.coupling_port_role_enum = coupling_port_role_enum_value

        # Parse default_vlan
        child = ARObject._find_child_element(element, "DEFAULT-VLAN")
        if child is not None:
            default_vlan_value = child.text
            obj.default_vlan = default_vlan_value

        # Parse mac_layer_type_enum
        child = ARObject._find_child_element(element, "MAC-LAYER-TYPE-ENUM")
        if child is not None:
            mac_layer_type_enum_value = EthernetMacLayerTypeEnum.deserialize(child)
            obj.mac_layer_type_enum = mac_layer_type_enum_value

        # Parse mac_multicast_group_refs (list from container "MAC-MULTICAST-GROUPS")
        obj.mac_multicast_group_refs = []
        container = ARObject._find_child_element(element, "MAC-MULTICAST-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mac_multicast_group_refs.append(child_value)

        # Parse mac_sec_propses (list from container "MAC-SEC-PROPSES")
        obj.mac_sec_propses = []
        container = ARObject._find_child_element(element, "MAC-SEC-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mac_sec_propses.append(child_value)

        # Parse physical_layer
        child = ARObject._find_child_element(element, "PHYSICAL-LAYER")
        if child is not None:
            physical_layer_value = EthernetPhysicalLayerTypeEnum.deserialize(child)
            obj.physical_layer = physical_layer_value

        # Parse plca_props
        child = ARObject._find_child_element(element, "PLCA-PROPS")
        if child is not None:
            plca_props_value = ARObject._deserialize_by_tag(child, "PlcaProps")
            obj.plca_props = plca_props_value

        # Parse pnc_mapping_ident_refs (list from container "PNC-MAPPING-IDENTS")
        obj.pnc_mapping_ident_refs = []
        container = ARObject._find_child_element(element, "PNC-MAPPING-IDENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_mapping_ident_refs.append(child_value)

        # Parse receive_activity
        child = ARObject._find_child_element(element, "RECEIVE-ACTIVITY")
        if child is not None:
            receive_activity_value = child.text
            obj.receive_activity = receive_activity_value

        # Parse vlans (list from container "VLANS")
        obj.vlans = []
        container = ARObject._find_child_element(element, "VLANS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.vlans.append(child_value)

        # Parse vlan_modifier
        child = ARObject._find_child_element(element, "VLAN-MODIFIER")
        if child is not None:
            vlan_modifier_value = child.text
            obj.vlan_modifier = vlan_modifier_value

        # Parse wakeup_sleep
        child = ARObject._find_child_element(element, "WAKEUP-SLEEP")
        if child is not None:
            wakeup_sleep_value = child.text
            obj.wakeup_sleep = wakeup_sleep_value

        return obj



class CouplingPortBuilder:
    """Builder for CouplingPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPort = CouplingPort()

    def build(self) -> CouplingPort:
        """Build and return CouplingPort object.

        Returns:
            CouplingPort instance
        """
        # TODO: Add validation
        return self._obj
