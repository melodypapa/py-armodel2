"""IPSecRule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 571)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    IPsecHeaderTypeEnum,
    IPsecIpProtocolEnum,
    IPsecModeEnum,
    IPsecPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
        NetworkEndpoint,
    )



class IPSecRule(Identifiable):
    """AUTOSAR IPSecRule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    direction: Optional[Any]
    header_type: Optional[IPsecHeaderTypeEnum]
    ip_protocol: Optional[IPsecIpProtocolEnum]
    local_certificates: list[Any]
    local_id: Optional[String]
    local_port_range: Optional[PositiveInteger]
    mode: Optional[IPsecModeEnum]
    policy: Optional[IPsecPolicyEnum]
    pre_shared_key: Optional[CryptoServiceKey]
    priority: Optional[PositiveInteger]
    remotes: list[Any]
    remote_id: Optional[String]
    remote_ips: list[NetworkEndpoint]
    remote_port: Optional[PositiveInteger]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPSecRule":
        """Deserialize XML element to IPSecRule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPSecRule object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse direction
        child = ARObject._find_child_element(element, "DIRECTION")
        if child is not None:
            direction_value = child.text
            obj.direction = direction_value

        # Parse header_type
        child = ARObject._find_child_element(element, "HEADER-TYPE")
        if child is not None:
            header_type_value = child.text
            obj.header_type = header_type_value

        # Parse ip_protocol
        child = ARObject._find_child_element(element, "IP-PROTOCOL")
        if child is not None:
            ip_protocol_value = child.text
            obj.ip_protocol = ip_protocol_value

        # Parse local_certificates (list)
        obj.local_certificates = []
        for child in ARObject._find_all_child_elements(element, "LOCAL-CERTIFICATES"):
            local_certificates_value = child.text
            obj.local_certificates.append(local_certificates_value)

        # Parse local_id
        child = ARObject._find_child_element(element, "LOCAL-ID")
        if child is not None:
            local_id_value = child.text
            obj.local_id = local_id_value

        # Parse local_port_range
        child = ARObject._find_child_element(element, "LOCAL-PORT-RANGE")
        if child is not None:
            local_port_range_value = child.text
            obj.local_port_range = local_port_range_value

        # Parse mode
        child = ARObject._find_child_element(element, "MODE")
        if child is not None:
            mode_value = child.text
            obj.mode = mode_value

        # Parse policy
        child = ARObject._find_child_element(element, "POLICY")
        if child is not None:
            policy_value = child.text
            obj.policy = policy_value

        # Parse pre_shared_key
        child = ARObject._find_child_element(element, "PRE-SHARED-KEY")
        if child is not None:
            pre_shared_key_value = ARObject._deserialize_by_tag(child, "CryptoServiceKey")
            obj.pre_shared_key = pre_shared_key_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse remotes (list)
        obj.remotes = []
        for child in ARObject._find_all_child_elements(element, "REMOTES"):
            remotes_value = child.text
            obj.remotes.append(remotes_value)

        # Parse remote_id
        child = ARObject._find_child_element(element, "REMOTE-ID")
        if child is not None:
            remote_id_value = child.text
            obj.remote_id = remote_id_value

        # Parse remote_ips (list)
        obj.remote_ips = []
        for child in ARObject._find_all_child_elements(element, "REMOTE-IPS"):
            remote_ips_value = ARObject._deserialize_by_tag(child, "NetworkEndpoint")
            obj.remote_ips.append(remote_ips_value)

        # Parse remote_port
        child = ARObject._find_child_element(element, "REMOTE-PORT")
        if child is not None:
            remote_port_value = child.text
            obj.remote_port = remote_port_value

        return obj



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
