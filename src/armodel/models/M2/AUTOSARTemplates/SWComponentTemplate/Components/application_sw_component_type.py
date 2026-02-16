"""ApplicationSwComponentType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)


class ApplicationSwComponentType(AtomicSwComponentType):
    """AUTOSAR ApplicationSwComponentType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ApplicationSwComponentType."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationSwComponentType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationSwComponentType":
        """Create ApplicationSwComponentType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationSwComponentType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationSwComponentType since parent returns ARObject
        return cast("ApplicationSwComponentType", obj)


class ApplicationSwComponentTypeBuilder:
    """Builder for ApplicationSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationSwComponentType = ApplicationSwComponentType()

    def build(self) -> ApplicationSwComponentType:
        """Build and return ApplicationSwComponentType object.

        Returns:
            ApplicationSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
