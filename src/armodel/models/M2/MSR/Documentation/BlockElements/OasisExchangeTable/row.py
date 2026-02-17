"""Row AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 336)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TableSeparatorString,
)


class Row(Paginateable):
    """AUTOSAR Row."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "rowsep": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rowsep
        "valign": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValignEnum,
        ),  # valign
    }

    def __init__(self) -> None:
        """Initialize Row."""
        super().__init__()
        self.rowsep: Optional[TableSeparatorString] = None
        self.valign: Optional[ValignEnum] = None


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
