"""ConsumedProvidedServiceInstanceGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)


class ConsumedProvidedServiceInstanceGroup(FibexElement):
    """AUTOSAR ConsumedProvidedServiceInstanceGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("consumed_services", None, False, True, any (ConsumedService)),  # consumedServices
        ("provided_services", None, False, True, any (ProvidedService)),  # providedServices
    ]

    def __init__(self) -> None:
        """Initialize ConsumedProvidedServiceInstanceGroup."""
        super().__init__()
        self.consumed_services: list[Any] = []
        self.provided_services: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConsumedProvidedServiceInstanceGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsumedProvidedServiceInstanceGroup":
        """Create ConsumedProvidedServiceInstanceGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConsumedProvidedServiceInstanceGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConsumedProvidedServiceInstanceGroup since parent returns ARObject
        return cast("ConsumedProvidedServiceInstanceGroup", obj)


class ConsumedProvidedServiceInstanceGroupBuilder:
    """Builder for ConsumedProvidedServiceInstanceGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsumedProvidedServiceInstanceGroup = ConsumedProvidedServiceInstanceGroup()

    def build(self) -> ConsumedProvidedServiceInstanceGroup:
        """Build and return ConsumedProvidedServiceInstanceGroup object.

        Returns:
            ConsumedProvidedServiceInstanceGroup instance
        """
        # TODO: Add validation
        return self._obj
