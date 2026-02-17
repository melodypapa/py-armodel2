"""AUTOSAR DataIdModeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 807)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.enums.json"""

from enum import Enum


class DataIdModeEnum(Enum):
    """AUTOSAR DataIdModeEnum enumeration."""

    ALL16BIT = "all16Bit"
    ALTERNATING8BITCOUNTER = "alternating8Bitcounter"
    LOWER12BIT = "lower12Bit"
    LOWER8BITARE = "lower8Bitare"
