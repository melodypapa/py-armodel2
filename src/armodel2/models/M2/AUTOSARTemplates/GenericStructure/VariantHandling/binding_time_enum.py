"""AUTOSAR BindingTimeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 308)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 971)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 162)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class BindingTimeEnum(AREnum):
    """AUTOSAR BindingTimeEnum enumeration.

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

    CODE_GENERATION_TIME = "CODE-GENERATION-TIME"
    LINK_TIME = "LINK-TIME"
    PRE_COMPILE_TIME = "PRE-COMPILE-TIME"
    SYSTEM_DESIGN_TIME = "SYSTEM-DESIGN-TIME"
