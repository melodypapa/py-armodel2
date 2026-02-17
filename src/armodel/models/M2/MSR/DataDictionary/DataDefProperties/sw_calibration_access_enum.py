"""AUTOSAR SwCalibrationAccessEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 337)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 335)

JSON Source: packages/M2_MSR_DataDictionary_DataDefProperties.enums.json"""

from enum import Enum


class SwCalibrationAccessEnum(Enum):
    """AUTOSAR SwCalibrationAccessEnum enumeration."""

    NOTACCESSIBLE = "notAccessible"
    READONLY = "readOnly"
    READWRITE = "readWrite"
