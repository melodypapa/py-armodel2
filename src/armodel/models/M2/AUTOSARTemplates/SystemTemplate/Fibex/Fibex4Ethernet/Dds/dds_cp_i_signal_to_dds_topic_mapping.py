"""DdsCpISignalToDdsTopicMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)


class DdsCpISignalToDdsTopicMapping(ARObject):
    """AUTOSAR DdsCpISignalToDdsTopicMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dds_topic", None, False, False, DdsCpTopic),  # ddsTopic
        ("i_signal", None, False, False, ISignal),  # iSignal
    ]

    def __init__(self) -> None:
        """Initialize DdsCpISignalToDdsTopicMapping."""
        super().__init__()
        self.dds_topic: Optional[DdsCpTopic] = None
        self.i_signal: Optional[ISignal] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpISignalToDdsTopicMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpISignalToDdsTopicMapping":
        """Create DdsCpISignalToDdsTopicMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpISignalToDdsTopicMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpISignalToDdsTopicMapping since parent returns ARObject
        return cast("DdsCpISignalToDdsTopicMapping", obj)


class DdsCpISignalToDdsTopicMappingBuilder:
    """Builder for DdsCpISignalToDdsTopicMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpISignalToDdsTopicMapping = DdsCpISignalToDdsTopicMapping()

    def build(self) -> DdsCpISignalToDdsTopicMapping:
        """Build and return DdsCpISignalToDdsTopicMapping object.

        Returns:
            DdsCpISignalToDdsTopicMapping instance
        """
        # TODO: Add validation
        return self._obj
