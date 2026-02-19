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
    AS_IS = "AS-IS"
    FIT_TO_PAGE = "FIT-TO-PAGE"
    GENERIC = "GENERIC"
    AUTOSAR = "A-U-T-O-S-A-R"
    LIMIT_TO_PAGE = "LIMIT-TO-PAGE"
    LIMIT_TO_TEXT = "LIMIT-TO-TEXT"
    ROTATE180_ROTATE180_LIMIT_TO = "ROTATE180-ROTATE180-LIMIT-TO"
    TEXT = "TEXT"
    ROTATE90CCW = "ROTATE90CCW"
    ROTATE90_CCW_FIT_TO_TEXT_ROTATE90_CCW_LIMIT = "ROTATE90-CCW-FIT-TO-TEXT-ROTATE90-CCW-LIMIT"
    TO_TEXT = "TO-TEXT"
    ROTATE90_CW = "ROTATE90-CW"
    ROTATE90_CW_FIT_TO_TEXT_ROTATE90_CW_LIMIT_TO = "ROTATE90-CW-FIT-TO-TEXT-ROTATE90-CW-LIMIT-TO"
