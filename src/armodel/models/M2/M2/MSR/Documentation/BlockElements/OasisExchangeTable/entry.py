"""Entry AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
    TableSeparatorString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class Entry(ARObject):
    """AUTOSAR Entry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "align": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AlignEnum,
        ),  # align
        "bgcolor": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # bgcolor
        "colname": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # colname
        "colsep": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # colsep
        "entry_contents": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=DocumentationBlock,
        ),  # entryContents
        "morerows": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # morerows
        "nameend": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nameend
        "namest": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # namest
        "rotate": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rotate
        "rowsep": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rowsep
        "spanname": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # spanname
        "valign": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValignEnum,
        ),  # valign
    }

    def __init__(self) -> None:
        """Initialize Entry."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.bgcolor: String = None
        self.colname: Optional[String] = None
        self.colsep: Optional[TableSeparatorString] = None
        self.entry_contents: DocumentationBlock = None
        self.morerows: Optional[String] = None
        self.nameend: Optional[String] = None
        self.namest: Optional[String] = None
        self.rotate: Optional[String] = None
        self.rowsep: Optional[TableSeparatorString] = None
        self.spanname: Optional[String] = None
        self.valign: Optional[ValignEnum] = None


class EntryBuilder:
    """Builder for Entry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Entry = Entry()

    def build(self) -> Entry:
        """Build and return Entry object.

        Returns:
            Entry instance
        """
        # TODO: Add validation
        return self._obj
