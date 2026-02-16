"""UserDefinedTransformationComSpecProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)


class UserDefinedTransformationComSpecProps(TransformationComSpecProps):
    """AUTOSAR UserDefinedTransformationComSpecProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationComSpecProps."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UserDefinedTransformationComSpecProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedTransformationComSpecProps":
        """Create UserDefinedTransformationComSpecProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UserDefinedTransformationComSpecProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UserDefinedTransformationComSpecProps since parent returns ARObject
        return cast("UserDefinedTransformationComSpecProps", obj)


class UserDefinedTransformationComSpecPropsBuilder:
    """Builder for UserDefinedTransformationComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationComSpecProps = UserDefinedTransformationComSpecProps()

    def build(self) -> UserDefinedTransformationComSpecProps:
        """Build and return UserDefinedTransformationComSpecProps object.

        Returns:
            UserDefinedTransformationComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
