"""SecurityEventContextMappingBswModule AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SecurityEventContextMappingBswModule(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingBswModule."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("affected_bsw", None, True, False, None),  # affectedBsw
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingBswModule."""
        super().__init__()
        self.affected_bsw: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventContextMappingBswModule to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMappingBswModule":
        """Create SecurityEventContextMappingBswModule from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventContextMappingBswModule instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventContextMappingBswModule since parent returns ARObject
        return cast("SecurityEventContextMappingBswModule", obj)


class SecurityEventContextMappingBswModuleBuilder:
    """Builder for SecurityEventContextMappingBswModule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingBswModule = SecurityEventContextMappingBswModule()

    def build(self) -> SecurityEventContextMappingBswModule:
        """Build and return SecurityEventContextMappingBswModule object.

        Returns:
            SecurityEventContextMappingBswModule instance
        """
        # TODO: Add validation
        return self._obj
