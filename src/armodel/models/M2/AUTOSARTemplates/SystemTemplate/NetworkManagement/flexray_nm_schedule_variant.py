"""AUTOSAR FlexrayNmScheduleVariant enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 680)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

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

    SCHEDULE_VARIANT1 = "scheduleVariant1"
    SCHEDULE_VARIANT2 = "scheduleVariant2"
    SCHEDULE_VARIANT3RECOMMENDED = "scheduleVariant3recommended"
    SCHEDULE_VARIANT4 = "scheduleVariant4"
    SCHEDULE_VARIANT5 = "scheduleVariant5"
    SCHEDULE_VARIANT6 = "scheduleVariant6"
    SCHEDULE_VARIANT7 = "scheduleVariant7"
