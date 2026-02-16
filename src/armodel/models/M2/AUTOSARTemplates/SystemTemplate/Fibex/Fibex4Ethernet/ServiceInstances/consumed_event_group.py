"""ConsumedEventGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("application_endpoint", None, False, False, ApplicationEndpoint),  # applicationEndpoint
        ("auto_require", None, True, False, None),  # autoRequire
        ("event_group", None, True, False, None),  # eventGroup
        ("event_multicasts", None, False, True, ApplicationEndpoint),  # eventMulticasts
        ("pdu_activation_routings", None, False, True, PduActivationRoutingGroup),  # pduActivationRoutings
        ("priority", None, True, False, None),  # priority
        ("routing_groups", None, False, True, SoAdRoutingGroup),  # routingGroups
        ("sd_client_config", None, False, False, any (SdClientConfig)),  # sdClientConfig
        ("sd_client_timer", None, False, False, SomeipSdClientEventGroupTimingConfig),  # sdClientTimer
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConsumedEventGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsumedEventGroup":
        """Create ConsumedEventGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConsumedEventGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConsumedEventGroup since parent returns ARObject
        return cast("ConsumedEventGroup", obj)


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
