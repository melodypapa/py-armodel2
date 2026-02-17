"""AUTOSAR EthGlobalTimeMessageFormatEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 868)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.enums.json"""

from enum import Enum


class EthGlobalTimeMessageFormatEnum(Enum):
    """AUTOSAR EthGlobalTimeMessageFormatEnum enumeration."""

    IEEE802_1AS = "IEEE802_1AS"
    IEEE802_1AS_AUTOSAR = "IEEE802_1AS_AUTOSAR"
