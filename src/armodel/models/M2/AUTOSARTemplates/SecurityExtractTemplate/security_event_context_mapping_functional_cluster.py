"""SecurityEventContextMappingFunctionalCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SecurityEventContextMappingFunctionalCluster(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingFunctionalCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("affected", None, True, False, None),  # affected
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingFunctionalCluster."""
        super().__init__()
        self.affected: String = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventContextMappingFunctionalCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMappingFunctionalCluster":
        """Create SecurityEventContextMappingFunctionalCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventContextMappingFunctionalCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventContextMappingFunctionalCluster since parent returns ARObject
        return cast("SecurityEventContextMappingFunctionalCluster", obj)


class SecurityEventContextMappingFunctionalClusterBuilder:
    """Builder for SecurityEventContextMappingFunctionalCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingFunctionalCluster = SecurityEventContextMappingFunctionalCluster()

    def build(self) -> SecurityEventContextMappingFunctionalCluster:
        """Build and return SecurityEventContextMappingFunctionalCluster object.

        Returns:
            SecurityEventContextMappingFunctionalCluster instance
        """
        # TODO: Add validation
        return self._obj
