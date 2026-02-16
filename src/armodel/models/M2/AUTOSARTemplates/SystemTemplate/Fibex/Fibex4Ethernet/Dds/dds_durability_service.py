"""DdsDurabilityService AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsDurabilityService(ARObject):
    """AUTOSAR DdsDurabilityService."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("durability", None, True, False, None),  # durability
    ]

    def __init__(self) -> None:
        """Initialize DdsDurabilityService."""
        super().__init__()
        self.durability: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsDurabilityService to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDurabilityService":
        """Create DdsDurabilityService from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsDurabilityService instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsDurabilityService since parent returns ARObject
        return cast("DdsDurabilityService", obj)


class DdsDurabilityServiceBuilder:
    """Builder for DdsDurabilityService."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDurabilityService = DdsDurabilityService()

    def build(self) -> DdsDurabilityService:
        """Build and return DdsDurabilityService object.

        Returns:
            DdsDurabilityService instance
        """
        # TODO: Add validation
        return self._obj
