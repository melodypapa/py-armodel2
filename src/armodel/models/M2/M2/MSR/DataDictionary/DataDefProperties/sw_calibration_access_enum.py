"""SwCalibrationAccessEnum enumeration."""

from enum import Enum


class SwCalibrationAccessEnum(Enum):
    """AUTOSAR SwCalibrationAccessEnum enumeration."""

    NOTACCESSIBLE = "notAccessible"
    READONLY = "readOnly"
    READWRITE = "readWrite"
