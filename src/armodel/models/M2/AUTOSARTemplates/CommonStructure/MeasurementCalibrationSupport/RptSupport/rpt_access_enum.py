"""AUTOSAR RptAccessEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 205)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 857)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.enums.json"""

from enum import Enum


class RptAccessEnum(Enum):
    """AUTOSAR RptAccessEnum enumeration."""

    ENABLED = "enabled"
    NONE = "none"
    PROTECTED = "protected"
