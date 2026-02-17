"""AUTOSAR SignalServiceTranslationControlEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 744)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.enums.json"""

from enum import Enum


class SignalServiceTranslationControlEnum(Enum):
    """AUTOSAR SignalServiceTranslationControlEnum enumeration."""

    ALLPARTIALNETWORKSACTIVE = "allPartialNetworksActive"
    ANYPARTIALNETWORKACTIVE = "anyPartialNetworkActive"
    PARTIALNETWORK = "partialNetwork"
    SERVICEDISCOVERY = "serviceDiscovery"
    TRANSLATIONSTART = "translationStart"
