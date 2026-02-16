"""Entry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("align", None, False, False, AlignEnum),  # align
        ("bgcolor", None, True, False, None),  # bgcolor
        ("colname", None, True, False, None),  # colname
        ("colsep", None, True, False, None),  # colsep
        ("entry_contents", None, False, False, DocumentationBlock),  # entryContents
        ("morerows", None, True, False, None),  # morerows
        ("nameend", None, True, False, None),  # nameend
        ("namest", None, True, False, None),  # namest
        ("rotate", None, True, False, None),  # rotate
        ("rowsep", None, True, False, None),  # rowsep
        ("spanname", None, True, False, None),  # spanname
        ("valign", None, False, False, ValignEnum),  # valign
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Entry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Entry":
        """Create Entry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Entry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Entry since parent returns ARObject
        return cast("Entry", obj)


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
