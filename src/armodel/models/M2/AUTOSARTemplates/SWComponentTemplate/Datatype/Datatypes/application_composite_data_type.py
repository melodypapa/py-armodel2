"""ApplicationCompositeDataType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)


class ApplicationCompositeDataType(ApplicationDataType):
    """AUTOSAR ApplicationCompositeDataType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ApplicationCompositeDataType."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationCompositeDataType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationCompositeDataType":
        """Create ApplicationCompositeDataType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationCompositeDataType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationCompositeDataType since parent returns ARObject
        return cast("ApplicationCompositeDataType", obj)


class ApplicationCompositeDataTypeBuilder:
    """Builder for ApplicationCompositeDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeDataType = ApplicationCompositeDataType()

    def build(self) -> ApplicationCompositeDataType:
        """Build and return ApplicationCompositeDataType object.

        Returns:
            ApplicationCompositeDataType instance
        """
        # TODO: Add validation
        return self._obj
