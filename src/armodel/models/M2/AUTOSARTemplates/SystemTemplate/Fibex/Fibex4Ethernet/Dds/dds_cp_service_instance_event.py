"""DdsCpServiceInstanceEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DdsCpServiceInstanceEvent(ARObject):
    """AUTOSAR DdsCpServiceInstanceEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dds_event", None, False, False, PduTriggering),  # ddsEvent
        ("dds_event_qos", None, False, False, DdsCpQosProfile),  # ddsEventQos
        ("dds_event_topic", None, False, False, DdsCpTopic),  # ddsEventTopic
    ]

    def __init__(self) -> None:
        """Initialize DdsCpServiceInstanceEvent."""
        super().__init__()
        self.dds_event: Optional[PduTriggering] = None
        self.dds_event_qos: Optional[DdsCpQosProfile] = None
        self.dds_event_topic: Optional[DdsCpTopic] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpServiceInstanceEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpServiceInstanceEvent":
        """Create DdsCpServiceInstanceEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpServiceInstanceEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpServiceInstanceEvent since parent returns ARObject
        return cast("DdsCpServiceInstanceEvent", obj)


class DdsCpServiceInstanceEventBuilder:
    """Builder for DdsCpServiceInstanceEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpServiceInstanceEvent = DdsCpServiceInstanceEvent()

    def build(self) -> DdsCpServiceInstanceEvent:
        """Build and return DdsCpServiceInstanceEvent object.

        Returns:
            DdsCpServiceInstanceEvent instance
        """
        # TODO: Add validation
        return self._obj
