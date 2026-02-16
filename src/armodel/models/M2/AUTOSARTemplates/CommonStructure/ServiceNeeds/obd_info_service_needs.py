"""ObdInfoServiceNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class ObdInfoServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdInfoServiceNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ObdInfoServiceNeeds."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ObdInfoServiceNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdInfoServiceNeeds":
        """Create ObdInfoServiceNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ObdInfoServiceNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ObdInfoServiceNeeds since parent returns ARObject
        return cast("ObdInfoServiceNeeds", obj)


class ObdInfoServiceNeedsBuilder:
    """Builder for ObdInfoServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdInfoServiceNeeds = ObdInfoServiceNeeds()

    def build(self) -> ObdInfoServiceNeeds:
        """Build and return ObdInfoServiceNeeds object.

        Returns:
            ObdInfoServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
