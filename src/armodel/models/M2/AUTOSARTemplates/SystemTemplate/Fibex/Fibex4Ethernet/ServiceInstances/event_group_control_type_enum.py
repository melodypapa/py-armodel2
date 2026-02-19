"""AUTOSAR EventGroupControlTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 489)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class EventGroupControlTypeEnum(AREnum):
    """AUTOSAR EventGroupControlTypeEnum enumeration.

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

    ACTIVATION_AND = "ACTIVATION-AND"
    ACTIVATION_MULTICAST = "ACTIVATION-MULTICAST"
    ACTIVATION_UNICAST = "ACTIVATION-UNICAST"
    TRIGGER_UNICAST = "TRIGGER-UNICAST"
