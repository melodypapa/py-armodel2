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
