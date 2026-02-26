"""AUTOSAR LogTraceDefaultLogLevelEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 723)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class LogTraceDefaultLogLevelEnum(AREnum):
    """AUTOSAR LogTraceDefaultLogLevelEnum enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

    DEBUG = "DEBUG"
    ERROR = "ERROR"
    FATALINFO = "FATALINFO"
    SYSTEM = "SYSTEM"
    AUTOSAR = "A-U-T-O-S-A-R"
    VERBOSE = "VERBOSE"
    WARN = "WARN"
