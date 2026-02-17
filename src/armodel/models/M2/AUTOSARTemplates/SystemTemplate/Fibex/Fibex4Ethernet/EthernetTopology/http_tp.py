"""HttpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 461)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

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
