"""ImpositionTime AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_ImpositionTimes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class ImpositionTime(Identifiable):
    """AUTOSAR ImpositionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ImpositionTime."""
        super().__init__()


class ImpositionTimeBuilder:
    """Builder for ImpositionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImpositionTime = ImpositionTime()

    def build(self) -> ImpositionTime:
        """Build and return ImpositionTime object.

        Returns:
            ImpositionTime instance
        """
        # TODO: Add validation
        return self._obj
