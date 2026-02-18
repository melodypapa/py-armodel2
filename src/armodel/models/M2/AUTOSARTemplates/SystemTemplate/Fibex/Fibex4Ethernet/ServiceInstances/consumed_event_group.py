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
