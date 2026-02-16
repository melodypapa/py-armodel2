"""UserDefinedTransformationISignalProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class UserDefinedTransformationISignalProps(ARObject):
    """AUTOSAR UserDefinedTransformationISignalProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationISignalProps."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UserDefinedTransformationISignalProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedTransformationISignalProps":
        """Create UserDefinedTransformationISignalProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UserDefinedTransformationISignalProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UserDefinedTransformationISignalProps since parent returns ARObject
        return cast("UserDefinedTransformationISignalProps", obj)


class UserDefinedTransformationISignalPropsBuilder:
    """Builder for UserDefinedTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationISignalProps = UserDefinedTransformationISignalProps()

    def build(self) -> UserDefinedTransformationISignalProps:
        """Build and return UserDefinedTransformationISignalProps object.

        Returns:
            UserDefinedTransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
