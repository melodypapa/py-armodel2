"""Ip6AddressString AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 468)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 110)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This is used to specify an IP6 address. Notation: FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF Alternative notations, short-cuts with duplicate colons like ::, etc. or mixtures using colons and dots, are not allowed. Tags: xml.xsd.customType=IP6-ADDRESS-STRING xml.xsd.pattern=[0-9A-Fa-f]{1,4}(:[0-9A-Fa-f]{1,4}){7,7}|ANY xml.xsd.type=string Table 6.143: Ip6AddressString In addition, infrastructure services may be provided or consumed by the Network- Endpoints. Identifiable NetworkEndpoint TimeSynchronization TimeSyncClientConfiguration + fullyQualifiedDomainName: String [0..1] + timeSyncTechnology: TimeSyncTechnologyEnum [0..1] + priority: PositiveInteger [0..1] 0..* +orderedMaster {ordered} +infrastructureServices 0..1 OrderedMaster InfrastructureServices + index: PositiveInteger [0..1] +timeSyncServer 0..1 Referrable +timeSyncServer TimeSyncServerConfiguration 0..1 + priority: PositiveInteger [0..1] + syncInterval: TimeValue [0..1] + timeSyncServerIdentifier: String [0..1] + timeSyncTechnology: TimeSyncTechnologyEnum [0..1] +doIpEntity DoIpEntity 0..1 + doIpEntityRole: DoIpEntityRoleEnum [0..1] «enumeration» TimeSyncTechnologyEnum «enumeration» DoIpEntityRoleEnum ntp_rfc958 ptp_ieee1588_2002 node ptp_ieee1588_2008 gateway avb_ieee802_1AS edgeNode noitazinorhcnySemit+ +timeSyncClient 0..1 0..1 Figure 6.40: Network Endpoint Infrastructure Services 468 of 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11
class Ip6AddressString(ARPrimitive):
    """AUTOSAR Ip6AddressString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize Ip6AddressString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
