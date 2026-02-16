"""IEEE1722TpRvfColorSpaceEnum enumeration."""

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
