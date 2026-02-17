"""AUTOSAR TtcanTriggerType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 450)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanCommunication.enums.json"""

from enum import Enum


class TtcanTriggerType(Enum):
    """AUTOSAR TtcanTriggerType enumeration."""

    RXTRIGGER = "rxTrigger"
    TXREFTRIGGER = "txRefTrigger"
    TXREFTRIGGERGAP = "txRefTriggerGap"
    TXTRIGGERMERGED = "txTriggerMerged"
    TXTRIGGERSINGLE = "txTriggerSingle"
    WATCHTRIGGER = "watchTrigger"
    WATCHTRIGGERGAP = "watchTriggerGap"
