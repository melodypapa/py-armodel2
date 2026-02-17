"""HttpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 461)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
    UriString,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_tp import (
    TcpTp,
)


class HttpTp(TransportProtocolConfiguration):
    """AUTOSAR HttpTp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "content_type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # contentType
        "protocol_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # protocolVersion
        "request_method_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (RequestMethodEnum),
        ),  # requestMethodEnum
        "tcp_tp_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TcpTp,
        ),  # tcpTpConfig
        "uri": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # uri
    }

    def __init__(self) -> None:
        """Initialize HttpTp."""
        super().__init__()
        self.content_type: Optional[String] = None
        self.protocol_version: Optional[String] = None
        self.request_method_enum: Optional[Any] = None
        self.tcp_tp_config: Optional[TcpTp] = None
        self.uri: Optional[UriString] = None


class HttpTpBuilder:
    """Builder for HttpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HttpTp = HttpTp()

    def build(self) -> HttpTp:
        """Build and return HttpTp object.

        Returns:
            HttpTp instance
        """
        # TODO: Add validation
        return self._obj
