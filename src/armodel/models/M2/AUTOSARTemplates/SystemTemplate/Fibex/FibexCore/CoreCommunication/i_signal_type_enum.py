"""AUTOSAR ISignalTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 322)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from enum import Enum


class ISignalTypeEnum(Enum):
    """AUTOSAR ISignalTypeEnum enumeration."""

    ARRAY = "array"
    PRIMITIVE = "primitive"
