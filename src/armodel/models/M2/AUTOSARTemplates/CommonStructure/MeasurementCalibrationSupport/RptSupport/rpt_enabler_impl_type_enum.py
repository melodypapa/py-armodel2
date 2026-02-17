"""AUTOSAR RptEnablerImplTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 202)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 855)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.enums.json"""

from enum import Enum


class RptEnablerImplTypeEnum(Enum):
    """AUTOSAR RptEnablerImplTypeEnum enumeration."""

    NONE = "none"
    RPTENABLERRAM = "rptEnablerRam"
    RPTENABLERRAMANDROM = "rptEnablerRamAndRom"
    RPTENABLERROM = "rptEnablerRom"
