"""EnumerationMappingTable AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)


class EnumerationMappingTable(PackageableElement):
    """AUTOSAR EnumerationMappingTable."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("entries", None, False, True, any (EnumerationMapping)),  # entries
    ]

    def __init__(self) -> None:
        """Initialize EnumerationMappingTable."""
        super().__init__()
        self.entries: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EnumerationMappingTable to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EnumerationMappingTable":
        """Create EnumerationMappingTable from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EnumerationMappingTable instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EnumerationMappingTable since parent returns ARObject
        return cast("EnumerationMappingTable", obj)


class EnumerationMappingTableBuilder:
    """Builder for EnumerationMappingTable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EnumerationMappingTable = EnumerationMappingTable()

    def build(self) -> EnumerationMappingTable:
        """Build and return EnumerationMappingTable object.

        Returns:
            EnumerationMappingTable instance
        """
        # TODO: Add validation
        return self._obj
