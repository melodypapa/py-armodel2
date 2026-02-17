"""AUTOSAR GraphicNotationEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 304)

JSON Source: packages/M2_MSR_Documentation_BlockElements_Figure.enums.json"""

from enum import Enum


class GraphicNotationEnum(Enum):
    """AUTOSAR GraphicNotationEnum enumeration."""

    BMP = "bmp"
    EPS = "eps"
    GIF = "gif"
    JPG = "jpg"
    PDF = "pdf"
    PNG = "png"
    GENERIC = "Generic"
    AUTOSAR = "AUTOSAR"
    TIFF = "tiff"
