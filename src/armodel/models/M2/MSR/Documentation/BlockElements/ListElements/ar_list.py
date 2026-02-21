"""ARList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 295)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_attribute

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import (
    ListEnum,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.item import (
        Item,
    )



class ARList(Paginateable):
    """AUTOSAR ARList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    item: list[Item]
    _type: Optional[ListEnum]
    def __init__(self) -> None:
        """Initialize ARList."""
        super().__init__()
        self.item: list[Item] = []
        self._type: Optional[ListEnum] = None
    @property
    @xml_attribute
    def type(self) -> ListEnum:
        """Get type XML attribute."""
        return self._type

    @type.setter
    def type(self, value: ListEnum) -> None:
        """Set type XML attribute."""
        self._type = value


    def serialize(self) -> ET.Element:
        """Serialize ARList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ARList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize item (list)
        for item in self.item:
            serialized = SerializationHelper.serialize_item(item, "Item")
            if serialized is not None:
                # For non-container lists, wrap with correct tag
                wrapped = ET.Element("ITEM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type as XML attribute
        if self.type is not None:
            elem.attrib["TYPE"] = str(self.type)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARList":
        """Deserialize XML element to ARList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ARList, cls).deserialize(element)

        # Parse item (list)
        obj.item = []
        for child in SerializationHelper.find_all_child_elements(element, "ITEM"):
            item_value = SerializationHelper.deserialize_by_tag(child, "Item")
            obj.item.append(item_value)

        # Parse type from XML attribute
        if "TYPE" in element.attrib:
            type_value = ListEnum(element.attrib["TYPE"])
            obj.type = type_value

        return obj



class ARListBuilder:
    """Builder for ARList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ARList = ARList()

    def build(self) -> ARList:
        """Build and return ARList object.

        Returns:
            ARList instance
        """
        # TODO: Add validation
        return self._obj
