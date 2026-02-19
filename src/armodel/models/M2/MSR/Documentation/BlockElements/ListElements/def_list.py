"""DefList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 297)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.def_item import (
        DefItem,
    )



class DefList(Paginateable):
    """AUTOSAR DefList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def_item: DefItem
    def __init__(self) -> None:
        """Initialize DefList."""
        super().__init__()
        self.def_item: DefItem = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DefList":
        """Deserialize XML element to DefList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DefList object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse def_item
        child = ARObject._find_child_element(element, "DEF-ITEM")
        if child is not None:
            def_item_value = ARObject._deserialize_by_tag(child, "DefItem")
            obj.def_item = def_item_value

        return obj



class DefListBuilder:
    """Builder for DefList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DefList = DefList()

    def build(self) -> DefList:
        """Build and return DefList object.

        Returns:
            DefList instance
        """
        # TODO: Add validation
        return self._obj
