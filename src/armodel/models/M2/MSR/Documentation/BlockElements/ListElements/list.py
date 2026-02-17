"""List AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 295)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import (
    ListEnum,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.item import (
        Item,
    )



class List(Paginateable):
    """AUTOSAR List."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "item": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class="Item",
        ),  # item
        "type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ListEnum,
        ),  # type
    }

    def __init__(self) -> None:
        """Initialize List."""
        super().__init__()
        self.item: Item = None
        self.type: Optional[ListEnum] = None


class ListBuilder:
    """Builder for List."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: List = List()

    def build(self) -> List:
        """Build and return List object.

        Returns:
            List instance
        """
        # TODO: Add validation
        return self._obj
