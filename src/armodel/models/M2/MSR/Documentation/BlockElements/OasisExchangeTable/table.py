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
