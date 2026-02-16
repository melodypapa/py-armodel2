"""GlobalTimeDomain AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_domain import (
    GlobalTimeDomain,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_gateway import (
    GlobalTimeGateway,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.network_segment_identification import (
    NetworkSegmentIdentification,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class GlobalTimeDomain(FibexElement):
    """AUTOSAR GlobalTimeDomain."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("debounce_time", None, True, False, None),  # debounceTime
        ("domain_id", None, True, False, None),  # domainId
        ("gateways", None, False, True, GlobalTimeGateway),  # gateways
        ("global_time", None, False, False, AbstractGlobalTimeDomainProps),  # globalTime
        ("global_time_master", None, False, False, GlobalTimeMaster),  # globalTimeMaster
        ("global_time_subs", None, False, True, GlobalTimeDomain),  # globalTimeSubs
        ("network", None, False, False, NetworkSegmentIdentification),  # network
        ("offset_time", None, False, False, GlobalTimeDomain),  # offsetTime
        ("pdu_triggering", None, False, False, PduTriggering),  # pduTriggering
        ("slaves", None, False, True, GlobalTimeSlave),  # slaves
        ("sync_loss", None, True, False, None),  # syncLoss
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeDomain."""
        super().__init__()
        self.debounce_time: Optional[TimeValue] = None
        self.domain_id: Optional[PositiveInteger] = None
        self.gateways: list[GlobalTimeGateway] = []
        self.global_time: Optional[AbstractGlobalTimeDomainProps] = None
        self.global_time_master: Optional[GlobalTimeMaster] = None
        self.global_time_subs: list[GlobalTimeDomain] = []
        self.network: Optional[NetworkSegmentIdentification] = None
        self.offset_time: Optional[GlobalTimeDomain] = None
        self.pdu_triggering: Optional[PduTriggering] = None
        self.slaves: list[GlobalTimeSlave] = []
        self.sync_loss: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeDomain to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeDomain":
        """Create GlobalTimeDomain from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeDomain instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeDomain since parent returns ARObject
        return cast("GlobalTimeDomain", obj)


class GlobalTimeDomainBuilder:
    """Builder for GlobalTimeDomain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeDomain = GlobalTimeDomain()

    def build(self) -> GlobalTimeDomain:
        """Build and return GlobalTimeDomain object.

        Returns:
            GlobalTimeDomain instance
        """
        # TODO: Add validation
        return self._obj
