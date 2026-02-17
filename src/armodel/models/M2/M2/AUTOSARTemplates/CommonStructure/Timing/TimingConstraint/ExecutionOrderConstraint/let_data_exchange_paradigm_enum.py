"""AUTOSAR LetDataExchangeParadigmEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 143)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.enums.json"""

from enum import Enum


class LetDataExchangeParadigmEnum(Enum):
    """AUTOSAR LetDataExchangeParadigmEnum enumeration."""

    INTERLETONLYINTRALETEOCONLY = "interLetOnlyintraLetEOCOnly"
