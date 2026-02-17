"""AUTOSAR RptExecutionControlEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 859)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.enums.json"""

from enum import Enum


class RptExecutionControlEnum(Enum):
    """AUTOSAR RptExecutionControlEnum enumeration."""

    CONDITIONAL = "conditional"
    NONE = "none"
