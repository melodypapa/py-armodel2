"""ConsumedEventGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 978)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 504)

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
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_activation_routing_group import (
    PduActivationRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.so_ad_routing_group import (
    SoAdRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_client_event_group_timing_config import (
    SomeipSdClientEventGroupTimingConfig,
)


class ConsumedEventGroup(Identifiable):
    """AUTOSAR ConsumedEventGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_endpoint: Optional[ApplicationEndpoint]
    auto_require: Optional[Boolean]
    event_group: Optional[PositiveInteger]
    event_multicasts: list[ApplicationEndpoint]
    pdu_activation_routings: list[PduActivationRoutingGroup]
    priority: Optional[PositiveInteger]
    routing_group_refs: list[ARRef]
    sd_client_config: Optional[Any]
    sd_client_timer: Optional[SomeipSdClientEventGroupTimingConfig]
    def __init__(self) -> None:
        """Initialize ConsumedEventGroup."""
        super().__init__()
        self.application_endpoint: Optional[ApplicationEndpoint] = None
        self.auto_require: Optional[Boolean] = None
        self.event_group: Optional[PositiveInteger] = None
        self.event_multicasts: list[ApplicationEndpoint] = []
        self.pdu_activation_routings: list[PduActivationRoutingGroup] = []
        self.priority: Optional[PositiveInteger] = None
        self.routing_group_refs: list[ARRef] = []
        self.sd_client_config: Optional[Any] = None
        self.sd_client_timer: Optional[SomeipSdClientEventGroupTimingConfig] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsumedEventGroup":
        """Deserialize XML element to ConsumedEventGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsumedEventGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsumedEventGroup, cls).deserialize(element)

        # Parse application_endpoint
        child = ARObject._find_child_element(element, "APPLICATION-ENDPOINT")
        if child is not None:
            application_endpoint_value = ARObject._deserialize_by_tag(child, "ApplicationEndpoint")
            obj.application_endpoint = application_endpoint_value

        # Parse auto_require
        child = ARObject._find_child_element(element, "AUTO-REQUIRE")
        if child is not None:
            auto_require_value = child.text
            obj.auto_require = auto_require_value

        # Parse event_group
        child = ARObject._find_child_element(element, "EVENT-GROUP")
        if child is not None:
            event_group_value = child.text
            obj.event_group = event_group_value

        # Parse event_multicasts (list from container "EVENT-MULTICASTS")
        obj.event_multicasts = []
        container = ARObject._find_child_element(element, "EVENT-MULTICASTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.event_multicasts.append(child_value)

        # Parse pdu_activation_routings (list from container "PDU-ACTIVATION-ROUTINGS")
        obj.pdu_activation_routings = []
        container = ARObject._find_child_element(element, "PDU-ACTIVATION-ROUTINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pdu_activation_routings.append(child_value)

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse routing_group_refs (list from container "ROUTING-GROUPS")
        obj.routing_group_refs = []
        container = ARObject._find_child_element(element, "ROUTING-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.routing_group_refs.append(child_value)

        # Parse sd_client_config
        child = ARObject._find_child_element(element, "SD-CLIENT-CONFIG")
        if child is not None:
            sd_client_config_value = child.text
            obj.sd_client_config = sd_client_config_value

        # Parse sd_client_timer
        child = ARObject._find_child_element(element, "SD-CLIENT-TIMER")
        if child is not None:
            sd_client_timer_value = ARObject._deserialize_by_tag(child, "SomeipSdClientEventGroupTimingConfig")
            obj.sd_client_timer = sd_client_timer_value

        return obj



class ConsumedEventGroupBuilder:
    """Builder for ConsumedEventGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsumedEventGroup = ConsumedEventGroup()

    def build(self) -> ConsumedEventGroup:
        """Build and return ConsumedEventGroup object.

        Returns:
            ConsumedEventGroup instance
        """
        # TODO: Add validation
        return self._obj
