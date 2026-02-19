"""EventHandler AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 492)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consumed_event_group_refs: list[ARRef]
    event_group: Optional[PositiveInteger]
    event_multicast: Optional[ApplicationEndpoint]
    multicast: Optional[PositiveInteger]
    pdu_activation_routings: list[PduActivationRoutingGroup]
    routing_group_refs: list[ARRef]
    sd_server_config: Optional[Any]
    sd_server_eg: Optional[SomeipSdServerEventGroupTimingConfig]
    def __init__(self) -> None:
        """Initialize EventHandler."""
        super().__init__()
        self.consumed_event_group_refs: list[ARRef] = []
        self.event_group: Optional[PositiveInteger] = None
        self.event_multicast: Optional[ApplicationEndpoint] = None
        self.multicast: Optional[PositiveInteger] = None
        self.pdu_activation_routings: list[PduActivationRoutingGroup] = []
        self.routing_group_refs: list[ARRef] = []
        self.sd_server_config: Optional[Any] = None
        self.sd_server_eg: Optional[SomeipSdServerEventGroupTimingConfig] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EventHandler":
        """Deserialize XML element to EventHandler object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EventHandler object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse consumed_event_group_refs (list)
        obj.consumed_event_group_refs = []
        for child in ARObject._find_all_child_elements(element, "CONSUMED-EVENT-GROUPS"):
            consumed_event_group_refs_value = ARObject._deserialize_by_tag(child, "ConsumedEventGroup")
            obj.consumed_event_group_refs.append(consumed_event_group_refs_value)

        # Parse event_group
        child = ARObject._find_child_element(element, "EVENT-GROUP")
        if child is not None:
            event_group_value = child.text
            obj.event_group = event_group_value

        # Parse event_multicast
        child = ARObject._find_child_element(element, "EVENT-MULTICAST")
        if child is not None:
            event_multicast_value = ARObject._deserialize_by_tag(child, "ApplicationEndpoint")
            obj.event_multicast = event_multicast_value

        # Parse multicast
        child = ARObject._find_child_element(element, "MULTICAST")
        if child is not None:
            multicast_value = child.text
            obj.multicast = multicast_value

        # Parse pdu_activation_routings (list)
        obj.pdu_activation_routings = []
        for child in ARObject._find_all_child_elements(element, "PDU-ACTIVATION-ROUTINGS"):
            pdu_activation_routings_value = ARObject._deserialize_by_tag(child, "PduActivationRoutingGroup")
            obj.pdu_activation_routings.append(pdu_activation_routings_value)

        # Parse routing_group_refs (list)
        obj.routing_group_refs = []
        for child in ARObject._find_all_child_elements(element, "ROUTING-GROUPS"):
            routing_group_refs_value = ARObject._deserialize_by_tag(child, "SoAdRoutingGroup")
            obj.routing_group_refs.append(routing_group_refs_value)

        # Parse sd_server_config
        child = ARObject._find_child_element(element, "SD-SERVER-CONFIG")
        if child is not None:
            sd_server_config_value = child.text
            obj.sd_server_config = sd_server_config_value

        # Parse sd_server_eg
        child = ARObject._find_child_element(element, "SD-SERVER-EG")
        if child is not None:
            sd_server_eg_value = ARObject._deserialize_by_tag(child, "SomeipSdServerEventGroupTimingConfig")
            obj.sd_server_eg = sd_server_eg_value

        return obj



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
