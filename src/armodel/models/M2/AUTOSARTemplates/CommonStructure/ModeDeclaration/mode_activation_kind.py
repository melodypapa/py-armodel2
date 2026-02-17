"""AUTOSAR ModeActivationKind enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 96)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 545)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.enums.json"""

from enum import Enum


class ModeActivationKind(Enum):
    """AUTOSAR ModeActivationKind enumeration."""

    ONENTRYONEXITONTRANSITION = "onEntryonExitonTransition"
