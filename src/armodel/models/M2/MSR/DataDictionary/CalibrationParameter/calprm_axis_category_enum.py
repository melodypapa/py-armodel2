"""AUTOSAR CalprmAxisCategoryEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 352)

JSON Source: packages/M2_MSR_DataDictionary_CalibrationParameter.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class CalprmAxisCategoryEnum(AREnum):
    """AUTOSAR CalprmAxisCategoryEnum enumeration.

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

    COM_AXIS = "COM-AXIS"
    FIX_AXIS = "FIX-A-X-I-S"
    RES_AXIS = "RES-AXIS"
    STD_AXIS = "STD-AXIS"
