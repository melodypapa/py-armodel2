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

    def serialize(self) -> ET.Element:
        """Serialize Item to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Item, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize item_contents as direct children (no ITEM-CONTENTS wrapper)
        if self.item_contents is not None:
            serialized = self.item_contents.serialize()
            if serialized is not None:
                # Append all children from item_contents directly to ITEM element
                for child in serialized:
                    elem.append(child)

        return elem

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

        # Parse item_contents from direct children (no ITEM-CONTENTS wrapper)
        # Create a DocumentationBlock and parse DocumentationBlock-related children
        from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import DocumentationBlock
        item_contents_value = DocumentationBlock()
        item_contents_value = DocumentationBlock.deserialize(element)
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
