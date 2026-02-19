"""Tgroup AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 334)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    AlignEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.colspec import (
    Colspec,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.tbody import (
    Tbody,
)


class Tgroup(ARObject):
    """AUTOSAR Tgroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    align: Optional[AlignEnum]
    cols: Integer
    colsep: Optional[TableSeparatorString]
    colspecs: list[Colspec]
    rowsep: Optional[TableSeparatorString]
    tbody: Tbody
    tfoot: Optional[Tbody]
    thead: Optional[Tbody]
    def __init__(self) -> None:
        """Initialize Tgroup."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.cols: Integer = None
        self.colsep: Optional[TableSeparatorString] = None
        self.colspecs: list[Colspec] = []
        self.rowsep: Optional[TableSeparatorString] = None
        self.tbody: Tbody = None
        self.tfoot: Optional[Tbody] = None
        self.thead: Optional[Tbody] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Tgroup":
        """Deserialize XML element to Tgroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Tgroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse align
        child = ARObject._find_child_element(element, "ALIGN")
        if child is not None:
            align_value = child.text
            obj.align = align_value

        # Parse cols
        child = ARObject._find_child_element(element, "COLS")
        if child is not None:
            cols_value = child.text
            obj.cols = cols_value

        # Parse colsep
        child = ARObject._find_child_element(element, "COLSEP")
        if child is not None:
            colsep_value = child.text
            obj.colsep = colsep_value

        # Parse colspecs (list)
        obj.colspecs = []
        for child in ARObject._find_all_child_elements(element, "COLSPECS"):
            colspecs_value = ARObject._deserialize_by_tag(child, "Colspec")
            obj.colspecs.append(colspecs_value)

        # Parse rowsep
        child = ARObject._find_child_element(element, "ROWSEP")
        if child is not None:
            rowsep_value = child.text
            obj.rowsep = rowsep_value

        # Parse tbody
        child = ARObject._find_child_element(element, "TBODY")
        if child is not None:
            tbody_value = ARObject._deserialize_by_tag(child, "Tbody")
            obj.tbody = tbody_value

        # Parse tfoot
        child = ARObject._find_child_element(element, "TFOOT")
        if child is not None:
            tfoot_value = ARObject._deserialize_by_tag(child, "Tbody")
            obj.tfoot = tfoot_value

        # Parse thead
        child = ARObject._find_child_element(element, "THEAD")
        if child is not None:
            thead_value = ARObject._deserialize_by_tag(child, "Tbody")
            obj.thead = thead_value

        return obj



class TgroupBuilder:
    """Builder for Tgroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Tgroup = Tgroup()

    def build(self) -> Tgroup:
        """Build and return Tgroup object.

        Returns:
            Tgroup instance
        """
        # TODO: Add validation
        return self._obj
