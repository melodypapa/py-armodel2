"""AUTOSAR GraphicFitEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 303)

JSON Source: packages/M2_MSR_Documentation_BlockElements_Figure.enums.json"""

from enum import Enum


class GraphicFitEnum(Enum):
    """AUTOSAR GraphicFitEnum enumeration."""

    # Note: 1 duplicate literal(s) found and removed: Text
    ASIS = "AsIs"
    FITTOPAGE = "FitToPage"
    GENERIC = "Generic"
    AUTOSAR = "AUTOSAR"
    LIMITTOPAGE = "LimitToPage"
    LIMITTOTEXT = "LimitToText"
    ROTATE180ROTATE180LIMITTO = "Rotate180Rotate180LimitTo"
    TEXT = "Text"
    ROTATE90CCW = "Rotate90ccw"
    ROTATE90CCWFITTOTEXTROTATE90CCWLIMIT = "Rotate90CcwFitToTextRotate90CcwLimit"
    TOTEXT = "ToText"
    ROTATE90CW = "Rotate90Cw"
    ROTATE90CWFITTOTEXTROTATE90CWLIMITTO = "Rotate90CwFitToTextRotate90CwLimitTo"
