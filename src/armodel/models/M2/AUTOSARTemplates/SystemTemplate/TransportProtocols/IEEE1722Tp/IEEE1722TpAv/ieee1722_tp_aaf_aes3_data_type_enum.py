"""AUTOSAR IEEE1722TpAafAes3DataTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 645)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.enums.json"""

from enum import Enum


class IEEE1722TpAafAes3DataTypeEnum(Enum):
    """AUTOSAR IEEE1722TpAafAes3DataTypeEnum enumeration."""

    IEC61937 = "iec61937"
    PCM = "pcm"
    SMPTE338 = "smpte338"
    UNSPECIFIED = "unspecified"
    VENDOR = "vendor"
