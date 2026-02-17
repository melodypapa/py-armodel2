"""AUTOSAR PncGatewayTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 55)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.enums.json"""

from enum import Enum


class PncGatewayTypeEnum(Enum):
    """AUTOSAR PncGatewayTypeEnum enumeration."""

    ACTIVE = "active"
    NONE = "none"
    PASSIVE = "passive"
