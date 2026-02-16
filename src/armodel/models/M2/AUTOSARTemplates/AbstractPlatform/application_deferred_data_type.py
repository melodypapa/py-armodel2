"""ApplicationDeferredDataType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)


class ApplicationDeferredDataType(ApplicationDataType):
    """AUTOSAR ApplicationDeferredDataType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ApplicationDeferredDataType."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationDeferredDataType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationDeferredDataType":
        """Create ApplicationDeferredDataType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationDeferredDataType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationDeferredDataType since parent returns ARObject
        return cast("ApplicationDeferredDataType", obj)


class ApplicationDeferredDataTypeBuilder:
    """Builder for ApplicationDeferredDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationDeferredDataType = ApplicationDeferredDataType()

    def build(self) -> ApplicationDeferredDataType:
        """Build and return ApplicationDeferredDataType object.

        Returns:
            ApplicationDeferredDataType instance
        """
        # TODO: Add validation
        return self._obj
