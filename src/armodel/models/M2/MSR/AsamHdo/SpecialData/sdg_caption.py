"""SdgCaption AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class SdgCaption(MultilanguageReferrable):
    """AUTOSAR SdgCaption."""

    desc: Optional[MultiLanguageOverviewParagraph]
    def __init__(self) -> None:
        """Initialize SdgCaption."""
        super().__init__()
        self.desc: Optional[MultiLanguageOverviewParagraph] = None


class SdgCaptionBuilder:
    """Builder for SdgCaption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgCaption = SdgCaption()

    def build(self) -> SdgCaption:
        """Build and return SdgCaption object.

        Returns:
            SdgCaption instance
        """
        # TODO: Add validation
        return self._obj
