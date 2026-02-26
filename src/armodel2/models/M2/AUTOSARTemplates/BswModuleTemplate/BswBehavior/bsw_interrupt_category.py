"""AUTOSAR BswInterruptCategory enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 76)

JSON Source: packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class BswInterruptCategory(AREnum):
    """AUTOSAR BswInterruptCategory enumeration.

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

    CAT1 = "CAT1"
    CAT2_INTERRUPT_ENTITY = "CAT2-INTERRUPT-ENTITY"
