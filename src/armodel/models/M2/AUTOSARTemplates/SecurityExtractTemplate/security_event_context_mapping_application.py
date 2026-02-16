"""SecurityEventContextMappingApplication AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SecurityEventContextMappingApplication(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingApplication."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("affected", None, True, False, None),  # affected
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingApplication."""
        super().__init__()
        self.affected: String = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventContextMappingApplication to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMappingApplication":
        """Create SecurityEventContextMappingApplication from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventContextMappingApplication instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventContextMappingApplication since parent returns ARObject
        return cast("SecurityEventContextMappingApplication", obj)


class SecurityEventContextMappingApplicationBuilder:
    """Builder for SecurityEventContextMappingApplication."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingApplication = SecurityEventContextMappingApplication()

    def build(self) -> SecurityEventContextMappingApplication:
        """Build and return SecurityEventContextMappingApplication object.

        Returns:
            SecurityEventContextMappingApplication instance
        """
        # TODO: Add validation
        return self._obj
