"""AUTOSAR DiagnosticAudienceEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 754)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticAudienceEnum(AREnum):
    """AUTOSAR DiagnosticAudienceEnum enumeration.

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

    AFTERMARKET = "AFTERMARKET"
    AFTER_SALES = "AFTER-SALES"
    DEVELOPMENT = "DEVELOPMENT"
    MANUFACTURING = "MANUFACTURING"
    SUPPLIER = "SUPPLIER"
