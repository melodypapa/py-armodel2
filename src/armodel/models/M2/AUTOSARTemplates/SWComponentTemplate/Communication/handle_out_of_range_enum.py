"""AUTOSAR HandleOutOfRangeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 180)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 323)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.enums.json"""

from enum import Enum


class HandleOutOfRangeEnum(Enum):
    """AUTOSAR HandleOutOfRangeEnum enumeration."""

    DEFAULT = "default"
    EXTERNALREPLACEMENT = "externalReplacement"
    IGNOREINVALID = "ignoreinvalid"
    NONE = "none"
    SATURATE = "saturate"
