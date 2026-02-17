"""DefList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 297)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.def_item import (
    DefItem,
)


class DefList(Paginateable):
    """AUTOSAR DefList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "def_item": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=DefItem,
        ),  # defItem
    }

    def __init__(self) -> None:
        """Initialize DefList."""
        super().__init__()
        self.def_item: DefItem = None


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
