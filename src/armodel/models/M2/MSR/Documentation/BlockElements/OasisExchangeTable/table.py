"""Table AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 332)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    FloatEnum,
    FrameEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.caption import (
    Caption,
)


class Table(Paginateable):
    """AUTOSAR Table."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    colsep: Optional[TableSeparatorString]
    float: FloatEnum
    frame: Optional[FrameEnum]
    help_entry: Optional[String]
    orient: Optional[Any]
    pgwide: Optional[NameToken]
    rowsep: Optional[TableSeparatorString]
    table_caption: Optional[Caption]
    tabstyle: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize Table."""
        super().__init__()
        self.colsep: Optional[TableSeparatorString] = None
        self.float: FloatEnum = None
        self.frame: Optional[FrameEnum] = None
        self.help_entry: Optional[String] = None
        self.orient: Optional[Any] = None
        self.pgwide: Optional[NameToken] = None
        self.rowsep: Optional[TableSeparatorString] = None
        self.table_caption: Optional[Caption] = None
        self.tabstyle: Optional[NameToken] = None
    def serialize(self) -> ET.Element:
        """Serialize Table to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Table, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize colsep
        if self.colsep is not None:
            serialized = ARObject._serialize_item(self.colsep, "TableSeparatorString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLSEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize float
        if self.float is not None:
            serialized = ARObject._serialize_item(self.float, "FloatEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize frame
        if self.frame is not None:
            serialized = ARObject._serialize_item(self.frame, "FrameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize help_entry
        if self.help_entry is not None:
            serialized = ARObject._serialize_item(self.help_entry, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HELP-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize orient
        if self.orient is not None:
            serialized = ARObject._serialize_item(self.orient, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ORIENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pgwide
        if self.pgwide is not None:
            serialized = ARObject._serialize_item(self.pgwide, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PGWIDE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize table_caption
        if self.table_caption is not None:
            serialized = ARObject._serialize_item(self.table_caption, "Caption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TABLE-CAPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tabstyle
        if self.tabstyle is not None:
            serialized = ARObject._serialize_item(self.tabstyle, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TABSTYLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Table":
        """Deserialize XML element to Table object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Table object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Table, cls).deserialize(element)

        # Parse colsep
        child = ARObject._find_child_element(element, "COLSEP")
        if child is not None:
            colsep_value = child.text
            obj.colsep = colsep_value

        # Parse float
        child = ARObject._find_child_element(element, "FLOAT")
        if child is not None:
            float_value = FloatEnum.deserialize(child)
            obj.float = float_value

        # Parse frame
        child = ARObject._find_child_element(element, "FRAME")
        if child is not None:
            frame_value = FrameEnum.deserialize(child)
            obj.frame = frame_value

        # Parse help_entry
        child = ARObject._find_child_element(element, "HELP-ENTRY")
        if child is not None:
            help_entry_value = child.text
            obj.help_entry = help_entry_value

        # Parse orient
        child = ARObject._find_child_element(element, "ORIENT")
        if child is not None:
            orient_value = child.text
            obj.orient = orient_value

        # Parse pgwide
        child = ARObject._find_child_element(element, "PGWIDE")
        if child is not None:
            pgwide_value = child.text
            obj.pgwide = pgwide_value

        # Parse rowsep
        child = ARObject._find_child_element(element, "ROWSEP")
        if child is not None:
            rowsep_value = child.text
            obj.rowsep = rowsep_value

        # Parse table_caption
        child = ARObject._find_child_element(element, "TABLE-CAPTION")
        if child is not None:
            table_caption_value = ARObject._deserialize_by_tag(child, "Caption")
            obj.table_caption = table_caption_value

        # Parse tabstyle
        child = ARObject._find_child_element(element, "TABSTYLE")
        if child is not None:
            tabstyle_value = child.text
            obj.tabstyle = tabstyle_value

        return obj



class TableBuilder:
    """Builder for Table."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Table = Table()

    def build(self) -> Table:
        """Build and return Table object.

        Returns:
            Table instance
        """
        # TODO: Add validation
        return self._obj
