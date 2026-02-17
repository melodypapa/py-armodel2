"""Table AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 332)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "colsep": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # colsep
        "float": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=FloatEnum,
        ),  # float
        "frame": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FrameEnum,
        ),  # frame
        "help_entry": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # helpEntry
        "orient": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # orient
        "pgwide": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pgwide
        "rowsep": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rowsep
        "table_caption": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Caption,
        ),  # tableCaption
        "tabstyle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tabstyle
    }

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
