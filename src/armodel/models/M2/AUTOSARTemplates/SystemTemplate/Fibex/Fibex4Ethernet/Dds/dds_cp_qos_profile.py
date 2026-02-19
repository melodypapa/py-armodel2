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
    def serialize(self) -> ET.Element:
        """Serialize DdsCpQosProfile to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpQosProfile, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize deadline
        if self.deadline is not None:
            serialized = ARObject._serialize_item(self.deadline, "DdsDeadline")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEADLINE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize destination_order
        if self.destination_order is not None:
            serialized = ARObject._serialize_item(self.destination_order, "DdsDestinationOrder")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize durability
        if self.durability is not None:
            serialized = ARObject._serialize_item(self.durability, "DdsDurabilityService")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DURABILITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize history
        if self.history is not None:
            serialized = ARObject._serialize_item(self.history, "DdsHistory")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HISTORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize latency_budget
        if self.latency_budget is not None:
            serialized = ARObject._serialize_item(self.latency_budget, "DdsLatencyBudget")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LATENCY-BUDGET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lifespan
        if self.lifespan is not None:
            serialized = ARObject._serialize_item(self.lifespan, "DdsLifespan")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIFESPAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize liveliness
        if self.liveliness is not None:
            serialized = ARObject._serialize_item(self.liveliness, "DdsLiveliness")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIVELINESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ownership
        if self.ownership is not None:
            serialized = ARObject._serialize_item(self.ownership, "DdsOwnershipStrength")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OWNERSHIP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reliability
        if self.reliability is not None:
            serialized = ARObject._serialize_item(self.reliability, "DdsReliability")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELIABILITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resource_limits
        if self.resource_limits is not None:
            serialized = ARObject._serialize_item(self.resource_limits, "DdsResourceLimits")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOURCE-LIMITS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize topic_data
        if self.topic_data is not None:
            serialized = ARObject._serialize_item(self.topic_data, "DdsTopicData")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOPIC-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transport_priority
        if self.transport_priority is not None:
            serialized = ARObject._serialize_item(self.transport_priority, "DdsTransportPriority")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSPORT-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpQosProfile":
        """Deserialize XML element to DdsCpQosProfile object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpQosProfile object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpQosProfile, cls).deserialize(element)

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
