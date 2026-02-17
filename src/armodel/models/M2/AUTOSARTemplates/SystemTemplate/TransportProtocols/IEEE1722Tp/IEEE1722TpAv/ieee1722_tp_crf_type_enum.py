"""AUTOSAR IEEE1722TpCrfTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 640)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.enums.json"""

from enum import Enum


class IEEE1722TpCrfTypeEnum(Enum):
    """AUTOSAR IEEE1722TpCrfTypeEnum enumeration."""

    AUDIOSAMPLE = "audioSample"
    MACHINECYCLE = "machineCycle"
    USER = "user"
    VIDEOFRAME = "videoFrame"
    VIDEOLINE = "videoLine"
