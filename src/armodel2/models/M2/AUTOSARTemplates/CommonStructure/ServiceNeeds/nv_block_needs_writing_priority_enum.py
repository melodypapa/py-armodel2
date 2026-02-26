"""AUTOSAR NvBlockNeedsWritingPriorityEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 233)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 680)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class NvBlockNeedsWritingPriorityEnum(AREnum):
    """AUTOSAR NvBlockNeedsWritingPriorityEnum enumeration.

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

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
