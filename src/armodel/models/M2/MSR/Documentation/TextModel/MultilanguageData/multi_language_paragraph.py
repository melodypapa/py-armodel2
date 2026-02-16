"""MultiLanguageParagraph AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import (
    LParagraph,
)


class MultiLanguageParagraph(Paginateable):
    """AUTOSAR MultiLanguageParagraph."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("help_entry", None, True, False, None),  # helpEntry
        ("l1", None, False, False, LParagraph),  # l1
    ]

    def __init__(self) -> None:
        """Initialize MultiLanguageParagraph."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self.l1: LParagraph = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MultiLanguageParagraph to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguageParagraph":
        """Create MultiLanguageParagraph from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MultiLanguageParagraph instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MultiLanguageParagraph since parent returns ARObject
        return cast("MultiLanguageParagraph", obj)


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
