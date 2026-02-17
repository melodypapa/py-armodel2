"""AUTOSAR RptServicePointEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 204)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 860)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.enums.json"""

from enum import Enum


class RptServicePointEnum(Enum):
    """AUTOSAR RptServicePointEnum enumeration."""

    ENABLED = "enabled"
    NONE = "none"
