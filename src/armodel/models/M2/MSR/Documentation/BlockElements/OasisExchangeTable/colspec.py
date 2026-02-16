"""Colspec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
    TableSeparatorString,
)


class Colspec(ARObject):
    """AUTOSAR Colspec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("align", None, False, False, AlignEnum),  # align
        ("colname", None, True, False, None),  # colname
        ("colnum", None, True, False, None),  # colnum
        ("colsep", None, True, False, None),  # colsep
        ("colwidth", None, True, False, None),  # colwidth
        ("rowsep", None, True, False, None),  # rowsep
    ]

    def __init__(self) -> None:
        """Initialize Colspec."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.colname: Optional[String] = None
        self.colnum: Optional[String] = None
        self.colsep: Optional[TableSeparatorString] = None
        self.colwidth: Optional[String] = None
        self.rowsep: Optional[TableSeparatorString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Colspec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Colspec":
        """Create Colspec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Colspec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Colspec since parent returns ARObject
        return cast("Colspec", obj)


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
