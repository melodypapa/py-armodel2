"""EnumerationMappingEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class EnumerationMappingEntry(ARObject):
    """AUTOSAR EnumerationMappingEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("enumerator", None, True, False, None),  # enumerator
        ("numerical_value", None, True, False, None),  # numericalValue
    ]

    def __init__(self) -> None:
        """Initialize EnumerationMappingEntry."""
        super().__init__()
        self.enumerator: NameToken = None
        self.numerical_value: PositiveInteger = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EnumerationMappingEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EnumerationMappingEntry":
        """Create EnumerationMappingEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EnumerationMappingEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EnumerationMappingEntry since parent returns ARObject
        return cast("EnumerationMappingEntry", obj)


class EnumerationMappingEntryBuilder:
    """Builder for EnumerationMappingEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EnumerationMappingEntry = EnumerationMappingEntry()

    def build(self) -> EnumerationMappingEntry:
        """Build and return EnumerationMappingEntry object.

        Returns:
            EnumerationMappingEntry instance
        """
        # TODO: Add validation
        return self._obj
