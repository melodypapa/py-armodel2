"""AUTOSAR RptPreparationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 855)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class RptPreparationEnum(AREnum):
    """AUTOSAR RptPreparationEnum enumeration.

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

    NONE = "NONE"
    RPT_LEVEL1 = "RPT-LEVEL1"
    RPT_LEVEL2 = "RPT-LEVEL2"
    RPT_LEVEL3 = "RPT-LEVEL3"
    ORIGINAL = "ORIGINAL"
