"""AUTOSAR BindingTimeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 308)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 971)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 162)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.enums.json"""

from enum import Enum


class BindingTimeEnum(Enum):
    """AUTOSAR BindingTimeEnum enumeration."""

    CODEGENERATIONTIME = "codeGenerationTime"
    LINKTIME = "linkTime"
    PRECOMPILETIME = "preCompileTime"
    SYSTEMDESIGNTIME = "systemDesignTime"
