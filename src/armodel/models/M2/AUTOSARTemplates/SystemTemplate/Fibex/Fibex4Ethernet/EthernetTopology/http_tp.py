"""HttpTp AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("content_type", None, True, False, None),  # contentType
        ("protocol_version", None, True, False, None),  # protocolVersion
        ("request_method_enum", None, False, False, any (RequestMethodEnum)),  # requestMethodEnum
        ("tcp_tp_config", None, False, False, TcpTp),  # tcpTpConfig
        ("uri", None, True, False, None),  # uri
    ]

    def __init__(self) -> None:
        """Initialize HttpTp."""
        super().__init__()
        self.content_type: Optional[String] = None
        self.protocol_version: Optional[String] = None
        self.request_method_enum: Optional[Any] = None
        self.tcp_tp_config: Optional[TcpTp] = None
        self.uri: Optional[UriString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HttpTp to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HttpTp":
        """Create HttpTp from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HttpTp instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HttpTp since parent returns ARObject
        return cast("HttpTp", obj)


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
