"""AUTOSAR BswExecutionContext enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 34)

JSON Source: packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class BswExecutionContext(AREnum):
    """AUTOSAR BswExecutionContext enumeration.

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

    HOOKINTERRUPT_CAT1INTERRUPT_CAT2 = "HOOKINTERRUPT-CAT1INTERRUPT-CAT2"
    TASK = "TASK"
    UNSPECIFIED = "UNSPECIFIED"
