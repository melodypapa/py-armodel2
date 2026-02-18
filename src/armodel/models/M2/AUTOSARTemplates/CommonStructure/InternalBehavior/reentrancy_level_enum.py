"""AUTOSAR ReentrancyLevelEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 73)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ReentrancyLevelEnum(AREnum):
    """AUTOSAR ReentrancyLevelEnum enumeration.

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

    MULTICORE_REENTRANTON = "multicoreReentranton"
    NON_REENTRANT = "nonReentrant"
    SINGLE_CORE_REENTRANT = "singleCoreReentrant"
