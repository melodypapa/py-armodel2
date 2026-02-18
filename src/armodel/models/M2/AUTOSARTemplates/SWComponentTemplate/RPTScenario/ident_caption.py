"""IdentCaption AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 317)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 851)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class IdentCaption(Identifiable, ABC):
    """AUTOSAR IdentCaption."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize IdentCaption."""
        super().__init__()


class IdentCaptionBuilder:
    """Builder for IdentCaption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdentCaption = IdentCaption()

    def build(self) -> IdentCaption:
        """Build and return IdentCaption object.

        Returns:
            IdentCaption instance
        """
        # TODO: Add validation
        return self._obj
