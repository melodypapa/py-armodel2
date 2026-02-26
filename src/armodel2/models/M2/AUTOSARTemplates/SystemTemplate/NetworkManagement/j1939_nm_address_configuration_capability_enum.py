"""AUTOSAR J1939NmAddressConfigurationCapabilityEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 692)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class J1939NmAddressConfigurationCapabilityEnum(AREnum):
    """AUTOSAR J1939NmAddressConfigurationCapabilityEnum enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

    J1939_NM_AAC = "J1939-N-M_-A-A-C"
    J1939_NM_CCA = "J1939-N-M_-C-C-A"
    J1939_NM_NCA = "J1939-N-M_-N-C-A"
    J1939_NM_SCA = "J1939-N-M_-S-C-A"
    J1939_NM_SVCA = "J1939-N-M_-S-V-C-A"
