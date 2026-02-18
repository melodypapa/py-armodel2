"""AUTOSAR TtcanTriggerType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 450)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanCommunication.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class TtcanTriggerType(AREnum):
    """AUTOSAR TtcanTriggerType enumeration.

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

    RX_TRIGGER = "rxTrigger"
    TX_REF_TRIGGER = "txRefTrigger"
    TX_REF_TRIGGER_GAP = "txRefTriggerGap"
    TX_TRIGGER_MERGED = "txTriggerMerged"
    TX_TRIGGER_SINGLE = "txTriggerSingle"
    WATCH_TRIGGER = "watchTrigger"
    WATCH_TRIGGER_GAP = "watchTriggerGap"
