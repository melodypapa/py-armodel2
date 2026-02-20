"""AUTOSAR SecurityEventReportingModeEnum enumeration.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 35)

JSON Source: packages/M2_AUTOSARTemplates_SecurityExtractTemplate.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class SecurityEventReportingModeEnum(AREnum):
    """AUTOSAR SecurityEventReportingModeEnum enumeration.

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

    BRIEF = "BRIEF"
    BRIEF_BYPASSING = "BRIEF-BYPASSING"
    DETAILED = "DETAILED"
    SECURITY = "SECURITY"
    AUTOSAR = "A-U-T-O-S-A-R"
    DETAILED_BYPASSING = "DETAILED-BYPASSING"
    OFF = "OFF"
