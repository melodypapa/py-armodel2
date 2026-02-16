"""ApplicationRecordDataType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import (
    ApplicationCompositeDataType,
)


class ApplicationRecordDataType(ApplicationCompositeDataType):
    """AUTOSAR ApplicationRecordDataType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("elements", None, False, True, any (ApplicationRecord)),  # elements
    ]

    def __init__(self) -> None:
        """Initialize ApplicationRecordDataType."""
        super().__init__()
        self.elements: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationRecordDataType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationRecordDataType":
        """Create ApplicationRecordDataType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationRecordDataType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationRecordDataType since parent returns ARObject
        return cast("ApplicationRecordDataType", obj)


class ApplicationRecordDataTypeBuilder:
    """Builder for ApplicationRecordDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationRecordDataType = ApplicationRecordDataType()

    def build(self) -> ApplicationRecordDataType:
        """Build and return ApplicationRecordDataType object.

        Returns:
            ApplicationRecordDataType instance
        """
        # TODO: Add validation
        return self._obj
