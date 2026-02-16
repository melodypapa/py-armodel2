"""DdsCpQosProfile AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_deadline import (
    DdsDeadline,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_destination_order import (
    DdsDestinationOrder,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_durability_service import (
    DdsDurabilityService,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_history import (
    DdsHistory,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_latency_budget import (
    DdsLatencyBudget,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_lifespan import (
    DdsLifespan,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_liveliness import (
    DdsLiveliness,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_ownership_strength import (
    DdsOwnershipStrength,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_reliability import (
    DdsReliability,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_resource_limits import (
    DdsResourceLimits,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_topic_data import (
    DdsTopicData,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_transport_priority import (
    DdsTransportPriority,
)


class DdsCpQosProfile(Identifiable):
    """AUTOSAR DdsCpQosProfile."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("deadline", None, False, False, DdsDeadline),  # deadline
        ("destination_order", None, False, False, DdsDestinationOrder),  # destinationOrder
        ("durability", None, False, False, DdsDurabilityService),  # durability
        ("history", None, False, False, DdsHistory),  # history
        ("latency_budget", None, False, False, DdsLatencyBudget),  # latencyBudget
        ("lifespan", None, False, False, DdsLifespan),  # lifespan
        ("liveliness", None, False, False, DdsLiveliness),  # liveliness
        ("ownership", None, False, False, DdsOwnershipStrength),  # ownership
        ("reliability", None, False, False, DdsReliability),  # reliability
        ("resource_limits", None, False, False, DdsResourceLimits),  # resourceLimits
        ("topic_data", None, False, False, DdsTopicData),  # topicData
        ("transport_priority", None, False, False, DdsTransportPriority),  # transportPriority
    ]

    def __init__(self) -> None:
        """Initialize DdsCpQosProfile."""
        super().__init__()
        self.deadline: Optional[DdsDeadline] = None
        self.destination_order: Optional[DdsDestinationOrder] = None
        self.durability: Optional[DdsDurabilityService] = None
        self.history: Optional[DdsHistory] = None
        self.latency_budget: Optional[DdsLatencyBudget] = None
        self.lifespan: Optional[DdsLifespan] = None
        self.liveliness: Optional[DdsLiveliness] = None
        self.ownership: Optional[DdsOwnershipStrength] = None
        self.reliability: Optional[DdsReliability] = None
        self.resource_limits: Optional[DdsResourceLimits] = None
        self.topic_data: Optional[DdsTopicData] = None
        self.transport_priority: Optional[DdsTransportPriority] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpQosProfile to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpQosProfile":
        """Create DdsCpQosProfile from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpQosProfile instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpQosProfile since parent returns ARObject
        return cast("DdsCpQosProfile", obj)


class DdsCpQosProfileBuilder:
    """Builder for DdsCpQosProfile."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpQosProfile = DdsCpQosProfile()

    def build(self) -> DdsCpQosProfile:
        """Build and return DdsCpQosProfile object.

        Returns:
            DdsCpQosProfile instance
        """
        # TODO: Add validation
        return self._obj
