"""AUTOSAR DiagnosticIndicatorTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 766)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticIndicator.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticIndicatorTypeEnum(AREnum):
    """AUTOSAR DiagnosticIndicatorTypeEnum enumeration.

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

    AMBER_WARNING = "amberWarning"
    MALFUNCTION = "malfunction"
    PROTECT_LAMP = "protectLamp"
    RED_STOP_LAMP = "redStopLamp"
    WARNING = "warning"
