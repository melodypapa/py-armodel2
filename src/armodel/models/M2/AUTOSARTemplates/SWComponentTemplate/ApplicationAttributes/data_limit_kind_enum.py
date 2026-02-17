"""AUTOSAR DataLimitKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 153)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.enums.json"""

from enum import Enum


class DataLimitKindEnum(Enum):
    """AUTOSAR DataLimitKindEnum enumeration."""

    MAX = "max"
    SOFTWARE = "Software"
    AUTOSAR = "AUTOSAR"
    MIN = "min"
    NONE = "none"
