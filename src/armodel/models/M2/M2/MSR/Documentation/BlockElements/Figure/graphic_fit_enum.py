"""GraphicFitEnum enumeration."""

from enum import Enum


class GraphicFitEnum(Enum):
    """AUTOSAR GraphicFitEnum enumeration."""

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
    TEXT = "Text"
