"""BswEntryRelationshipSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_relationship import (
    BswEntryRelationship,
)


class BswEntryRelationshipSet(ARElement):
    """AUTOSAR BswEntryRelationshipSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_entry_relationships", None, False, True, BswEntryRelationship),  # bswEntryRelationships
    ]

    def __init__(self) -> None:
        """Initialize BswEntryRelationshipSet."""
        super().__init__()
        self.bsw_entry_relationships: list[BswEntryRelationship] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswEntryRelationshipSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEntryRelationshipSet":
        """Create BswEntryRelationshipSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswEntryRelationshipSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswEntryRelationshipSet since parent returns ARObject
        return cast("BswEntryRelationshipSet", obj)


class BswEntryRelationshipSetBuilder:
    """Builder for BswEntryRelationshipSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswEntryRelationshipSet = BswEntryRelationshipSet()

    def build(self) -> BswEntryRelationshipSet:
        """Build and return BswEntryRelationshipSet object.

        Returns:
            BswEntryRelationshipSet instance
        """
        # TODO: Add validation
        return self._obj
