"""AUTOSAR NoteTypeEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 311)

JSON Source: packages/M2_MSR_Documentation_BlockElements_Note.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class NoteTypeEnum(AREnum):
    """AUTOSAR NoteTypeEnum enumeration.

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

    CAUTION = "CAUTION"
    EXAMPLE = "EXAMPLE"
    EXERCISE = "EXERCISE"
    HINTINSTRUCTION = "HINTINSTRUCTION"
    OTHERIN = "OTHERIN"
    TIP = "TIP"
