"""DdsCpQosProfile AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 528)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    deadline: Optional[DdsDeadline]
    destination_order: Optional[DdsDestinationOrder]
    durability: Optional[DdsDurabilityService]
    history: Optional[DdsHistory]
    latency_budget: Optional[DdsLatencyBudget]
    lifespan: Optional[DdsLifespan]
    liveliness: Optional[DdsLiveliness]
    ownership: Optional[DdsOwnershipStrength]
    reliability: Optional[DdsReliability]
    resource_limits: Optional[DdsResourceLimits]
    topic_data: Optional[DdsTopicData]
    transport_priority: Optional[DdsTransportPriority]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpQosProfile":
        """Deserialize XML element to DdsCpQosProfile object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpQosProfile object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse deadline
        child = ARObject._find_child_element(element, "DEADLINE")
        if child is not None:
            deadline_value = ARObject._deserialize_by_tag(child, "DdsDeadline")
            obj.deadline = deadline_value

        # Parse destination_order
        child = ARObject._find_child_element(element, "DESTINATION-ORDER")
        if child is not None:
            destination_order_value = ARObject._deserialize_by_tag(child, "DdsDestinationOrder")
            obj.destination_order = destination_order_value

        # Parse durability
        child = ARObject._find_child_element(element, "DURABILITY")
        if child is not None:
            durability_value = ARObject._deserialize_by_tag(child, "DdsDurabilityService")
            obj.durability = durability_value

        # Parse history
        child = ARObject._find_child_element(element, "HISTORY")
        if child is not None:
            history_value = ARObject._deserialize_by_tag(child, "DdsHistory")
            obj.history = history_value

        # Parse latency_budget
        child = ARObject._find_child_element(element, "LATENCY-BUDGET")
        if child is not None:
            latency_budget_value = ARObject._deserialize_by_tag(child, "DdsLatencyBudget")
            obj.latency_budget = latency_budget_value

        # Parse lifespan
        child = ARObject._find_child_element(element, "LIFESPAN")
        if child is not None:
            lifespan_value = ARObject._deserialize_by_tag(child, "DdsLifespan")
            obj.lifespan = lifespan_value

        # Parse liveliness
        child = ARObject._find_child_element(element, "LIVELINESS")
        if child is not None:
            liveliness_value = ARObject._deserialize_by_tag(child, "DdsLiveliness")
            obj.liveliness = liveliness_value

        # Parse ownership
        child = ARObject._find_child_element(element, "OWNERSHIP")
        if child is not None:
            ownership_value = ARObject._deserialize_by_tag(child, "DdsOwnershipStrength")
            obj.ownership = ownership_value

        # Parse reliability
        child = ARObject._find_child_element(element, "RELIABILITY")
        if child is not None:
            reliability_value = ARObject._deserialize_by_tag(child, "DdsReliability")
            obj.reliability = reliability_value

        # Parse resource_limits
        child = ARObject._find_child_element(element, "RESOURCE-LIMITS")
        if child is not None:
            resource_limits_value = ARObject._deserialize_by_tag(child, "DdsResourceLimits")
            obj.resource_limits = resource_limits_value

        # Parse topic_data
        child = ARObject._find_child_element(element, "TOPIC-DATA")
        if child is not None:
            topic_data_value = ARObject._deserialize_by_tag(child, "DdsTopicData")
            obj.topic_data = topic_data_value

        # Parse transport_priority
        child = ARObject._find_child_element(element, "TRANSPORT-PRIORITY")
        if child is not None:
            transport_priority_value = ARObject._deserialize_by_tag(child, "DdsTransportPriority")
            obj.transport_priority = transport_priority_value

        return obj



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
