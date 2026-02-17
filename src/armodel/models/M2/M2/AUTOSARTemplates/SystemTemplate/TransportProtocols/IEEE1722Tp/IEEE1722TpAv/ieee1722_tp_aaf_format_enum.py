"""AUTOSAR IEEE1722TpAafFormatEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 644)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.enums.json"""

from enum import Enum


class IEEE1722TpAafFormatEnum(Enum):
    """AUTOSAR IEEE1722TpAafFormatEnum enumeration."""

    AES3_32BIT = "aes3_32bit"
    FLOAT_32BITINT_16BITINT_24BITINT_32BIT = "float_32bitint_16bitint_24bitint_32bit"
    USER = "user"
