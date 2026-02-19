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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    item_label_pos_enum: Optional[ItemLabelPosEnum]
    l2: LOverviewParagraph
    def __init__(self) -> None:
        """Initialize IndentSample."""
        super().__init__()
        self.item_label_pos_enum: Optional[ItemLabelPosEnum] = None
        self.l2: LOverviewParagraph = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndentSample":
        """Deserialize XML element to IndentSample object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IndentSample object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse item_label_pos_enum
        child = ARObject._find_child_element(element, "ITEM-LABEL-POS-ENUM")
        if child is not None:
            item_label_pos_enum_value = ItemLabelPosEnum.deserialize(child)
            obj.item_label_pos_enum = item_label_pos_enum_value

        # Parse l2
        child = ARObject._find_child_element(element, "L2")
        if child is not None:
            l2_value = ARObject._deserialize_by_tag(child, "LOverviewParagraph")
            obj.l2 = l2_value

        return obj



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
