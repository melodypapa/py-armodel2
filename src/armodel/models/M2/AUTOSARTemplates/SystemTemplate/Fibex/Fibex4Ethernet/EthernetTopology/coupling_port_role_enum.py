"""CouplingPortRoleEnum enumeration."""

from enum import Enum


class CouplingPortRoleEnum(Enum):
    """AUTOSAR CouplingPortRoleEnum enumeration."""

    HOSTPORTELEMENT = "hostPortElement"
    STANDARDPORTUPLINKPORT = "standardPortupLinkPort"
    ECU = "ECU"
