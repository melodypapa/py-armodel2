"""AUTOSAR DataFilterTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 182)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 394)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Filter.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DataFilterTypeEnum(AREnum):
    """AUTOSAR DataFilterTypeEnum enumeration.

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

    ALWAYS = "ALWAYS"
    MASKED_NEW_DIFFERS_MASKED_OLD = "MASKED-NEW-DIFFERS-MASKED-OLD"
    MASKED_NEW_DIFFERS_X = "MASKED-NEW-DIFFERS-X"
    MASKED_NEW_EQUALS_X = "MASKED-NEW-EQUALS-X"
    NEVER = "NEVER"
    NEW_IS_OUTSIDE = "NEW-IS-OUTSIDE"
    NEW_IS_WITHINMINONE_EVERY_N = "NEW-IS-WITHINMINONE-EVERY-N"
