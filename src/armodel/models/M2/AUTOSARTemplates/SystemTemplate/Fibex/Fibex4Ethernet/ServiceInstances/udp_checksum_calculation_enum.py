"""AUTOSAR UdpChecksumCalculationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 454)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.enums.json"""

from enum import Enum


class UdpChecksumCalculationEnum(Enum):
    """AUTOSAR UdpChecksumCalculationEnum enumeration."""

    UDPCHECKSUMDISABLED = "udpChecksumDisabled"
    UDPCHECKSUMENABLED = "udpChecksumEnabled"
