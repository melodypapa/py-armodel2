"""VlanMembership AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class VlanMembership(ARObject):
    """AUTOSAR VlanMembership."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_priority: Optional[PositiveInteger]
    dhcp_address: Optional[Any]
    send_activity: Optional[Any]
    vlan: Optional[Any]
    def __init__(self) -> None:
        """Initialize VlanMembership."""
        super().__init__()
        self.default_priority: Optional[PositiveInteger] = None
        self.dhcp_address: Optional[Any] = None
        self.send_activity: Optional[Any] = None
        self.vlan: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize VlanMembership to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize default_priority
        if self.default_priority is not None:
            serialized = ARObject._serialize_item(self.default_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dhcp_address
        if self.dhcp_address is not None:
            serialized = ARObject._serialize_item(self.dhcp_address, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DHCP-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize send_activity
        if self.send_activity is not None:
            serialized = ARObject._serialize_item(self.send_activity, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEND-ACTIVITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan
        if self.vlan is not None:
            serialized = ARObject._serialize_item(self.vlan, "Any")
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
    def deserialize(cls, element: ET.Element) -> "VlanMembership":
        """Deserialize XML element to VlanMembership object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VlanMembership object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse default_priority
        child = ARObject._find_child_element(element, "DEFAULT-PRIORITY")
        if child is not None:
            default_priority_value = child.text
            obj.default_priority = default_priority_value

        # Parse dhcp_address
        child = ARObject._find_child_element(element, "DHCP-ADDRESS")
        if child is not None:
            dhcp_address_value = child.text
            obj.dhcp_address = dhcp_address_value

        # Parse send_activity
        child = ARObject._find_child_element(element, "SEND-ACTIVITY")
        if child is not None:
            send_activity_value = child.text
            obj.send_activity = send_activity_value

        # Parse vlan
        child = ARObject._find_child_element(element, "VLAN")
        if child is not None:
            vlan_value = child.text
            obj.vlan = vlan_value

        return obj



class VlanMembershipBuilder:
    """Builder for VlanMembership."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VlanMembership = VlanMembership()

    def build(self) -> VlanMembership:
        """Build and return VlanMembership object.

        Returns:
            VlanMembership instance
        """
        # TODO: Add validation
        return self._obj
