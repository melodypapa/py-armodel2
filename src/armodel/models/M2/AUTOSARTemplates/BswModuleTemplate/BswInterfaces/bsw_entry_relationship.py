"""BswEntryRelationship AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_entry_relationship import (
    BswEntryRelationship,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class BswEntryRelationship(ARObject):
    """AUTOSAR BswEntryRelationship."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_entry", None, False, False, BswEntryRelationship),  # bswEntry
        ("from_", 'FROM', False, False, BswModuleEntry),  # from
        ("to", None, False, False, BswModuleEntry),  # to
    ]

    def __init__(self) -> None:
        """Initialize BswEntryRelationship."""
        super().__init__()
        self.bsw_entry: Optional[BswEntryRelationship] = None
        self.from_: Optional[BswModuleEntry] = None
        self.to: Optional[BswModuleEntry] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswEntryRelationship to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEntryRelationship":
        """Create BswEntryRelationship from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswEntryRelationship instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswEntryRelationship since parent returns ARObject
        return cast("BswEntryRelationship", obj)


class BswEntryRelationshipBuilder:
    """Builder for BswEntryRelationship."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswEntryRelationship = BswEntryRelationship()

    def build(self) -> BswEntryRelationship:
        """Build and return BswEntryRelationship object.

        Returns:
            BswEntryRelationship instance
        """
        # TODO: Add validation
        return self._obj
