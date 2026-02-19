"""LabeledItem AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 296)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

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
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class LabeledItem(Paginateable):
    """AUTOSAR LabeledItem."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    help_entry: Optional[String]
    item_contents: Optional[DocumentationBlock]
    item_label: MultiLanguageOverviewParagraph
    def __init__(self) -> None:
        """Initialize LabeledItem."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self.item_contents: Optional[DocumentationBlock] = None
        self.item_label: MultiLanguageOverviewParagraph = None
    def serialize(self) -> ET.Element:
        """Serialize LabeledItem to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LabeledItem, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize help_entry
        if self.help_entry is not None:
            serialized = ARObject._serialize_item(self.help_entry, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HELP-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize item_contents
        if self.item_contents is not None:
            serialized = ARObject._serialize_item(self.item_contents, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ITEM-CONTENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize item_label
        if self.item_label is not None:
            serialized = ARObject._serialize_item(self.item_label, "MultiLanguageOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ITEM-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LabeledItem":
        """Deserialize XML element to LabeledItem object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LabeledItem object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LabeledItem, cls).deserialize(element)

        # Parse help_entry
        child = ARObject._find_child_element(element, "HELP-ENTRY")
        if child is not None:
            help_entry_value = child.text
            obj.help_entry = help_entry_value

        # Parse item_contents
        child = ARObject._find_child_element(element, "ITEM-CONTENTS")
        if child is not None:
            item_contents_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.item_contents = item_contents_value

        # Parse item_label
        child = ARObject._find_child_element(element, "ITEM-LABEL")
        if child is not None:
            item_label_value = ARObject._deserialize_by_tag(child, "MultiLanguageOverviewParagraph")
            obj.item_label = item_label_value

        return obj



class LabeledItemBuilder:
    """Builder for LabeledItem."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LabeledItem = LabeledItem()

    def build(self) -> LabeledItem:
        """Build and return LabeledItem object.

        Returns:
            LabeledItem instance
        """
        # TODO: Add validation
        return self._obj
