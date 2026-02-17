"""AUTOSAR EcucScopeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 46)

JSON Source: packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.enums.json"""

from enum import Enum


class EcucScopeEnum(Enum):
    """AUTOSAR EcucScopeEnum enumeration."""

    ECU = "ECU"
    LOCAL = "local"
