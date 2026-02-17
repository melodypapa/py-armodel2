"""AUTOSAR RptPreparationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 855)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.enums.json"""

from enum import Enum


class RptPreparationEnum(Enum):
    """AUTOSAR RptPreparationEnum enumeration."""

    NONE = "none"
    RPTLEVEL1 = "rptLevel1"
    RPTLEVEL2 = "rptLevel2"
    RPTLEVEL3 = "rptLevel3"
    ORIGINAL = "original"
