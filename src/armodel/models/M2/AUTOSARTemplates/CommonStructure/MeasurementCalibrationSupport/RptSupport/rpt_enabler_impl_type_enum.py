"""AUTOSAR RptEnablerImplTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 202)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 855)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class RptEnablerImplTypeEnum(AREnum):
    """AUTOSAR RptEnablerImplTypeEnum enumeration.

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
    RPT_ENABLER_RAM = "RPT-ENABLER-RAM"
    RPT_ENABLER_RAM_AND_ROM = "RPT-ENABLER-RAM-AND-ROM"
    RPT_ENABLER_ROM = "RPT-ENABLER-ROM"
