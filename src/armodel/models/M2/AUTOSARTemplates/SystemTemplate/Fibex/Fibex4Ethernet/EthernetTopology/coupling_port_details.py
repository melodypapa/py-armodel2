"""CouplingPortDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 121)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "coupling_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CouplingPortStructuralElement,
        ),  # couplingPorts
        "ethernet_priority": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=EthernetPriorityRegeneration,
        ),  # ethernetPriority
        "ethernet_traffic": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=CouplingPortTrafficClassAssignment,
        ),  # ethernetTraffic
        "global_time_coupling": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=GlobalTimeCouplingPortProps,
        ),  # globalTimeCoupling
        "last_egress": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CouplingPortScheduler,
        ),  # lastEgress
        "rate_policies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CouplingPortRatePolicy,
        ),  # ratePolicies
    }

    def __init__(self) -> None:
        """Initialize CouplingPortDetails."""
        super().__init__()
        self.coupling_ports: list[CouplingPortStructuralElement] = []
        self.ethernet_priority: EthernetPriorityRegeneration = None
        self.ethernet_traffic: CouplingPortTrafficClassAssignment = None
        self.global_time_coupling: Optional[GlobalTimeCouplingPortProps] = None
        self.last_egress: Optional[CouplingPortScheduler] = None
        self.rate_policies: list[CouplingPortRatePolicy] = []


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
