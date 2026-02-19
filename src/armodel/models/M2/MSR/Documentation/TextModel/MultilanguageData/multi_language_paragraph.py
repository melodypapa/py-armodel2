"""MultiLanguageParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 290)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import (
    LParagraph,
)


class MultiLanguageParagraph(Paginateable):
    """AUTOSAR MultiLanguageParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    help_entry: Optional[String]
    l1: LParagraph
    def __init__(self) -> None:
        """Initialize MultiLanguageParagraph."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self.l1: LParagraph = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguageParagraph":
        """Deserialize XML element to MultiLanguageParagraph object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiLanguageParagraph object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultiLanguageParagraph, cls).deserialize(element)

        # Parse help_entry
        child = ARObject._find_child_element(element, "HELP-ENTRY")
        if child is not None:
            help_entry_value = child.text
            obj.help_entry = help_entry_value

        # Parse l1
        child = ARObject._find_child_element(element, "L1")
        if child is not None:
            l1_value = ARObject._deserialize_by_tag(child, "LParagraph")
            obj.l1 = l1_value

        return obj



class MultiLanguageParagraphBuilder:
    """Builder for MultiLanguageParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguageParagraph = MultiLanguageParagraph()

    def build(self) -> MultiLanguageParagraph:
        """Build and return MultiLanguageParagraph object.

        Returns:
            MultiLanguageParagraph instance
        """
        # TODO: Add validation
        return self._obj
