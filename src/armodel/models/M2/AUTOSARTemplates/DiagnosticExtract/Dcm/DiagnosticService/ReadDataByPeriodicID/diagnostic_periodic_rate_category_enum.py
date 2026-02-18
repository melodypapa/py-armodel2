"""AUTOSAR DiagnosticPeriodicRateCategoryEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 131)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticPeriodicRateCategoryEnum(AREnum):
    """AUTOSAR DiagnosticPeriodicRateCategoryEnum enumeration.

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

    PERIODIC_RATE_FAST = "periodicRateFast"
    PERIODIC_RATE_MEDIUM = "periodicRateMedium"
    PERIODIC_RATE_SLOW = "periodicRateSlow"
