"""StreamFilterIpv4Address AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
)


class StreamFilterIpv4Address(ARObject):
    """AUTOSAR StreamFilterIpv4Address."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ipv4_address: Optional[Ip4AddressString]
    def __init__(self) -> None:
        """Initialize StreamFilterIpv4Address."""
        super().__init__()
        self.ipv4_address: Optional[Ip4AddressString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterIpv4Address":
        """Deserialize XML element to StreamFilterIpv4Address object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterIpv4Address object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ipv4_address
        child = ARObject._find_child_element(element, "IPV4-ADDRESS")
        if child is not None:
            ipv4_address_value = child.text
            obj.ipv4_address = ipv4_address_value

        return obj



class StreamFilterIpv4AddressBuilder:
    """Builder for StreamFilterIpv4Address."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterIpv4Address = StreamFilterIpv4Address()

    def build(self) -> StreamFilterIpv4Address:
        """Build and return StreamFilterIpv4Address object.

        Returns:
            StreamFilterIpv4Address instance
        """
        # TODO: Add validation
        return self._obj
