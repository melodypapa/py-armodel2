"""AUTOSAR ProcessingKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 153)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.enums.json"""

from enum import Enum


class ProcessingKindEnum(Enum):
    """AUTOSAR ProcessingKindEnum enumeration."""

    FILTERED = "filtered"
    NONE = "none"
    RAW = "raw"
