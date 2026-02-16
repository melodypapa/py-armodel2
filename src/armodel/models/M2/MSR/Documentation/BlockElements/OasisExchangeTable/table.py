"""Table AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
    TableSeparatorString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.caption import (
    Caption,
)


class Table(Paginateable):
    """AUTOSAR Table."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("colsep", None, True, False, None),  # colsep
        ("float", None, False, False, FloatEnum),  # float
        ("frame", None, False, False, FrameEnum),  # frame
        ("help_entry", None, True, False, None),  # helpEntry
        ("orient", None, False, False, any (OrientEnum)),  # orient
        ("pgwide", None, True, False, None),  # pgwide
        ("rowsep", None, True, False, None),  # rowsep
        ("table_caption", None, False, False, Caption),  # tableCaption
        ("tabstyle", None, True, False, None),  # tabstyle
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Table to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Table":
        """Create Table from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Table instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Table since parent returns ARObject
        return cast("Table", obj)


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
