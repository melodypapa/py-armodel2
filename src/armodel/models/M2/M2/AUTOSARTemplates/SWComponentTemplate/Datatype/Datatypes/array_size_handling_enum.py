"""ArraySizeHandlingEnum enumeration."""

from enum import Enum


class ArraySizeHandlingEnum(Enum):
    """AUTOSAR ArraySizeHandlingEnum enumeration."""

    ALLINDICESDIFFERENTARRAYSIZE = "allIndicesDifferentArraySize"
    ALLINDICESSAMEARRAYSIZE = "allIndicesSameArraySize"
    SOFTWARE = "Software"
    AUTOSARINHERITEDFROMARRAY = "AUTOSARinheritedFromArray"
