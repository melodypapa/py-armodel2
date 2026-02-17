"""AUTOSAR ContainerIPduHeaderTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 355)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from enum import Enum


class ContainerIPduHeaderTypeEnum(Enum):
    """AUTOSAR ContainerIPduHeaderTypeEnum enumeration."""

    LONGHEADER = "longHeader"
    NOHEADER = "noHeader"
    SHORTHEADER = "shortHeader"
