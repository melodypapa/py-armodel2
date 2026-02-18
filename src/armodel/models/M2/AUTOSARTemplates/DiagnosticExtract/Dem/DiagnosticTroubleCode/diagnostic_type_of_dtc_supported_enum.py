"""AUTOSAR DiagnosticTypeOfDtcSupportedEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 66)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticTypeOfDtcSupportedEnum(AREnum):
    """AUTOSAR DiagnosticTypeOfDtcSupportedEnum enumeration.

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

    ISO11992_4 = "iso11992_4"
    ISO14229_1 = "iso14229_1"
    ISO15031_6 = "iso15031_6"
    SAE_J1939_73 = "saeJ1939_73"
    SAE_J2012_DA = "saeJ2012_da"
