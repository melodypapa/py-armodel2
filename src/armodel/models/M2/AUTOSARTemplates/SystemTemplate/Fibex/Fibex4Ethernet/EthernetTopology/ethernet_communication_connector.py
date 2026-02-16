"""EthernetCommunicationConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("eth_ip_props", None, False, False, EthIpProps),  # ethIpProps
        ("maximum", None, True, False, None),  # maximum
        ("neighbor_cache", None, True, False, None),  # neighborCache
        ("path_mtu", None, True, False, None),  # pathMtu
        ("path_mtu_timeout", None, True, False, None),  # pathMtuTimeout
    ]

    def __init__(self) -> None:
        """Initialize EthernetCommunicationConnector."""
        super().__init__()
        self.eth_ip_props: Optional[EthIpProps] = None
        self.maximum: Optional[PositiveInteger] = None
        self.neighbor_cache: Optional[PositiveInteger] = None
        self.path_mtu: Optional[Boolean] = None
        self.path_mtu_timeout: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthernetCommunicationConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCommunicationConnector":
        """Create EthernetCommunicationConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthernetCommunicationConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthernetCommunicationConnector since parent returns ARObject
        return cast("EthernetCommunicationConnector", obj)


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
