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
    def serialize(self) -> ET.Element:
        """Serialize List to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(List, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize item
        if self.item is not None:
            serialized = ARObject._serialize_item(self.item, "Item")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ITEM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type_ref
        if self.type_ref is not None:
            serialized = ARObject._serialize_item(self.type_ref, "ListEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
