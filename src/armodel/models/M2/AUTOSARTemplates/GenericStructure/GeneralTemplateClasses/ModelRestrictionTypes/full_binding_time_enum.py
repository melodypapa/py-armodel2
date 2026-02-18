"""AUTOSAR FullBindingTimeEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 104)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 89)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class FullBindingTimeEnum(AREnum):
    """AUTOSAR FullBindingTimeEnum enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

    BLUEPRINT_DERIVATION_TIME = "blueprintDerivationTime"
    CODE_GENERATION_TIME = "codeGenerationTime"
    LINK_TIME = "linkTime"
    POST_BUILD = "postBuild"
    PRE_COMPILE_TIME = "preCompileTime"
    SYSTEM_DESIGN_TIME = "systemDesignTime"
