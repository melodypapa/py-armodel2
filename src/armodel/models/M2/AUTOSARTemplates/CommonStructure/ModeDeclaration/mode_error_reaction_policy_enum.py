"""AUTOSAR ModeErrorReactionPolicyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 44)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 637)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.enums.json"""

from enum import Enum


class ModeErrorReactionPolicyEnum(Enum):
    """AUTOSAR ModeErrorReactionPolicyEnum enumeration."""

    DEFAULTMODELASTMODE = "defaultModelastMode"
