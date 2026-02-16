"""ConsumedEventGroup AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "application_endpoint": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationEndpoint,
        ),  # applicationEndpoint
        "auto_require": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # autoRequire
        "event_group": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # eventGroup
        "event_multicasts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ApplicationEndpoint,
        ),  # eventMulticasts
        "pdu_activation_routings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PduActivationRoutingGroup,
        ),  # pduActivationRoutings
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
        "routing_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SoAdRoutingGroup,
        ),  # routingGroups
        "sd_client_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SdClientConfig),
        ),  # sdClientConfig
        "sd_client_timer": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SomeipSdClientEventGroupTimingConfig,
        ),  # sdClientTimer
    }

    def __init__(self) -> None:
        """Initialize ConsumedEventGroup."""
        super().__init__()
        self.application_endpoint: Optional[ApplicationEndpoint] = None
        self.auto_require: Optional[Boolean] = None
        self.event_group: Optional[PositiveInteger] = None
        self.event_multicasts: list[ApplicationEndpoint] = []
        self.pdu_activation_routings: list[PduActivationRoutingGroup] = []
        self.priority: Optional[PositiveInteger] = None
        self.routing_groups: list[SoAdRoutingGroup] = []
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
