"""LabeledItem AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class LabeledItem(Paginateable):
    """AUTOSAR LabeledItem."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("help_entry", None, True, False, None),  # helpEntry
        ("item_contents", None, False, False, DocumentationBlock),  # itemContents
        ("item_label", None, False, False, MultiLanguageOverviewParagraph),  # itemLabel
    ]

    def __init__(self) -> None:
        """Initialize LabeledItem."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self.item_contents: Optional[DocumentationBlock] = None
        self.item_label: MultiLanguageOverviewParagraph = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LabeledItem to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LabeledItem":
        """Create LabeledItem from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LabeledItem instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LabeledItem since parent returns ARObject
        return cast("LabeledItem", obj)


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
