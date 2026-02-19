"""Row AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 336)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    ValignEnum,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)


class Row(Paginateable):
    """AUTOSAR Row."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rowsep: Optional[TableSeparatorString]
    valign: Optional[ValignEnum]
    def __init__(self) -> None:
        """Initialize Row."""
        super().__init__()
        self.rowsep: Optional[TableSeparatorString] = None
        self.valign: Optional[ValignEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize Row to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Row, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rowsep
        if self.rowsep is not None:
            serialized = ARObject._serialize_item(self.rowsep, "TableSeparatorString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROWSEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize valign
        if self.valign is not None:
            serialized = ARObject._serialize_item(self.valign, "ValignEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIGN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Row":
        """Deserialize XML element to Row object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Row object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Row, cls).deserialize(element)

        # Parse rowsep
        child = ARObject._find_child_element(element, "ROWSEP")
        if child is not None:
            rowsep_value = child.text
            obj.rowsep = rowsep_value

        # Parse valign
        child = ARObject._find_child_element(element, "VALIGN")
        if child is not None:
            valign_value = ValignEnum.deserialize(child)
            obj.valign = valign_value

        return obj



class RowBuilder:
    """Builder for Row."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Row = Row()

    def build(self) -> Row:
        """Build and return Row object.

        Returns:
            Row instance
        """
        # TODO: Add validation
        return self._obj
