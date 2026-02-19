"""AUTOSAR DiagnosticConnectedIndicatorBehaviorEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 168)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticConnectedIndicatorBehaviorEnum(AREnum):
    """AUTOSAR DiagnosticConnectedIndicatorBehaviorEnum enumeration.

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

    BLINK_MODE = "BLINK-MODE"
    BLINK_OR_CONTINUOUS_ON_MODE = "BLINK-OR-CONTINUOUS-ON-MODE"
    CONTINUOUS_ON_MODE = "CONTINUOUS-ON-MODE"
    FAST_FLASHING_MODE = "FAST-FLASHING-MODE"
    SLOW_FLASHING_MODE = "SLOW-FLASHING-MODE"
