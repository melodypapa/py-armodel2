"""AUTOSAR HandleTerminationAndRestartEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 354)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class HandleTerminationAndRestartEnum(AREnum):
    """AUTOSAR HandleTerminationAndRestartEnum enumeration.

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

    CAN_BE_TERMINATED = "CAN-BE-TERMINATED"
    CAN_BE_TERMINATED_AND_RESTARTED = "CAN-BE-TERMINATED-AND-RESTARTED"
    NO_SUPPORT = "NO-SUPPORT"
