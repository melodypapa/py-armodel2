"""DdsTopicData AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class DdsTopicData(ARObject):
    """AUTOSAR DdsTopicData."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("topic_data", None, True, False, None),  # topicData
    ]

    def __init__(self) -> None:
        """Initialize DdsTopicData."""
        super().__init__()
        self.topic_data: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsTopicData to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsTopicData":
        """Create DdsTopicData from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsTopicData instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsTopicData since parent returns ARObject
        return cast("DdsTopicData", obj)


class DdsTopicDataBuilder:
    """Builder for DdsTopicData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsTopicData = DdsTopicData()

    def build(self) -> DdsTopicData:
        """Build and return DdsTopicData object.

        Returns:
            DdsTopicData instance
        """
        # TODO: Add validation
        return self._obj
