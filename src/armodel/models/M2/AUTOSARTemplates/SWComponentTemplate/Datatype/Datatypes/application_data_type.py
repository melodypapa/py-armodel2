"""ApplicationDataType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
    AutosarDataType,
)


class ApplicationDataType(AutosarDataType):
    """AUTOSAR ApplicationDataType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ApplicationDataType."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationDataType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationDataType":
        """Create ApplicationDataType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationDataType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationDataType since parent returns ARObject
        return cast("ApplicationDataType", obj)


class ApplicationDataTypeBuilder:
    """Builder for ApplicationDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationDataType = ApplicationDataType()

    def build(self) -> ApplicationDataType:
        """Build and return ApplicationDataType object.

        Returns:
            ApplicationDataType instance
        """
        # TODO: Add validation
        return self._obj
