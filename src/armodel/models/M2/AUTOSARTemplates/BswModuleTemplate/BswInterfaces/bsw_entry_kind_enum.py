"""AUTOSAR BswEntryKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 33)

JSON Source: packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.enums.json"""

from enum import Enum


class BswEntryKindEnum(Enum):
    """AUTOSAR BswEntryKindEnum enumeration."""

    ABSTRACT = "abstract"
    CONCRETE = "concrete"
