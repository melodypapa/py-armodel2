"""EthernetCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 117)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.eth_ip_props import (
    EthIpProps,
)


class EthernetCommunicationConnector(CommunicationConnector):
    """AUTOSAR EthernetCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    eth_ip_props: Optional[EthIpProps]
    maximum: Optional[PositiveInteger]
    neighbor_cache: Optional[PositiveInteger]
    path_mtu: Optional[Boolean]
    path_mtu_timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize EthernetCommunicationConnector."""
        super().__init__()
        self.eth_ip_props: Optional[EthIpProps] = None
        self.maximum: Optional[PositiveInteger] = None
        self.neighbor_cache: Optional[PositiveInteger] = None
        self.path_mtu: Optional[Boolean] = None
        self.path_mtu_timeout: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCommunicationConnector":
        """Deserialize XML element to EthernetCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetCommunicationConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse eth_ip_props
        child = ARObject._find_child_element(element, "ETH-IP-PROPS")
        if child is not None:
            eth_ip_props_value = ARObject._deserialize_by_tag(child, "EthIpProps")
            obj.eth_ip_props = eth_ip_props_value

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        # Parse neighbor_cache
        child = ARObject._find_child_element(element, "NEIGHBOR-CACHE")
        if child is not None:
            neighbor_cache_value = child.text
            obj.neighbor_cache = neighbor_cache_value

        # Parse path_mtu
        child = ARObject._find_child_element(element, "PATH-MTU")
        if child is not None:
            path_mtu_value = child.text
            obj.path_mtu = path_mtu_value

        # Parse path_mtu_timeout
        child = ARObject._find_child_element(element, "PATH-MTU-TIMEOUT")
        if child is not None:
            path_mtu_timeout_value = child.text
            obj.path_mtu_timeout = path_mtu_timeout_value

        return obj



class EthernetCommunicationConnectorBuilder:
    """Builder for EthernetCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetCommunicationConnector = EthernetCommunicationConnector()

    def build(self) -> EthernetCommunicationConnector:
        """Build and return EthernetCommunicationConnector object.

        Returns:
            EthernetCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
