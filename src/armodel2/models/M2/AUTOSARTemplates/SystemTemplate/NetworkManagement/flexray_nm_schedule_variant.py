"""AUTOSAR FlexrayNmScheduleVariant enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 680)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class FlexrayNmScheduleVariant(AREnum):
    """AUTOSAR FlexrayNmScheduleVariant enumeration.

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

    SCHEDULE_VARIANT1 = "SCHEDULE-VARIANT1"
    SCHEDULE_VARIANT2 = "SCHEDULE-VARIANT2"
    SCHEDULE_VARIANT3RECOMMENDED = "SCHEDULE-VARIANT3RECOMMENDED"
    SCHEDULE_VARIANT4 = "SCHEDULE-VARIANT4"
    SCHEDULE_VARIANT5 = "SCHEDULE-VARIANT5"
    SCHEDULE_VARIANT6 = "SCHEDULE-VARIANT6"
    SCHEDULE_VARIANT7 = "SCHEDULE-VARIANT7"
