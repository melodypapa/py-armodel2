"""ServiceInstanceCollectionSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)


class ServiceInstanceCollectionSet(FibexElement):
    """AUTOSAR ServiceInstanceCollectionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("service_instances", None, False, True, AbstractServiceInstance),  # serviceInstances
    ]

    def __init__(self) -> None:
        """Initialize ServiceInstanceCollectionSet."""
        super().__init__()
        self.service_instances: list[AbstractServiceInstance] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ServiceInstanceCollectionSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServiceInstanceCollectionSet":
        """Create ServiceInstanceCollectionSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ServiceInstanceCollectionSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ServiceInstanceCollectionSet since parent returns ARObject
        return cast("ServiceInstanceCollectionSet", obj)


class ServiceInstanceCollectionSetBuilder:
    """Builder for ServiceInstanceCollectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceInstanceCollectionSet = ServiceInstanceCollectionSet()

    def build(self) -> ServiceInstanceCollectionSet:
        """Build and return ServiceInstanceCollectionSet object.

        Returns:
            ServiceInstanceCollectionSet instance
        """
        # TODO: Add validation
        return self._obj
