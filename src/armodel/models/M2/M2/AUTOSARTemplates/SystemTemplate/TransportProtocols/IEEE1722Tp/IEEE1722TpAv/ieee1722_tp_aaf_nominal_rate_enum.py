"""AUTOSAR IEEE1722TpAafNominalRateEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 643)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.enums.json"""

from enum import Enum


class IEEE1722TpAafNominalRateEnum(Enum):
    """AUTOSAR IEEE1722TpAafNominalRateEnum enumeration."""

    _16KHZ = "_16kHz"
    _176_4KHZ = "_176_4kHz"
    _192KHZ = "_192kHz"
    _24KHZ = "_24kHz"
    _32KHZ = "_32kHz"
    _44_1KHZ = "_44_1kHz"
    _48KHZ = "_48kHz"
    SYSTEM = "System"
    AUTOSAR_88_2KHZ = "AUTOSAR_88_2kHz"
    _8KHZ = "_8kHz"
    _96KHZ = "_96kHz"
    USER = "user"
