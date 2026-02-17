"""AUTOSAR BswEntryRelationshipEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 52)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 52)

JSON Source: packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.enums.json"""

from enum import Enum


class BswEntryRelationshipEnum(Enum):
    """AUTOSAR BswEntryRelationshipEnum enumeration."""

    DERIVEDFROM = "derivedFrom"
