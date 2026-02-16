"""SecurityEventStateFilter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.block_state import (
    BlockState,
)


class SecurityEventStateFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventStateFilter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("block_if_states", None, False, True, BlockState),  # blockIfStates
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventStateFilter."""
        super().__init__()
        self.block_if_states: list[BlockState] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventStateFilter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventStateFilter":
        """Create SecurityEventStateFilter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventStateFilter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventStateFilter since parent returns ARObject
        return cast("SecurityEventStateFilter", obj)


class SecurityEventStateFilterBuilder:
    """Builder for SecurityEventStateFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventStateFilter = SecurityEventStateFilter()

    def build(self) -> SecurityEventStateFilter:
        """Build and return SecurityEventStateFilter object.

        Returns:
            SecurityEventStateFilter instance
        """
        # TODO: Add validation
        return self._obj
