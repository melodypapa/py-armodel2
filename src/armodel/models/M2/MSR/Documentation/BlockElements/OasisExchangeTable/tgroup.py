"""Tgroup AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "align": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AlignEnum,
        ),  # align
        "cols": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # cols
        "colsep": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # colsep
        "colspecs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Colspec,
        ),  # colspecs
        "rowsep": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rowsep
        "tbody": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Tbody,
        ),  # tbody
        "tfoot": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Tbody,
        ),  # tfoot
        "thead": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Tbody,
        ),  # thead
    }

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
