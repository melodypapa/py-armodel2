"""Ipv4Props AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_arp_props import (
    Ipv4ArpProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_auto_ip_props import (
    Ipv4AutoIpProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_fragmentation_props import (
    Ipv4FragmentationProps,
)


class Ipv4Props(ARObject):
    """AUTOSAR Ipv4Props."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("arp_props", None, False, False, Ipv4ArpProps),  # arpProps
        ("auto_ip_props", None, False, False, Ipv4AutoIpProps),  # autoIpProps
        ("fragmentation", None, False, False, Ipv4FragmentationProps),  # fragmentation
    ]

    def __init__(self) -> None:
        """Initialize Ipv4Props."""
        super().__init__()
        self.arp_props: Optional[Ipv4ArpProps] = None
        self.auto_ip_props: Optional[Ipv4AutoIpProps] = None
        self.fragmentation: Optional[Ipv4FragmentationProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ipv4Props to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4Props":
        """Create Ipv4Props from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ipv4Props instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ipv4Props since parent returns ARObject
        return cast("Ipv4Props", obj)


class Ipv4PropsBuilder:
    """Builder for Ipv4Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4Props = Ipv4Props()

    def build(self) -> Ipv4Props:
        """Build and return Ipv4Props object.

        Returns:
            Ipv4Props instance
        """
        # TODO: Add validation
        return self._obj
