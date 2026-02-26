"""AUTOSAR ServiceVersionAcceptanceKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2056)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ServiceVersionAcceptanceKindEnum(AREnum):
    """AUTOSAR ServiceVersionAcceptanceKindEnum enumeration.

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

    EXACT_OR_ANY_MINOR = "EXACT-OR-ANY-MINOR"
    SYSTEM = "SYSTEM"
    AUTOSAR = "A-U-T-O-S-A-R"
    MINIMUM_MINOR = "MINIMUM-MINOR"
