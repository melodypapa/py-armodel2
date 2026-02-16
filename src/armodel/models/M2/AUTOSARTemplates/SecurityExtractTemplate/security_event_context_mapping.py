"""SecurityEventContextMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_mapping import (
    IdsMapping,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_instance import (
    IdsmInstance,
)


class SecurityEventContextMapping(IdsMapping):
    """AUTOSAR SecurityEventContextMapping."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("filter_chain", None, False, False, any (SecurityEventFilter)),  # filterChain
        ("idsm_instance", None, False, False, IdsmInstance),  # idsmInstance
        ("mapped_securities", None, False, True, any (SecurityEventContext)),  # mappedSecurities
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventContextMapping."""
        super().__init__()
        self.filter_chain: Optional[Any] = None
        self.idsm_instance: Optional[IdsmInstance] = None
        self.mapped_securities: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventContextMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextMapping":
        """Create SecurityEventContextMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventContextMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventContextMapping since parent returns ARObject
        return cast("SecurityEventContextMapping", obj)


class SecurityEventContextMappingBuilder:
    """Builder for SecurityEventContextMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMapping = SecurityEventContextMapping()

    def build(self) -> SecurityEventContextMapping:
        """Build and return SecurityEventContextMapping object.

        Returns:
            SecurityEventContextMapping instance
        """
        # TODO: Add validation
        return self._obj
