"""AUTOSAR GraphicFitEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 303)

JSON Source: packages/M2_MSR_Documentation_BlockElements_Figure.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class GraphicFitEnum(AREnum):
    """AUTOSAR GraphicFitEnum enumeration.

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

    # Note: 1 duplicate literal(s) found and removed: Text
    AS_IS = "AsIs"
    FIT_TO_PAGE = "FitToPage"
    GENERIC = "Generic"
    AUTOSAR = "AUTOSAR"
    LIMIT_TO_PAGE = "LimitToPage"
    LIMIT_TO_TEXT = "LimitToText"
    ROTATE180_ROTATE180_LIMIT_TO = "Rotate180Rotate180LimitTo"
    TEXT = "Text"
    ROTATE90CCW = "Rotate90ccw"
    ROTATE90_CCW_FIT_TO_TEXT_ROTATE90_CCW_LIMIT = "Rotate90CcwFitToTextRotate90CcwLimit"
    TO_TEXT = "ToText"
    ROTATE90_CW = "Rotate90Cw"
    ROTATE90_CW_FIT_TO_TEXT_ROTATE90_CW_LIMIT_TO = "Rotate90CwFitToTextRotate90CwLimitTo"
