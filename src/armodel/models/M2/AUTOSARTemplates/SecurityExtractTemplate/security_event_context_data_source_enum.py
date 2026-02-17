"""AUTOSAR SecurityEventContextDataSourceEnum enumeration.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 25)

JSON Source: packages/M2_AUTOSARTemplates_SecurityExtractTemplate.enums.json"""

from enum import Enum


class SecurityEventContextDataSourceEnum(Enum):
    """AUTOSAR SecurityEventContextDataSourceEnum enumeration."""

    USEFIRSTCONTEXTDATA = "useFirstContextData"
    USELASTCONTEXTDATA = "useLastContextData"
