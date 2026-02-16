"""ApplicationCompositeDataTypeSubElementRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)


class ApplicationCompositeDataTypeSubElementRef(SubElementRef):
    """AUTOSAR ApplicationCompositeDataTypeSubElementRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("application", None, False, False, any (ApplicationComposite)),  # application
    ]

    def __init__(self) -> None:
        """Initialize ApplicationCompositeDataTypeSubElementRef."""
        super().__init__()
        self.application: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationCompositeDataTypeSubElementRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationCompositeDataTypeSubElementRef":
        """Create ApplicationCompositeDataTypeSubElementRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationCompositeDataTypeSubElementRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationCompositeDataTypeSubElementRef since parent returns ARObject
        return cast("ApplicationCompositeDataTypeSubElementRef", obj)


class ApplicationCompositeDataTypeSubElementRefBuilder:
    """Builder for ApplicationCompositeDataTypeSubElementRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeDataTypeSubElementRef = ApplicationCompositeDataTypeSubElementRef()

    def build(self) -> ApplicationCompositeDataTypeSubElementRef:
        """Build and return ApplicationCompositeDataTypeSubElementRef object.

        Returns:
            ApplicationCompositeDataTypeSubElementRef instance
        """
        # TODO: Add validation
        return self._obj
