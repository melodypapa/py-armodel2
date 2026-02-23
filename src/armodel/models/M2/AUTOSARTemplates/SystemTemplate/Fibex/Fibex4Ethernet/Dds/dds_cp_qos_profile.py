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
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


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
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpQosProfile, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize deadline
        if self.deadline is not None:
            serialized = SerializationHelper.serialize_item(self.deadline, "DdsDeadline")
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
            serialized = SerializationHelper.serialize_item(self.destination_order, "DdsDestinationOrder")
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
            serialized = SerializationHelper.serialize_item(self.durability, "DdsDurabilityService")
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
            serialized = SerializationHelper.serialize_item(self.history, "DdsHistory")
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
            serialized = SerializationHelper.serialize_item(self.latency_budget, "DdsLatencyBudget")
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
            serialized = SerializationHelper.serialize_item(self.lifespan, "DdsLifespan")
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
            serialized = SerializationHelper.serialize_item(self.liveliness, "DdsLiveliness")
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
            serialized = SerializationHelper.serialize_item(self.ownership, "DdsOwnershipStrength")
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
            serialized = SerializationHelper.serialize_item(self.reliability, "DdsReliability")
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
            serialized = SerializationHelper.serialize_item(self.resource_limits, "DdsResourceLimits")
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
            serialized = SerializationHelper.serialize_item(self.topic_data, "DdsTopicData")
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
            serialized = SerializationHelper.serialize_item(self.transport_priority, "DdsTransportPriority")
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
        child = SerializationHelper.find_child_element(element, "DEADLINE")
        if child is not None:
            deadline_value = SerializationHelper.deserialize_by_tag(child, "DdsDeadline")
            obj.deadline = deadline_value

        # Parse destination_order
        child = SerializationHelper.find_child_element(element, "DESTINATION-ORDER")
        if child is not None:
            destination_order_value = SerializationHelper.deserialize_by_tag(child, "DdsDestinationOrder")
            obj.destination_order = destination_order_value

        # Parse durability
        child = SerializationHelper.find_child_element(element, "DURABILITY")
        if child is not None:
            durability_value = SerializationHelper.deserialize_by_tag(child, "DdsDurabilityService")
            obj.durability = durability_value

        # Parse history
        child = SerializationHelper.find_child_element(element, "HISTORY")
        if child is not None:
            history_value = SerializationHelper.deserialize_by_tag(child, "DdsHistory")
            obj.history = history_value

        # Parse latency_budget
        child = SerializationHelper.find_child_element(element, "LATENCY-BUDGET")
        if child is not None:
            latency_budget_value = SerializationHelper.deserialize_by_tag(child, "DdsLatencyBudget")
            obj.latency_budget = latency_budget_value

        # Parse lifespan
        child = SerializationHelper.find_child_element(element, "LIFESPAN")
        if child is not None:
            lifespan_value = SerializationHelper.deserialize_by_tag(child, "DdsLifespan")
            obj.lifespan = lifespan_value

        # Parse liveliness
        child = SerializationHelper.find_child_element(element, "LIVELINESS")
        if child is not None:
            liveliness_value = SerializationHelper.deserialize_by_tag(child, "DdsLiveliness")
            obj.liveliness = liveliness_value

        # Parse ownership
        child = SerializationHelper.find_child_element(element, "OWNERSHIP")
        if child is not None:
            ownership_value = SerializationHelper.deserialize_by_tag(child, "DdsOwnershipStrength")
            obj.ownership = ownership_value

        # Parse reliability
        child = SerializationHelper.find_child_element(element, "RELIABILITY")
        if child is not None:
            reliability_value = SerializationHelper.deserialize_by_tag(child, "DdsReliability")
            obj.reliability = reliability_value

        # Parse resource_limits
        child = SerializationHelper.find_child_element(element, "RESOURCE-LIMITS")
        if child is not None:
            resource_limits_value = SerializationHelper.deserialize_by_tag(child, "DdsResourceLimits")
            obj.resource_limits = resource_limits_value

        # Parse topic_data
        child = SerializationHelper.find_child_element(element, "TOPIC-DATA")
        if child is not None:
            topic_data_value = SerializationHelper.deserialize_by_tag(child, "DdsTopicData")
            obj.topic_data = topic_data_value

        # Parse transport_priority
        child = SerializationHelper.find_child_element(element, "TRANSPORT-PRIORITY")
        if child is not None:
            transport_priority_value = SerializationHelper.deserialize_by_tag(child, "DdsTransportPriority")
            obj.transport_priority = transport_priority_value

        return obj



class DdsCpQosProfileBuilder(IdentifiableBuilder):
    """Builder for DdsCpQosProfile with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsCpQosProfile = DdsCpQosProfile()


    def with_deadline(self, value: Optional[DdsDeadline]) -> "DdsCpQosProfileBuilder":
        """Set deadline attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.deadline = value
        return self

    def with_destination_order(self, value: Optional[DdsDestinationOrder]) -> "DdsCpQosProfileBuilder":
        """Set destination_order attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.destination_order = value
        return self

    def with_durability(self, value: Optional[DdsDurabilityService]) -> "DdsCpQosProfileBuilder":
        """Set durability attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.durability = value
        return self

    def with_history(self, value: Optional[DdsHistory]) -> "DdsCpQosProfileBuilder":
        """Set history attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.history = value
        return self

    def with_latency_budget(self, value: Optional[DdsLatencyBudget]) -> "DdsCpQosProfileBuilder":
        """Set latency_budget attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.latency_budget = value
        return self

    def with_lifespan(self, value: Optional[DdsLifespan]) -> "DdsCpQosProfileBuilder":
        """Set lifespan attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lifespan = value
        return self

    def with_liveliness(self, value: Optional[DdsLiveliness]) -> "DdsCpQosProfileBuilder":
        """Set liveliness attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.liveliness = value
        return self

    def with_ownership(self, value: Optional[DdsOwnershipStrength]) -> "DdsCpQosProfileBuilder":
        """Set ownership attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ownership = value
        return self

    def with_reliability(self, value: Optional[DdsReliability]) -> "DdsCpQosProfileBuilder":
        """Set reliability attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reliability = value
        return self

    def with_resource_limits(self, value: Optional[DdsResourceLimits]) -> "DdsCpQosProfileBuilder":
        """Set resource_limits attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resource_limits = value
        return self

    def with_topic_data(self, value: Optional[DdsTopicData]) -> "DdsCpQosProfileBuilder":
        """Set topic_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.topic_data = value
        return self

    def with_transport_priority(self, value: Optional[DdsTransportPriority]) -> "DdsCpQosProfileBuilder":
        """Set transport_priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transport_priority = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> DdsCpQosProfile:
        """Build and return the DdsCpQosProfile instance with validation."""
        self._validate_instance()
        pass
        return self._obj