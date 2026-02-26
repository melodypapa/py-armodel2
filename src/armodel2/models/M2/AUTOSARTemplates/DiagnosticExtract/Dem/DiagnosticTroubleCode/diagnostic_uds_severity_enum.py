"""AUTOSAR DiagnosticUdsSeverityEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 187)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticUdsSeverityEnum(AREnum):
    """AUTOSAR DiagnosticUdsSeverityEnum enumeration.

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

    CHECK_AT_NEXT_HALT = "CHECK-AT-NEXT-HALT"
    IMMEDIATELY = "IMMEDIATELY"
    MAINTENANCE_ONLY = "MAINTENANCE-ONLY"
    NO_SEVERITY = "NO-SEVERITY"
