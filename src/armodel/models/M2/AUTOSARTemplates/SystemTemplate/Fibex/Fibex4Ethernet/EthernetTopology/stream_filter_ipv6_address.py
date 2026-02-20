"""StreamFilterIpv6Address AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip6AddressString,
)


class StreamFilterIpv6Address(ARObject):
    """AUTOSAR StreamFilterIpv6Address."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ipv6_address: Optional[Ip6AddressString]
    def __init__(self) -> None:
        """Initialize StreamFilterIpv6Address."""
        super().__init__()
        self.ipv6_address: Optional[Ip6AddressString] = None

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterIpv6Address to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize ipv6_address
        if self.ipv6_address is not None:
            serialized = ARObject._serialize_item(self.ipv6_address, "Ip6AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV6-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterIpv6Address":
        """Deserialize XML element to StreamFilterIpv6Address object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterIpv6Address object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ipv6_address
        child = ARObject._find_child_element(element, "IPV6-ADDRESS")
        if child is not None:
            ipv6_address_value = child.text
            obj.ipv6_address = ipv6_address_value

        return obj



class StreamFilterIpv6AddressBuilder:
    """Builder for StreamFilterIpv6Address."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterIpv6Address = StreamFilterIpv6Address()

    def build(self) -> StreamFilterIpv6Address:
        """Build and return StreamFilterIpv6Address object.

        Returns:
            StreamFilterIpv6Address instance
        """
        # TODO: Add validation
        return self._obj
