"""AUTOSAR CalprmAxisCategoryEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 352)

JSON Source: packages/M2_MSR_DataDictionary_CalibrationParameter.enums.json"""

from enum import Enum


class CalprmAxisCategoryEnum(Enum):
    """AUTOSAR CalprmAxisCategoryEnum enumeration."""

    COMAXIS = "comAxis"
    FIXAXIS = "fixAXIS"
    RESAXIS = "resAxis"
    STDAXIS = "stdAxis"
