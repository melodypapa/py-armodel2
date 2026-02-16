"""Ipv6Props AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.dhcpv6_props import (
    Dhcpv6Props,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_fragmentation_props import (
    Ipv6FragmentationProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_ndp_props import (
    Ipv6NdpProps,
)


class Ipv6Props(ARObject):
    """AUTOSAR Ipv6Props."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dhcp_props", None, False, False, Dhcpv6Props),  # dhcpProps
        ("fragmentation", None, False, False, Ipv6FragmentationProps),  # fragmentation
        ("ndp_props", None, False, False, Ipv6NdpProps),  # ndpProps
    ]

    def __init__(self) -> None:
        """Initialize Ipv6Props."""
        super().__init__()
        self.dhcp_props: Optional[Dhcpv6Props] = None
        self.fragmentation: Optional[Ipv6FragmentationProps] = None
        self.ndp_props: Optional[Ipv6NdpProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ipv6Props to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6Props":
        """Create Ipv6Props from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ipv6Props instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ipv6Props since parent returns ARObject
        return cast("Ipv6Props", obj)


class Ipv6PropsBuilder:
    """Builder for Ipv6Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv6Props = Ipv6Props()

    def build(self) -> Ipv6Props:
        """Build and return Ipv6Props object.

        Returns:
            Ipv6Props instance
        """
        # TODO: Add validation
        return self._obj
