"""ServiceSwComponentType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)


class ServiceSwComponentType(AtomicSwComponentType):
    """AUTOSAR ServiceSwComponentType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ServiceSwComponentType."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ServiceSwComponentType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServiceSwComponentType":
        """Create ServiceSwComponentType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ServiceSwComponentType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ServiceSwComponentType since parent returns ARObject
        return cast("ServiceSwComponentType", obj)


class ServiceSwComponentTypeBuilder:
    """Builder for ServiceSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceSwComponentType = ServiceSwComponentType()

    def build(self) -> ServiceSwComponentType:
        """Build and return ServiceSwComponentType object.

        Returns:
            ServiceSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
