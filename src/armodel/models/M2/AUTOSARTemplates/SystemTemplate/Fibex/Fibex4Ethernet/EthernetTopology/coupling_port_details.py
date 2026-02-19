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

        # Parse coupling_ports (list)
        obj.coupling_ports = []
        for child in ARObject._find_all_child_elements(element, "COUPLING-PORTS"):
            coupling_ports_value = ARObject._deserialize_by_tag(child, "CouplingPortStructuralElement")
            obj.coupling_ports.append(coupling_ports_value)

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

        # Parse rate_policies (list)
        obj.rate_policies = []
        for child in ARObject._find_all_child_elements(element, "RATE-POLICIES"):
            rate_policies_value = ARObject._deserialize_by_tag(child, "CouplingPortRatePolicy")
            obj.rate_policies.append(rate_policies_value)

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
