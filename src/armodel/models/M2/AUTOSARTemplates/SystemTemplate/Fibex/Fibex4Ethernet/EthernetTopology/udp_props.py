"""UdpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 154)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class UdpProps(ARObject):
    """AUTOSAR UdpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    udp_ttl: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize UdpProps."""
        super().__init__()
        self.udp_ttl: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UdpProps":
        """Deserialize XML element to UdpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UdpProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse udp_ttl
        child = ARObject._find_child_element(element, "UDP-TTL")
        if child is not None:
            udp_ttl_value = child.text
            obj.udp_ttl = udp_ttl_value

        return obj



class UdpPropsBuilder:
    """Builder for UdpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpProps = UdpProps()

    def build(self) -> UdpProps:
        """Build and return UdpProps object.

        Returns:
            UdpProps instance
        """
        # TODO: Add validation
        return self._obj
