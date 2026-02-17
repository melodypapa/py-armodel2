"""AUTOSAR FilterDebouncingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 157)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.enums.json"""

from enum import Enum


class FilterDebouncingEnum(Enum):
    """AUTOSAR FilterDebouncingEnum enumeration."""

    DEBOUNCEDATA = "debounceData"
    RAWDATA = "rawData"
    WAITTIMEDATE = "waitTimeDate"
