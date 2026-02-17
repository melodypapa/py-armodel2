"""Note AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 310)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Note.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "label": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultilanguageLongName,
        ),  # label
        "note_text": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=DocumentationBlock,
        ),  # noteText
        "note_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NoteTypeEnum,
        ),  # noteType
    }

    def __init__(self) -> None:
        """Initialize Note."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.note_text: DocumentationBlock = None
        self.note_type: Optional[NoteTypeEnum] = None


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
