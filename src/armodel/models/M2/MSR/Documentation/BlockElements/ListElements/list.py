"""List AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 295)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import (
    ListEnum,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.item import (
        Item,
    )



class List(Paginateable):
    """AUTOSAR List."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    item: Item
    type_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize List."""
        super().__init__()
        self.item: Item = None
        self.type_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "List":
        """Deserialize XML element to List object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized List object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(List, cls).deserialize(element)

        # Parse item
        child = ARObject._find_child_element(element, "ITEM")
        if child is not None:
            item_value = ARObject._deserialize_by_tag(child, "Item")
            obj.item = item_value

        # Parse type_ref
        child = ARObject._find_child_element(element, "TYPE")
        if child is not None:
            type_ref_value = ListEnum.deserialize(child)
            obj.type_ref = type_ref_value

        return obj



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
