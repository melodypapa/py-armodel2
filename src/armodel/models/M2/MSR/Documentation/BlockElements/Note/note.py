"""Note AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class Note(Paginateable):
    """AUTOSAR Note."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("label", None, False, False, MultilanguageLongName),  # label
        ("note_text", None, False, False, DocumentationBlock),  # noteText
        ("note_type", None, False, False, NoteTypeEnum),  # noteType
    ]

    def __init__(self) -> None:
        """Initialize Note."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.note_text: DocumentationBlock = None
        self.note_type: Optional[NoteTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Note to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Note":
        """Create Note from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Note instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Note since parent returns ARObject
        return cast("Note", obj)


class NoteBuilder:
    """Builder for Note."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Note = Note()

    def build(self) -> Note:
        """Build and return Note object.

        Returns:
            Note instance
        """
        # TODO: Add validation
        return self._obj
