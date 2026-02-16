"""SecurityEventOneEveryNFilter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecurityEventOneEveryNFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventOneEveryNFilter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("n", None, True, False, None),  # n
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventOneEveryNFilter."""
        super().__init__()
        self.n: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventOneEveryNFilter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventOneEveryNFilter":
        """Create SecurityEventOneEveryNFilter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventOneEveryNFilter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventOneEveryNFilter since parent returns ARObject
        return cast("SecurityEventOneEveryNFilter", obj)


class SecurityEventOneEveryNFilterBuilder:
    """Builder for SecurityEventOneEveryNFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventOneEveryNFilter = SecurityEventOneEveryNFilter()

    def build(self) -> SecurityEventOneEveryNFilter:
        """Build and return SecurityEventOneEveryNFilter object.

        Returns:
            SecurityEventOneEveryNFilter instance
        """
        # TODO: Add validation
        return self._obj
