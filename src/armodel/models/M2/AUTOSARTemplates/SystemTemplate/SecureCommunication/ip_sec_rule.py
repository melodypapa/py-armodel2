"""IPSecRule AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)


class IPSecRule(Identifiable):
    """AUTOSAR IPSecRule."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("direction", None, False, False, any (Communication)),  # direction
        ("header_type", None, False, False, IPsecHeaderTypeEnum),  # headerType
        ("ip_protocol", None, False, False, IPsecIpProtocolEnum),  # ipProtocol
        ("local_certificates", None, False, True, any (CryptoService)),  # localCertificates
        ("local_id", None, True, False, None),  # localId
        ("local_port_range", None, True, False, None),  # localPortRange
        ("mode", None, False, False, IPsecModeEnum),  # mode
        ("policy", None, False, False, IPsecPolicyEnum),  # policy
        ("pre_shared_key", None, False, False, CryptoServiceKey),  # preSharedKey
        ("priority", None, True, False, None),  # priority
        ("remotes", None, False, True, any (CryptoService)),  # remotes
        ("remote_id", None, True, False, None),  # remoteId
        ("remote_ips", None, False, True, NetworkEndpoint),  # remoteIps
        ("remote_port", None, True, False, None),  # remotePort
    ]

    def __init__(self) -> None:
        """Initialize IPSecRule."""
        super().__init__()
        self.direction: Optional[Any] = None
        self.header_type: Optional[IPsecHeaderTypeEnum] = None
        self.ip_protocol: Optional[IPsecIpProtocolEnum] = None
        self.local_certificates: list[Any] = []
        self.local_id: Optional[String] = None
        self.local_port_range: Optional[PositiveInteger] = None
        self.mode: Optional[IPsecModeEnum] = None
        self.policy: Optional[IPsecPolicyEnum] = None
        self.pre_shared_key: Optional[CryptoServiceKey] = None
        self.priority: Optional[PositiveInteger] = None
        self.remotes: list[Any] = []
        self.remote_id: Optional[String] = None
        self.remote_ips: list[NetworkEndpoint] = []
        self.remote_port: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IPSecRule to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPSecRule":
        """Create IPSecRule from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IPSecRule instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IPSecRule since parent returns ARObject
        return cast("IPSecRule", obj)


class IPSecRuleBuilder:
    """Builder for IPSecRule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPSecRule = IPSecRule()

    def build(self) -> IPSecRule:
        """Build and return IPSecRule object.

        Returns:
            IPSecRule instance
        """
        # TODO: Add validation
        return self._obj
