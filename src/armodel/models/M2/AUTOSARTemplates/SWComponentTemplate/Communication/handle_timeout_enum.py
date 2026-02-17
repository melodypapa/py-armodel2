"""AUTOSAR HandleTimeoutEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 174)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.enums.json"""

from enum import Enum


class HandleTimeoutEnum(Enum):
    """AUTOSAR HandleTimeoutEnum enumeration."""

    NONE = "none"
    REPLACE = "replace"
    REPLACEBYTIMEOUTSUBSTITUTIONVALUE = "replaceByTimeoutSubstitutionValue"
