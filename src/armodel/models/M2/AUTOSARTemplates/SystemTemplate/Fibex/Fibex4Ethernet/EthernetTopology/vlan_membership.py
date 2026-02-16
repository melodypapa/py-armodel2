"""VlanMembership AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class VlanMembership(ARObject):
    """AUTOSAR VlanMembership."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_priority", None, True, False, None),  # defaultPriority
        ("dhcp_address", None, False, False, any (DhcpServer)),  # dhcpAddress
        ("send_activity", None, False, False, any (EthernetSwitchVlan)),  # sendActivity
        ("vlan", None, False, False, any (EthernetPhysical)),  # vlan
    ]

    def __init__(self) -> None:
        """Initialize VlanMembership."""
        super().__init__()
        self.default_priority: Optional[PositiveInteger] = None
        self.dhcp_address: Optional[Any] = None
        self.send_activity: Optional[Any] = None
        self.vlan: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert VlanMembership to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VlanMembership":
        """Create VlanMembership from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            VlanMembership instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to VlanMembership since parent returns ARObject
        return cast("VlanMembership", obj)


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
