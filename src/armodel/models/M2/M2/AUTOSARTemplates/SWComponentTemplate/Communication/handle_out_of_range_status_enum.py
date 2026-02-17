"""AUTOSAR HandleOutOfRangeStatusEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 172)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.enums.json"""

from enum import Enum


class HandleOutOfRangeStatusEnum(Enum):
    """AUTOSAR HandleOutOfRangeStatusEnum enumeration."""

    INDICATE = "indicate"
    SILENT = "silent"
