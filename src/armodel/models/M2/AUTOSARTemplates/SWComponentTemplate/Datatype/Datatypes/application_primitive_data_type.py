"""ApplicationPrimitiveDataType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)


class ApplicationPrimitiveDataType(ApplicationDataType):
    """AUTOSAR ApplicationPrimitiveDataType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ApplicationPrimitiveDataType."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationPrimitiveDataType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationPrimitiveDataType":
        """Create ApplicationPrimitiveDataType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationPrimitiveDataType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationPrimitiveDataType since parent returns ARObject
        return cast("ApplicationPrimitiveDataType", obj)


class ApplicationPrimitiveDataTypeBuilder:
    """Builder for ApplicationPrimitiveDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationPrimitiveDataType = ApplicationPrimitiveDataType()

    def build(self) -> ApplicationPrimitiveDataType:
        """Build and return ApplicationPrimitiveDataType object.

        Returns:
            ApplicationPrimitiveDataType instance
        """
        # TODO: Add validation
        return self._obj
