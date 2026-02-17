"""AUTOSAR IEEE1722TpRvfColorSpaceEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 652)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.enums.json"""

from enum import Enum


class IEEE1722TpRvfColorSpaceEnum(Enum):
    """AUTOSAR IEEE1722TpRvfColorSpaceEnum enumeration."""

    BT_REC_601 = "bt_rec_601"
    BT_REC_709 = "bt_rec_709"
    GRAYSCALE = "grayscale"
    ITU_BT_2020 = "itu_bt_2020"
    USER = "user"
    XYZ = "xyz"
    YCBCR = "ycbcr"
    YCGCO = "ycgco"
    YCM = "ycm"
