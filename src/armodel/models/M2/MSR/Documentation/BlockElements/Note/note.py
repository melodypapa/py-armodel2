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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    label: Optional[MultilanguageLongName]
    note_text: DocumentationBlock
    note_type: Optional[NoteTypeEnum]
    def __init__(self) -> None:
        """Initialize Note."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.note_text: DocumentationBlock = None
        self.note_type: Optional[NoteTypeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Note":
        """Deserialize XML element to Note object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Note object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Note, cls).deserialize(element)

        # Parse label
        child = ARObject._find_child_element(element, "LABEL")
        if child is not None:
            label_value = ARObject._deserialize_by_tag(child, "MultilanguageLongName")
            obj.label = label_value

        # Parse note_text
        child = ARObject._find_child_element(element, "NOTE-TEXT")
        if child is not None:
            note_text_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.note_text = note_text_value

        # Parse note_type
        child = ARObject._find_child_element(element, "NOTE-TYPE")
        if child is not None:
            note_type_value = NoteTypeEnum.deserialize(child)
            obj.note_type = note_type_value

        return obj



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
