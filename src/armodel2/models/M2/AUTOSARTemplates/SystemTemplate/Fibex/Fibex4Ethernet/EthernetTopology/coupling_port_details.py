"""CouplingPortDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 121)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_rate_policy import (
    CouplingPortRatePolicy,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_scheduler import (
    CouplingPortScheduler,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_traffic_class_assignment import (
    CouplingPortTrafficClassAssignment,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_priority_regeneration import (
    EthernetPriorityRegeneration,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.global_time_coupling_port_props import (
    GlobalTimeCouplingPortProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CouplingPortDetails(ARObject):
    """AUTOSAR CouplingPortDetails."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "COUPLING-PORT-DETAILS"


    coupling_ports: list[CouplingPortStructuralElement]
    ethernet_priority: EthernetPriorityRegeneration
    ethernet_traffic: CouplingPortTrafficClassAssignment
    global_time_coupling: Optional[GlobalTimeCouplingPortProps]
    last_egress_ref: Optional[ARRef]
    rate_policies: list[CouplingPortRatePolicy]
    _DESERIALIZE_DISPATCH = {
        "COUPLING-PORTS": ("_POLYMORPHIC_LIST", "coupling_ports", ["CouplingPortFifo", "CouplingPortScheduler", "CouplingPortShaper"]),
        "ETHERNET-PRIORITY": lambda obj, elem: setattr(obj, "ethernet_priority", SerializationHelper.deserialize_by_tag(elem, "EthernetPriorityRegeneration")),
        "ETHERNET-TRAFFIC": lambda obj, elem: setattr(obj, "ethernet_traffic", SerializationHelper.deserialize_by_tag(elem, "CouplingPortTrafficClassAssignment")),
        "GLOBAL-TIME-COUPLING": lambda obj, elem: setattr(obj, "global_time_coupling", SerializationHelper.deserialize_by_tag(elem, "GlobalTimeCouplingPortProps")),
        "LAST-EGRESS-REF": lambda obj, elem: setattr(obj, "last_egress_ref", ARRef.deserialize(elem)),
        "RATE-POLICYS": lambda obj, elem: obj.rate_policies.append(SerializationHelper.deserialize_by_tag(elem, "CouplingPortRatePolicy")),
    }


    def __init__(self) -> None:
        """Initialize CouplingPortDetails."""
        super().__init__()
        self.coupling_ports: list[CouplingPortStructuralElement] = []
        self.ethernet_priority: EthernetPriorityRegeneration = None
        self.ethernet_traffic: CouplingPortTrafficClassAssignment = None
        self.global_time_coupling: Optional[GlobalTimeCouplingPortProps] = None
        self.last_egress_ref: Optional[ARRef] = None
        self.rate_policies: list[CouplingPortRatePolicy] = []

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortDetails to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COUPLING-PORTS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "COUPLING-PORT-FIFO":
                        obj.coupling_ports.append(SerializationHelper.deserialize_by_tag(item_elem, "CouplingPortFifo"))
                    elif concrete_tag == "COUPLING-PORT-SCHEDULER":
                        obj.coupling_ports.append(SerializationHelper.deserialize_by_tag(item_elem, "CouplingPortScheduler"))
                    elif concrete_tag == "COUPLING-PORT-SHAPER":
                        obj.coupling_ports.append(SerializationHelper.deserialize_by_tag(item_elem, "CouplingPortShaper"))
            elif tag == "ETHERNET-PRIORITY":
                setattr(obj, "ethernet_priority", SerializationHelper.deserialize_by_tag(child, "EthernetPriorityRegeneration"))
            elif tag == "ETHERNET-TRAFFIC":
                setattr(obj, "ethernet_traffic", SerializationHelper.deserialize_by_tag(child, "CouplingPortTrafficClassAssignment"))
            elif tag == "GLOBAL-TIME-COUPLING":
                setattr(obj, "global_time_coupling", SerializationHelper.deserialize_by_tag(child, "GlobalTimeCouplingPortProps"))
            elif tag == "LAST-EGRESS-REF":
                setattr(obj, "last_egress_ref", ARRef.deserialize(child))
            elif tag == "RATE-POLICYS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.rate_policies.append(SerializationHelper.deserialize_by_tag(item_elem, "CouplingPortRatePolicy"))

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
            raise ValueError("Attribute 'ethernet_priority' is required and cannot be None")
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
            raise ValueError("Attribute 'ethernet_traffic' is required and cannot be None")
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
            raise ValueError("Attribute 'global_time_coupling' is required and cannot be None")
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
            raise ValueError("Attribute 'last_egress' is required and cannot be None")
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

    def add_rate_policy(self, item: CouplingPortRatePolicy) -> "CouplingPortDetailsBuilder":
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


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "ethernetPriority",
        "ethernetTraffic",
    }
    _OPTIONAL_ATTRIBUTES = {
        "couplingPort",
        "globalTimeCoupling",
        "lastEgress",
        "ratePolicy",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "ethernetPriority", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'ethernetPriority' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'ethernetPriority' is None", UserWarning)
        if getattr(self._obj, "ethernetTraffic", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'ethernetTraffic' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'ethernetTraffic' is None", UserWarning)


    def build(self) -> CouplingPortDetails:
        """Build and return the CouplingPortDetails instance with validation."""
        self._validate_instance()
        return self._obj