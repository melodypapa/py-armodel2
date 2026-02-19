"""Item AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 295)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class Item(Paginateable):
    """AUTOSAR Item."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    item_contents: DocumentationBlock
    def __init__(self) -> None:
        """Initialize Item."""
        super().__init__()
        self.item_contents: DocumentationBlock = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Item":
        """Deserialize XML element to Item object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Item object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Item, cls).deserialize(element)

        # Parse item_contents
        child = ARObject._find_child_element(element, "ITEM-CONTENTS")
        if child is not None:
            item_contents_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.item_contents = item_contents_value

        return obj



class ItemBuilder:
    """Builder for Item."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Item = Item()

    def build(self) -> Item:
        """Build and return Item object.

        Returns:
            Item instance
        """
        # TODO: Add validation
        return self._obj
