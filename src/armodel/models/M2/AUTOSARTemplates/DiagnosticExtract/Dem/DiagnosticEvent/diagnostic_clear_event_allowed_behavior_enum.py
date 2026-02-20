"""AUTOSAR DiagnosticClearEventAllowedBehaviorEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 166)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticClearEventAllowedBehaviorEnum(AREnum):
    """AUTOSAR DiagnosticClearEventAllowedBehaviorEnum enumeration.

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

    NO_STATUS_BYTE_CHANGEONLY_THIS_CYCLE_AND = "NO-STATUS-BYTE-CHANGEONLY-THIS-CYCLE-AND"
    READINESS = "READINESS"
