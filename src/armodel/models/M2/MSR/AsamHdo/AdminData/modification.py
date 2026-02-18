"""Modification AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 86)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_AdminData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class Modification(ARObject):
    """AUTOSAR Modification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    change: MultiLanguageOverviewParagraph
    reason: Optional[MultiLanguageOverviewParagraph]
    def __init__(self) -> None:
        """Initialize Modification."""
        super().__init__()
        self.change: MultiLanguageOverviewParagraph = None
        self.reason: Optional[MultiLanguageOverviewParagraph] = None


class ModificationBuilder:
    """Builder for Modification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Modification = Modification()

    def build(self) -> Modification:
        """Build and return Modification object.

        Returns:
            Modification instance
        """
        # TODO: Add validation
        return self._obj
