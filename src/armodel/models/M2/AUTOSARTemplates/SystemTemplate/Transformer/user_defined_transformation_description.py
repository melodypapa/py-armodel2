"""UserDefinedTransformationDescription AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)


class UserDefinedTransformationDescription(TransformationDescription):
    """AUTOSAR UserDefinedTransformationDescription."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationDescription."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UserDefinedTransformationDescription to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedTransformationDescription":
        """Create UserDefinedTransformationDescription from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UserDefinedTransformationDescription instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UserDefinedTransformationDescription since parent returns ARObject
        return cast("UserDefinedTransformationDescription", obj)


class UserDefinedTransformationDescriptionBuilder:
    """Builder for UserDefinedTransformationDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationDescription = UserDefinedTransformationDescription()

    def build(self) -> UserDefinedTransformationDescription:
        """Build and return UserDefinedTransformationDescription object.

        Returns:
            UserDefinedTransformationDescription instance
        """
        # TODO: Add validation
        return self._obj
