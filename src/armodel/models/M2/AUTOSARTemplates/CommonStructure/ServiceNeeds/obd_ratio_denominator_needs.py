"""ObdRatioDenominatorNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class ObdRatioDenominatorNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdRatioDenominatorNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("denominator", None, False, False, DiagnosticDenominatorConditionEnum),  # denominator
    ]

    def __init__(self) -> None:
        """Initialize ObdRatioDenominatorNeeds."""
        super().__init__()
        self.denominator: Optional[DiagnosticDenominatorConditionEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ObdRatioDenominatorNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdRatioDenominatorNeeds":
        """Create ObdRatioDenominatorNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ObdRatioDenominatorNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ObdRatioDenominatorNeeds since parent returns ARObject
        return cast("ObdRatioDenominatorNeeds", obj)


class ObdRatioDenominatorNeedsBuilder:
    """Builder for ObdRatioDenominatorNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdRatioDenominatorNeeds = ObdRatioDenominatorNeeds()

    def build(self) -> ObdRatioDenominatorNeeds:
        """Build and return ObdRatioDenominatorNeeds object.

        Returns:
            ObdRatioDenominatorNeeds instance
        """
        # TODO: Add validation
        return self._obj
