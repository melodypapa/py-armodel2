"""AUTOSAR StandardNameEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 169)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 314)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 26)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_DocumentationOnM1.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class StandardNameEnum(AREnum):
    """AUTOSAR StandardNameEnum enumeration.

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

    AP = "AP"
    CP = "CP"
    FO = "FO"
    TA = "TA"
    TC = "TC"
