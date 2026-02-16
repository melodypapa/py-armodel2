"""ErrorTracerNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import (
    TracedFailure,
)


class ErrorTracerNeeds(ServiceNeeds):
    """AUTOSAR ErrorTracerNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("traced_failures", None, False, True, TracedFailure),  # tracedFailures
    ]

    def __init__(self) -> None:
        """Initialize ErrorTracerNeeds."""
        super().__init__()
        self.traced_failures: list[TracedFailure] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ErrorTracerNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ErrorTracerNeeds":
        """Create ErrorTracerNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ErrorTracerNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ErrorTracerNeeds since parent returns ARObject
        return cast("ErrorTracerNeeds", obj)


class ErrorTracerNeedsBuilder:
    """Builder for ErrorTracerNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ErrorTracerNeeds = ErrorTracerNeeds()

    def build(self) -> ErrorTracerNeeds:
        """Build and return ErrorTracerNeeds object.

        Returns:
            ErrorTracerNeeds instance
        """
        # TODO: Add validation
        return self._obj
