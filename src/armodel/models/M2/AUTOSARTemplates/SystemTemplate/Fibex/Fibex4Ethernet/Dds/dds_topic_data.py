"""DdsTopicData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 529)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class DdsTopicData(ARObject):
    """AUTOSAR DdsTopicData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    topic_data: Optional[String]
    def __init__(self) -> None:
        """Initialize DdsTopicData."""
        super().__init__()
        self.topic_data: Optional[String] = None
    def serialize(self) -> ET.Element:
        """Serialize DdsTopicData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize topic_data
        if self.topic_data is not None:
            serialized = ARObject._serialize_item(self.topic_data, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOPIC-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsTopicData":
        """Deserialize XML element to DdsTopicData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsTopicData object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse topic_data
        child = ARObject._find_child_element(element, "TOPIC-DATA")
        if child is not None:
            topic_data_value = child.text
            obj.topic_data = topic_data_value

        return obj



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
