"""IndentSample AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 297)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import (
    ItemLabelPosEnum,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_overview_paragraph import (
    LOverviewParagraph,
)


class IndentSample(ARObject):
    """AUTOSAR IndentSample."""

    item_label_pos_enum: Optional[ItemLabelPosEnum]
    l2: LOverviewParagraph
    def __init__(self) -> None:
        """Initialize IndentSample."""
        super().__init__()
        self.item_label_pos_enum: Optional[ItemLabelPosEnum] = None
        self.l2: LOverviewParagraph = None


class IndentSampleBuilder:
    """Builder for IndentSample."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IndentSample = IndentSample()

    def build(self) -> IndentSample:
        """Build and return IndentSample object.

        Returns:
            IndentSample instance
        """
        # TODO: Add validation
        return self._obj
