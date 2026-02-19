"""Ipv6Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 147)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dhcp_props: Optional[Dhcpv6Props]
    fragmentation: Optional[Ipv6FragmentationProps]
    ndp_props: Optional[Ipv6NdpProps]
    def __init__(self) -> None:
        """Initialize Ipv6Props."""
        super().__init__()
        self.dhcp_props: Optional[Dhcpv6Props] = None
        self.fragmentation: Optional[Ipv6FragmentationProps] = None
        self.ndp_props: Optional[Ipv6NdpProps] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6Props":
        """Deserialize XML element to Ipv6Props object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv6Props object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dhcp_props
        child = ARObject._find_child_element(element, "DHCP-PROPS")
        if child is not None:
            dhcp_props_value = ARObject._deserialize_by_tag(child, "Dhcpv6Props")
            obj.dhcp_props = dhcp_props_value

        # Parse fragmentation
        child = ARObject._find_child_element(element, "FRAGMENTATION")
        if child is not None:
            fragmentation_value = ARObject._deserialize_by_tag(child, "Ipv6FragmentationProps")
            obj.fragmentation = fragmentation_value

        # Parse ndp_props
        child = ARObject._find_child_element(element, "NDP-PROPS")
        if child is not None:
            ndp_props_value = ARObject._deserialize_by_tag(child, "Ipv6NdpProps")
            obj.ndp_props = ndp_props_value

        return obj



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
