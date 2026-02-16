"""FMFeatureSelectionState enumeration."""

from enum import Enum


class FMFeatureSelectionState(Enum):
    """AUTOSAR FMFeatureSelectionState enumeration."""

    DESELECTED = "deselected"
    SELECTED = "selected"
    UNDECIDED = "undecided"
