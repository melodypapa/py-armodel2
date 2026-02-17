"""AUTOSAR J1939NmAddressConfigurationCapabilityEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 692)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.enums.json"""

from enum import Enum


class J1939NmAddressConfigurationCapabilityEnum(Enum):
    """AUTOSAR J1939NmAddressConfigurationCapabilityEnum enumeration."""

    J1939NM_AAC = "J1939NM_AAC"
    J1939NM_CCA = "J1939NM_CCA"
    J1939NM_NCA = "J1939NM_NCA"
    J1939NM_SCA = "J1939NM_SCA"
    J1939NM_SVCA = "J1939NM_SVCA"
