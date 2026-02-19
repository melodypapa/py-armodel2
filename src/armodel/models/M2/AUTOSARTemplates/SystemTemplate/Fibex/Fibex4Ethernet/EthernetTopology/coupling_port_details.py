"""CouplingPortDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 121)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    last_egress: Optional[CouplingPortScheduler]
    rate_policies: list[CouplingPortRatePolicy]
    def __init__(self) -> None:
        """Initialize CouplingPortDetails."""
        super().__init__()
        self.coupling_ports: list[CouplingPortStructuralElement] = []
        self.ethernet_priority: EthernetPriorityRegeneration = None
        self.ethernet_traffic: CouplingPortTrafficClassAssignment = None
        self.global_time_coupling: Optional[GlobalTimeCouplingPortProps] = None
        self.last_egress: Optional[CouplingPortScheduler] = None
        self.rate_policies: list[CouplingPortRatePolicy] = []
    def serialize(self) -> ET.Element:
        """Serialize CouplingPortDetails to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize coupling_ports (list to container "COUPLING-PORTS")
        if self.coupling_ports:
            wrapper = ET.Element("COUPLING-PORTS")
            for item in self.coupling_ports:
                serialized = ARObject._serialize_item(item, "CouplingPortStructuralElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ethernet_priority
        if self.ethernet_priority is not None:
            serialized = ARObject._serialize_item(self.ethernet_priority, "EthernetPriorityRegeneration")
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
            serialized = ARObject._serialize_item(self.ethernet_traffic, "CouplingPortTrafficClassAssignment")
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
            serialized = ARObject._serialize_item(self.global_time_coupling, "GlobalTimeCouplingPortProps")
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

        # Serialize last_egress
        if self.last_egress is not None:
            serialized = ARObject._serialize_item(self.last_egress, "CouplingPortScheduler")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LAST-EGRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_policies (list to container "RATE-POLICIES")
        if self.rate_policies:
            wrapper = ET.Element("RATE-POLICIES")
            for item in self.rate_policies:
                serialized = ARObject._serialize_item(item, "CouplingPortRatePolicy")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse coupling_ports (list from container "COUPLING-PORTS")
        obj.coupling_ports = []
        container = ARObject._find_child_element(element, "COUPLING-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.coupling_ports.append(child_value)

        # Parse ethernet_priority
        child = ARObject._find_child_element(element, "ETHERNET-PRIORITY")
        if child is not None:
            ethernet_priority_value = ARObject._deserialize_by_tag(child, "EthernetPriorityRegeneration")
            obj.ethernet_priority = ethernet_priority_value

        # Parse ethernet_traffic
        child = ARObject._find_child_element(element, "ETHERNET-TRAFFIC")
        if child is not None:
            ethernet_traffic_value = ARObject._deserialize_by_tag(child, "CouplingPortTrafficClassAssignment")
            obj.ethernet_traffic = ethernet_traffic_value

        # Parse global_time_coupling
        child = ARObject._find_child_element(element, "GLOBAL-TIME-COUPLING")
        if child is not None:
            global_time_coupling_value = ARObject._deserialize_by_tag(child, "GlobalTimeCouplingPortProps")
            obj.global_time_coupling = global_time_coupling_value

        # Parse last_egress
        child = ARObject._find_child_element(element, "LAST-EGRESS")
        if child is not None:
            last_egress_value = ARObject._deserialize_by_tag(child, "CouplingPortScheduler")
            obj.last_egress = last_egress_value

        # Parse rate_policies (list from container "RATE-POLICIES")
        obj.rate_policies = []
        container = ARObject._find_child_element(element, "RATE-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rate_policies.append(child_value)

        return obj



class CouplingPortDetailsBuilder:
    """Builder for CouplingPortDetails."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortDetails = CouplingPortDetails()

    def build(self) -> CouplingPortDetails:
        """Build and return CouplingPortDetails object.

        Returns:
            CouplingPortDetails instance
        """
        # TODO: Add validation
        return self._obj
