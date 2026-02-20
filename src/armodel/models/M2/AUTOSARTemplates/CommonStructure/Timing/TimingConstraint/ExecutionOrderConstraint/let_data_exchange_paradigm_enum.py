"""AUTOSAR LetDataExchangeParadigmEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 143)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class LetDataExchangeParadigmEnum(AREnum):
    """AUTOSAR LetDataExchangeParadigmEnum enumeration.

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

    INTER_LET_ONLYINTRA_LET_EOC_ONLY = "INTER-LET-ONLYINTRA-LET-E-O-C-ONLY"
