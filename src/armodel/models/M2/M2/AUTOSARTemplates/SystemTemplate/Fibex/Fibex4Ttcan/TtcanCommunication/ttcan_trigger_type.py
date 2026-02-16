"""TtcanTriggerType enumeration."""

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
