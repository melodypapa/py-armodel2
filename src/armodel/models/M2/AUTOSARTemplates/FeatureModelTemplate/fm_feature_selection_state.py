"""AUTOSAR FMFeatureSelectionState enumeration.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 41)

JSON Source: packages/M2_AUTOSARTemplates_FeatureModelTemplate.enums.json"""

from enum import Enum


class FMFeatureSelectionState(Enum):
    """AUTOSAR FMFeatureSelectionState enumeration."""

    DESELECTED = "deselected"
    SELECTED = "selected"
    UNDECIDED = "undecided"
