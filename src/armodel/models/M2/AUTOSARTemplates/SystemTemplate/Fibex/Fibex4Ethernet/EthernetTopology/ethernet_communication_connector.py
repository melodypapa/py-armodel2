"""EthernetCommunicationConnector AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "eth_ip_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EthIpProps,
        ),  # ethIpProps
        "maximum": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maximum
        "neighbor_cache": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # neighborCache
        "path_mtu": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pathMtu
        "path_mtu_timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pathMtuTimeout
    }

    def __init__(self) -> None:
        """Initialize EthernetCommunicationConnector."""
        super().__init__()
        self.eth_ip_props: Optional[EthIpProps] = None
        self.maximum: Optional[PositiveInteger] = None
        self.neighbor_cache: Optional[PositiveInteger] = None
        self.path_mtu: Optional[Boolean] = None
        self.path_mtu_timeout: Optional[TimeValue] = None


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
