"""DdsCpTopic AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_partition import (
    DdsCpPartition,
)


class DdsCpTopic(Identifiable):
    """AUTOSAR DdsCpTopic."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dds_partition", None, False, False, DdsCpPartition),  # ddsPartition
        ("topic_name", None, True, False, None),  # topicName
    ]

    def __init__(self) -> None:
        """Initialize DdsCpTopic."""
        super().__init__()
        self.dds_partition: Optional[DdsCpPartition] = None
        self.topic_name: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpTopic to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpTopic":
        """Create DdsCpTopic from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpTopic instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpTopic since parent returns ARObject
        return cast("DdsCpTopic", obj)


class DdsCpTopicBuilder:
    """Builder for DdsCpTopic."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpTopic = DdsCpTopic()

    def build(self) -> DdsCpTopic:
        """Build and return DdsCpTopic object.

        Returns:
            DdsCpTopic instance
        """
        # TODO: Add validation
        return self._obj
