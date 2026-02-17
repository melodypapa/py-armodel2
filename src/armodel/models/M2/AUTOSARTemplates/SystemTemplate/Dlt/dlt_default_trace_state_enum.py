"""AUTOSAR DltDefaultTraceStateEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 723)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.enums.json"""

from enum import Enum


class DltDefaultTraceStateEnum(Enum):
    """AUTOSAR DltDefaultTraceStateEnum enumeration."""

    DEFAULTTRACESTATEDISABLED = "DefaultTraceStateDisabled"
    DEFAULTTRACESTATEENABLED = "DefaultTraceStateEnabled"
