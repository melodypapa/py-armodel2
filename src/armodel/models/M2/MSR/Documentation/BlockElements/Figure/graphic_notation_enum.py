"""AUTOSAR GraphicNotationEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 304)

JSON Source: packages/M2_MSR_Documentation_BlockElements_Figure.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class GraphicNotationEnum(AREnum):
    """AUTOSAR GraphicNotationEnum enumeration.

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

    BMP = "bmp"
    EPS = "eps"
    GIF = "gif"
    JPG = "jpg"
    PDF = "pdf"
    PNG = "png"
    GENERIC = "Generic"
    AUTOSAR = "AUTOSAR"
    TIFF = "tiff"
