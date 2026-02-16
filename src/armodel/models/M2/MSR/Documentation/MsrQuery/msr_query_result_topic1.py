"""MsrQueryResultTopic1 AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class MsrQueryResultTopic1(ARObject):
    """AUTOSAR MsrQueryResultTopic1."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize MsrQueryResultTopic1."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MsrQueryResultTopic1 to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryResultTopic1":
        """Create MsrQueryResultTopic1 from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MsrQueryResultTopic1 instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MsrQueryResultTopic1 since parent returns ARObject
        return cast("MsrQueryResultTopic1", obj)


class MsrQueryResultTopic1Builder:
    """Builder for MsrQueryResultTopic1."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryResultTopic1 = MsrQueryResultTopic1()

    def build(self) -> MsrQueryResultTopic1:
        """Build and return MsrQueryResultTopic1 object.

        Returns:
            MsrQueryResultTopic1 instance
        """
        # TODO: Add validation
        return self._obj
