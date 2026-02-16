"""EventHandler AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_event_group import (
    ConsumedEventGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_activation_routing_group import (
    PduActivationRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.so_ad_routing_group import (
    SoAdRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_server_event_group_timing_config import (
    SomeipSdServerEventGroupTimingConfig,
)


class EventHandler(Identifiable):
    """AUTOSAR EventHandler."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("consumed_event_groups", None, False, True, ConsumedEventGroup),  # consumedEventGroups
        ("event_group", None, True, False, None),  # eventGroup
        ("event_multicast", None, False, False, ApplicationEndpoint),  # eventMulticast
        ("multicast", None, True, False, None),  # multicast
        ("pdu_activation_routings", None, False, True, PduActivationRoutingGroup),  # pduActivationRoutings
        ("routing_groups", None, False, True, SoAdRoutingGroup),  # routingGroups
        ("sd_server_config", None, False, False, any (SdServerConfig)),  # sdServerConfig
        ("sd_server_eg", None, False, False, SomeipSdServerEventGroupTimingConfig),  # sdServerEg
    ]

    def __init__(self) -> None:
        """Initialize EventHandler."""
        super().__init__()
        self.consumed_event_groups: list[ConsumedEventGroup] = []
        self.event_group: Optional[PositiveInteger] = None
        self.event_multicast: Optional[ApplicationEndpoint] = None
        self.multicast: Optional[PositiveInteger] = None
        self.pdu_activation_routings: list[PduActivationRoutingGroup] = []
        self.routing_groups: list[SoAdRoutingGroup] = []
        self.sd_server_config: Optional[Any] = None
        self.sd_server_eg: Optional[SomeipSdServerEventGroupTimingConfig] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EventHandler to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EventHandler":
        """Create EventHandler from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EventHandler instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EventHandler since parent returns ARObject
        return cast("EventHandler", obj)


class EventHandlerBuilder:
    """Builder for EventHandler."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EventHandler = EventHandler()

    def build(self) -> EventHandler:
        """Build and return EventHandler object.

        Returns:
            EventHandler instance
        """
        # TODO: Add validation
        return self._obj
