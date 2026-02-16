"""Ipv4FragmentationProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class Ipv4FragmentationProps(ARObject):
    """AUTOSAR Ipv4FragmentationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_ip_ip", None, True, False, None),  # tcpIpIp
        ("tcp_ip_ip_num", None, True, False, None),  # tcpIpIpNum
        ("tcp_ip_ip_reass", None, True, False, None),  # tcpIpIpReass
    ]

    def __init__(self) -> None:
        """Initialize Ipv4FragmentationProps."""
        super().__init__()
        self.tcp_ip_ip: Optional[Boolean] = None
        self.tcp_ip_ip_num: Optional[PositiveInteger] = None
        self.tcp_ip_ip_reass: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ipv4FragmentationProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4FragmentationProps":
        """Create Ipv4FragmentationProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ipv4FragmentationProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ipv4FragmentationProps since parent returns ARObject
        return cast("Ipv4FragmentationProps", obj)


class Ipv4FragmentationPropsBuilder:
    """Builder for Ipv4FragmentationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4FragmentationProps = Ipv4FragmentationProps()

    def build(self) -> Ipv4FragmentationProps:
        """Build and return Ipv4FragmentationProps object.

        Returns:
            Ipv4FragmentationProps instance
        """
        # TODO: Add validation
        return self._obj
