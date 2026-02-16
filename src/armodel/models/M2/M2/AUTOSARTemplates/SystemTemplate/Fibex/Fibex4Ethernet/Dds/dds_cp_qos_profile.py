"""DdsCpQosProfile AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "deadline": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsDeadline,
        ),  # deadline
        "destination_order": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsDestinationOrder,
        ),  # destinationOrder
        "durability": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsDurabilityService,
        ),  # durability
        "history": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsHistory,
        ),  # history
        "latency_budget": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsLatencyBudget,
        ),  # latencyBudget
        "lifespan": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsLifespan,
        ),  # lifespan
        "liveliness": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsLiveliness,
        ),  # liveliness
        "ownership": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsOwnershipStrength,
        ),  # ownership
        "reliability": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsReliability,
        ),  # reliability
        "resource_limits": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsResourceLimits,
        ),  # resourceLimits
        "topic_data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsTopicData,
        ),  # topicData
        "transport_priority": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsTransportPriority,
        ),  # transportPriority
    }

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
