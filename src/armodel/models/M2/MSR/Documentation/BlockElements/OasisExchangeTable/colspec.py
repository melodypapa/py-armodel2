"""Colspec AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
    TableSeparatorString,
)


class Colspec(ARObject):
    """AUTOSAR Colspec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "align": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AlignEnum,
        ),  # align
        "colname": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # colname
        "colnum": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # colnum
        "colsep": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # colsep
        "colwidth": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # colwidth
        "rowsep": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rowsep
    }

    def __init__(self) -> None:
        """Initialize Colspec."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.colname: Optional[String] = None
        self.colnum: Optional[String] = None
        self.colsep: Optional[TableSeparatorString] = None
        self.colwidth: Optional[String] = None
        self.rowsep: Optional[TableSeparatorString] = None


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
