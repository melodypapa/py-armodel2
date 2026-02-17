"""AUTOSAR HandleInvalidEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 97)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 306)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.enums.json"""

from enum import Enum


class HandleInvalidEnum(Enum):
    """AUTOSAR HandleInvalidEnum enumeration."""

    DONTINVALIDATE = "dontInvalidate"
    EXTERNAL = "external"
    KEEP = "keep"
    REPLACE = "replace"
