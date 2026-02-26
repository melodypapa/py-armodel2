"""AUTOSAR DiagnosticValueAccessEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 246)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 114)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 782)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticValueAccessEnum(AREnum):
    """AUTOSAR DiagnosticValueAccessEnum enumeration.

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

    INFORMATION = "INFORMATION"
    READ_WRITE = "READ-WRITE"
    WRITE_ONLY = "WRITE-ONLY"
