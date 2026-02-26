"""AUTOSAR DltDefaultTraceStateEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 723)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DltDefaultTraceStateEnum(AREnum):
    """AUTOSAR DltDefaultTraceStateEnum enumeration.

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

    DEFAULT_TRACE_STATE_DISABLED = "DEFAULT-TRACE-STATE-DISABLED"
    DEFAULT_TRACE_STATE_ENABLED = "DEFAULT-TRACE-STATE-ENABLED"
