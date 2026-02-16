"""SignalServiceTranslationControlEnum enumeration."""

from enum import Enum


class SignalServiceTranslationControlEnum(Enum):
    """AUTOSAR SignalServiceTranslationControlEnum enumeration."""

    ALLPARTIALNETWORKSACTIVE = "allPartialNetworksActive"
    ANYPARTIALNETWORKACTIVE = "anyPartialNetworkActive"
    PARTIALNETWORK = "partialNetwork"
    SERVICEDISCOVERY = "serviceDiscovery"
    TRANSLATIONSTART = "translationStart"
