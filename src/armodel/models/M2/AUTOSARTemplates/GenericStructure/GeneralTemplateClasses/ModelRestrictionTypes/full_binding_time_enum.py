"""AUTOSAR FullBindingTimeEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 104)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 89)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.enums.json"""

from enum import Enum


class FullBindingTimeEnum(Enum):
    """AUTOSAR FullBindingTimeEnum enumeration."""

    BLUEPRINTDERIVATIONTIME = "blueprintDerivationTime"
    CODEGENERATIONTIME = "codeGenerationTime"
    LINKTIME = "linkTime"
    POSTBUILD = "postBuild"
    PRECOMPILETIME = "preCompileTime"
    SYSTEMDESIGNTIME = "systemDesignTime"
