"""SecurityEventAggregationFilter AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class SecurityEventAggregationFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventAggregationFilter."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_data", None, False, False, any (SecurityEventContext)),  # contextData
        ("minimum", None, True, False, None),  # minimum
    ]

    def __init__(self) -> None:
        """Initialize SecurityEventAggregationFilter."""
        super().__init__()
        self.context_data: Optional[Any] = None
        self.minimum: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecurityEventAggregationFilter to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventAggregationFilter":
        """Create SecurityEventAggregationFilter from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecurityEventAggregationFilter instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecurityEventAggregationFilter since parent returns ARObject
        return cast("SecurityEventAggregationFilter", obj)


class SecurityEventAggregationFilterBuilder:
    """Builder for SecurityEventAggregationFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventAggregationFilter = SecurityEventAggregationFilter()

    def build(self) -> SecurityEventAggregationFilter:
        """Build and return SecurityEventAggregationFilter object.

        Returns:
            SecurityEventAggregationFilter instance
        """
        # TODO: Add validation
        return self._obj
