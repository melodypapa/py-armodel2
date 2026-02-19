"""Colspec AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    AlignEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)


class Colspec(ARObject):
    """AUTOSAR Colspec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    align: Optional[AlignEnum]
    colname: Optional[String]
    colnum: Optional[String]
    colsep: Optional[TableSeparatorString]
    colwidth: Optional[String]
    rowsep: Optional[TableSeparatorString]
    def __init__(self) -> None:
        """Initialize Colspec."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.colname: Optional[String] = None
        self.colnum: Optional[String] = None
        self.colsep: Optional[TableSeparatorString] = None
        self.colwidth: Optional[String] = None
        self.rowsep: Optional[TableSeparatorString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Colspec":
        """Deserialize XML element to Colspec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Colspec object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse align
        child = ARObject._find_child_element(element, "ALIGN")
        if child is not None:
            align_value = child.text
            obj.align = align_value

        # Parse colname
        child = ARObject._find_child_element(element, "COLNAME")
        if child is not None:
            colname_value = child.text
            obj.colname = colname_value

        # Parse colnum
        child = ARObject._find_child_element(element, "COLNUM")
        if child is not None:
            colnum_value = child.text
            obj.colnum = colnum_value

        # Parse colsep
        child = ARObject._find_child_element(element, "COLSEP")
        if child is not None:
            colsep_value = child.text
            obj.colsep = colsep_value

        # Parse colwidth
        child = ARObject._find_child_element(element, "COLWIDTH")
        if child is not None:
            colwidth_value = child.text
            obj.colwidth = colwidth_value

        # Parse rowsep
        child = ARObject._find_child_element(element, "ROWSEP")
        if child is not None:
            rowsep_value = child.text
            obj.rowsep = rowsep_value

        return obj



class ColspecBuilder:
    """Builder for Colspec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Colspec = Colspec()

    def build(self) -> Colspec:
        """Build and return Colspec object.

        Returns:
            Colspec instance
        """
        # TODO: Add validation
        return self._obj
