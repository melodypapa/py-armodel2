"""Ipv6FragmentationProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class Ipv6FragmentationProps(ARObject):
    """AUTOSAR Ipv6FragmentationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_ip_ip", None, True, False, None),  # tcpIpIp
        ("tcp_ip_ip_reassembly_buffer_size", None, True, False, None),  # tcpIpIpReassemblyBufferSize
        ("tcp_ip_ip_tx", None, True, False, None),  # tcpIpIpTx
        ("tcp_ip_ip_tx_fragment_buffer_size", None, True, False, None),  # tcpIpIpTxFragmentBufferSize
    ]

    def __init__(self) -> None:
        """Initialize Ipv6FragmentationProps."""
        super().__init__()
        self.tcp_ip_ip: Optional[TimeValue] = None
        self.tcp_ip_ip_reassembly_buffer_size: Optional[PositiveInteger] = None
        self.tcp_ip_ip_tx: Optional[PositiveInteger] = None
        self.tcp_ip_ip_tx_fragment_buffer_size: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ipv6FragmentationProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6FragmentationProps":
        """Create Ipv6FragmentationProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ipv6FragmentationProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ipv6FragmentationProps since parent returns ARObject
        return cast("Ipv6FragmentationProps", obj)


class Ipv6FragmentationPropsBuilder:
    """Builder for Ipv6FragmentationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv6FragmentationProps = Ipv6FragmentationProps()

    def build(self) -> Ipv6FragmentationProps:
        """Build and return Ipv6FragmentationProps object.

        Returns:
            Ipv6FragmentationProps instance
        """
        # TODO: Add validation
        return self._obj
