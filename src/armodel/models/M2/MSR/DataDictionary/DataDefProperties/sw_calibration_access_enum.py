"""AUTOSAR SwCalibrationAccessEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 337)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 335)

JSON Source: packages/M2_MSR_DataDictionary_DataDefProperties.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class SwCalibrationAccessEnum(AREnum):
    """AUTOSAR SwCalibrationAccessEnum enumeration.

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

    NOT_ACCESSIBLE = "NOT-ACCESSIBLE"
    READ_ONLY = "READ-ONLY"
    READ_WRITE = "READ-WRITE"
