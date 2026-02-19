"""Ipv4DhcpServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    TimeValue,
)


class Ipv4DhcpServerConfiguration(Describable):
    """AUTOSAR Ipv4DhcpServerConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    address_range: Optional[Ip4AddressString]
    default_gateway: Optional[Ip4AddressString]
    default_lease: Optional[TimeValue]
    dns_servers: list[Ip4AddressString]
    network_mask: Optional[Ip4AddressString]
    def __init__(self) -> None:
        """Initialize Ipv4DhcpServerConfiguration."""
        super().__init__()
        self.address_range: Optional[Ip4AddressString] = None
        self.default_gateway: Optional[Ip4AddressString] = None
        self.default_lease: Optional[TimeValue] = None
        self.dns_servers: list[Ip4AddressString] = []
        self.network_mask: Optional[Ip4AddressString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4DhcpServerConfiguration":
        """Deserialize XML element to Ipv4DhcpServerConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4DhcpServerConfiguration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse address_range
        child = ARObject._find_child_element(element, "ADDRESS-RANGE")
        if child is not None:
            address_range_value = child.text
            obj.address_range = address_range_value

        # Parse default_gateway
        child = ARObject._find_child_element(element, "DEFAULT-GATEWAY")
        if child is not None:
            default_gateway_value = child.text
            obj.default_gateway = default_gateway_value

        # Parse default_lease
        child = ARObject._find_child_element(element, "DEFAULT-LEASE")
        if child is not None:
            default_lease_value = child.text
            obj.default_lease = default_lease_value

        # Parse dns_servers (list)
        obj.dns_servers = []
        for child in ARObject._find_all_child_elements(element, "DNS-SERVERS"):
            dns_servers_value = child.text
            obj.dns_servers.append(dns_servers_value)

        # Parse network_mask
        child = ARObject._find_child_element(element, "NETWORK-MASK")
        if child is not None:
            network_mask_value = child.text
            obj.network_mask = network_mask_value

        return obj



class Ipv4DhcpServerConfigurationBuilder:
    """Builder for Ipv4DhcpServerConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4DhcpServerConfiguration = Ipv4DhcpServerConfiguration()

    def build(self) -> Ipv4DhcpServerConfiguration:
        """Build and return Ipv4DhcpServerConfiguration object.

        Returns:
            Ipv4DhcpServerConfiguration instance
        """
        # TODO: Add validation
        return self._obj
