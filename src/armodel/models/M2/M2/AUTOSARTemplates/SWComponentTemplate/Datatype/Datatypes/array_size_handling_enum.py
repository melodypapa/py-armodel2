"""AUTOSAR ArraySizeHandlingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 253)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.enums.json"""

from enum import Enum


class ArraySizeHandlingEnum(Enum):
    """AUTOSAR ArraySizeHandlingEnum enumeration."""

    ALLINDICESDIFFERENTARRAYSIZE = "allIndicesDifferentArraySize"
    ALLINDICESSAMEARRAYSIZE = "allIndicesSameArraySize"
    SOFTWARE = "Software"
    AUTOSARINHERITEDFROMARRAY = "AUTOSARinheritedFromArray"
