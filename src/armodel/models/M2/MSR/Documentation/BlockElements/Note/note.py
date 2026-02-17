"""Note AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 310)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Note.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Note import (
    NoteTypeEnum,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class Note(Paginateable):
    """AUTOSAR Note."""

    label: Optional[MultilanguageLongName]
    note_text: DocumentationBlock
    note_type: Optional[NoteTypeEnum]
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
