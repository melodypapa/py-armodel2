"""CouplingPortDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 121)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_rate_policy import (
    CouplingPortRatePolicy,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_scheduler import (
    CouplingPortScheduler,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_traffic_class_assignment import (
    CouplingPortTrafficClassAssignment,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_priority_regeneration import (
    EthernetPriorityRegeneration,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.global_time_coupling_port_props import (
    GlobalTimeCouplingPortProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class CouplingPortDetails(ARObject):
    """AUTOSAR CouplingPortDetails."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    coupling_ports: list[CouplingPortStructuralElement]
    ethernet_priority: EthernetPriorityRegeneration
    ethernet_traffic: CouplingPortTrafficClassAssignment
    global_time_coupling: Optional[GlobalTimeCouplingPortProps]
    last_egress_ref: Optional[ARRef]
    _rate_policies: list[CouplingPortRatePolicy]
    def __init__(self) -> None:
        """Initialize CouplingPortDetails."""
        super().__init__()
        self.coupling_ports: list[CouplingPortStructuralElement] = []
        self.ethernet_priority: EthernetPriorityRegeneration = None
        self.ethernet_traffic: CouplingPortTrafficClassAssignment = None
        self.global_time_coupling: Optional[GlobalTimeCouplingPortProps] = None
        self.last_egress_ref: Optional[ARRef] = None
        self._rate_policies: list[CouplingPortRatePolicy] = []
    @property
    @xml_element_name("RATE-POLICYS")
    def rate_policies(self) -> list[CouplingPortRatePolicy]:
        """Get rate_policies with custom XML element name."""
        return self._rate_policies

    @rate_policies.setter
    def rate_policies(self, value: list[CouplingPortRatePolicy]) -> None:
        """Set rate_policies with custom XML element name."""
        self._rate_policies = value


    def serialize(self) -> ET.Element:
        """Serialize CouplingPortDetails to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortDetails, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize coupling_ports (list to container "COUPLING-PORTS")
        if self.coupling_ports:
            wrapper = ET.Element("COUPLING-PORTS")
            for item in self.coupling_ports:
                serialized = SerializationHelper.serialize_item(item, "CouplingPortStructuralElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ethernet_priority
        if self.ethernet_priority is not None:
            serialized = SerializationHelper.serialize_item(self.ethernet_priority, "EthernetPriorityRegeneration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ETHERNET-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ethernet_traffic
        if self.ethernet_traffic is not None:
            serialized = SerializationHelper.serialize_item(self.ethernet_traffic, "CouplingPortTrafficClassAssignment")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ETHERNET-TRAFFIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_time_coupling
        if self.global_time_coupling is not None:
            serialized = SerializationHelper.serialize_item(self.global_time_coupling, "GlobalTimeCouplingPortProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GLOBAL-TIME-COUPLING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize last_egress_ref
        if self.last_egress_ref is not None:
            serialized = SerializationHelper.serialize_item(self.last_egress_ref, "CouplingPortScheduler")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LAST-EGRESS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_policies (list to container "RATE-POLICYS")
        if self.rate_policies:
            wrapper = ET.Element("RATE-POLICYS")
            for item in self.rate_policies:
                serialized = SerializationHelper.serialize_item(item, "CouplingPortRatePolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortDetails":
        """Deserialize XML element to CouplingPortDetails object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortDetails object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortDetails, cls).deserialize(element)

        # Parse coupling_ports (list from container "COUPLING-PORTS")
        obj.coupling_ports = []
        container = SerializationHelper.find_child_element(element, "COUPLING-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.coupling_ports.append(child_value)

        # Parse ethernet_priority
        child = SerializationHelper.find_child_element(element, "ETHERNET-PRIORITY")
        if child is not None:
            ethernet_priority_value = SerializationHelper.deserialize_by_tag(child, "EthernetPriorityRegeneration")
            obj.ethernet_priority = ethernet_priority_value

        # Parse ethernet_traffic
        child = SerializationHelper.find_child_element(element, "ETHERNET-TRAFFIC")
        if child is not None:
            ethernet_traffic_value = SerializationHelper.deserialize_by_tag(child, "CouplingPortTrafficClassAssignment")
            obj.ethernet_traffic = ethernet_traffic_value

        # Parse global_time_coupling
        child = SerializationHelper.find_child_element(element, "GLOBAL-TIME-COUPLING")
        if child is not None:
            global_time_coupling_value = SerializationHelper.deserialize_by_tag(child, "GlobalTimeCouplingPortProps")
            obj.global_time_coupling = global_time_coupling_value

        # Parse last_egress_ref
        child = SerializationHelper.find_child_element(element, "LAST-EGRESS-REF")
        if child is not None:
            last_egress_ref_value = ARRef.deserialize(child)
            obj.last_egress_ref = last_egress_ref_value

        # Parse rate_policies (list from container "RATE-POLICYS")
        obj.rate_policies = []
        container = SerializationHelper.find_child_element(element, "RATE-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rate_policies.append(child_value)

        return obj



class CouplingPortDetailsBuilder(BuilderBase):
    """Builder for CouplingPortDetails with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CouplingPortDetails = CouplingPortDetails()


    def with_coupling_ports(self, items: list[CouplingPortStructuralElement]) -> "CouplingPortDetailsBuilder":
        """Set coupling_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.coupling_ports = list(items) if items else []
        return self

    def with_ethernet_priority(self, value: EthernetPriorityRegeneration) -> "CouplingPortDetailsBuilder":
        """Set ethernet_priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ethernet_priority = value
        return self

    def with_ethernet_traffic(self, value: CouplingPortTrafficClassAssignment) -> "CouplingPortDetailsBuilder":
        """Set ethernet_traffic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ethernet_traffic = value
        return self

    def with_global_time_coupling(self, value: Optional[GlobalTimeCouplingPortProps]) -> "CouplingPortDetailsBuilder":
        """Set global_time_coupling attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.global_time_coupling = value
        return self

    def with_last_egress(self, value: Optional[CouplingPortScheduler]) -> "CouplingPortDetailsBuilder":
        """Set last_egress attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.last_egress = value
        return self

    def with_rate_policies(self, items: list[CouplingPortRatePolicy]) -> "CouplingPortDetailsBuilder":
        """Set rate_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rate_policies = list(items) if items else []
        return self


    def add_coupling_port(self, item: CouplingPortStructuralElement) -> "CouplingPortDetailsBuilder":
        """Add a single item to coupling_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.coupling_ports.append(item)
        return self

    def clear_coupling_ports(self) -> "CouplingPortDetailsBuilder":
        """Clear all items from coupling_ports list.

        Returns:
            self for method chaining
        """
        self._obj.coupling_ports = []
        return self

    def add_rate_policie(self, item: CouplingPortRatePolicy) -> "CouplingPortDetailsBuilder":
        """Add a single item to rate_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rate_policies.append(item)
        return self

    def clear_rate_policies(self) -> "CouplingPortDetailsBuilder":
        """Clear all items from rate_policies list.

        Returns:
            self for method chaining
        """
        self._obj.rate_policies = []
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


    def build(self) -> CouplingPortDetails:
        """Build and return the CouplingPortDetails instance with validation."""
        self._validate_instance()
        pass
        return self._obj