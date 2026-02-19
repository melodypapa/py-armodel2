"""DefItem AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 298)

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

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class DefItem(Paginateable):
    """AUTOSAR DefItem."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def_: DocumentationBlock
    help_entry: Optional[String]
    def __init__(self) -> None:
        """Initialize DefItem."""
        super().__init__()
        self.def_: DocumentationBlock = None
        self.help_entry: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DefItem":
        """Deserialize XML element to DefItem object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DefItem object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DefItem, cls).deserialize(element)

        # Parse def_
        child = ARObject._find_child_element(element, "DEF")
        if child is not None:
            def__value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.def_ = def__value

        # Parse help_entry
        child = ARObject._find_child_element(element, "HELP-ENTRY")
        if child is not None:
            help_entry_value = child.text
            obj.help_entry = help_entry_value

        return obj



class DefItemBuilder:
    """Builder for DefItem."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DefItem = DefItem()

    def build(self) -> DefItem:
        """Build and return DefItem object.

        Returns:
            DefItem instance
        """
        # TODO: Add validation
        return self._obj
