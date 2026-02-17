"""AUTOSAR AdditionalBindingTimeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 700)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 422)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.enums.json"""

from enum import Enum


class AdditionalBindingTimeEnum(Enum):
    """AUTOSAR AdditionalBindingTimeEnum enumeration."""

    BLUEPRINTDERIVATIONTIME = "blueprintDerivationTime"
    POSTBUILD = "postBuild"
