"""UserDefinedTransformationProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)


class UserDefinedTransformationProps(TransformationProps):
    """AUTOSAR UserDefinedTransformationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationProps."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UserDefinedTransformationProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedTransformationProps":
        """Create UserDefinedTransformationProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UserDefinedTransformationProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UserDefinedTransformationProps since parent returns ARObject
        return cast("UserDefinedTransformationProps", obj)


class UserDefinedTransformationPropsBuilder:
    """Builder for UserDefinedTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationProps = UserDefinedTransformationProps()

    def build(self) -> UserDefinedTransformationProps:
        """Build and return UserDefinedTransformationProps object.

        Returns:
            UserDefinedTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
