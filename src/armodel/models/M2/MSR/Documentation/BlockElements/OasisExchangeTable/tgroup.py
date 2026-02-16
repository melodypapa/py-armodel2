"""Tgroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("align", None, False, False, AlignEnum),  # align
        ("cols", None, True, False, None),  # cols
        ("colsep", None, True, False, None),  # colsep
        ("colspecs", None, False, True, Colspec),  # colspecs
        ("rowsep", None, True, False, None),  # rowsep
        ("tbody", None, False, False, Tbody),  # tbody
        ("tfoot", None, False, False, Tbody),  # tfoot
        ("thead", None, False, False, Tbody),  # thead
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Tgroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Tgroup":
        """Create Tgroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Tgroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Tgroup since parent returns ARObject
        return cast("Tgroup", obj)


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
