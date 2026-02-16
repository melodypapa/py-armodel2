"""CouplingPortDetails AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("coupling_ports", None, False, True, CouplingPortStructuralElement),  # couplingPorts
        ("ethernet_priority", None, False, False, EthernetPriorityRegeneration),  # ethernetPriority
        ("ethernet_traffic", None, False, False, CouplingPortTrafficClassAssignment),  # ethernetTraffic
        ("global_time_coupling", None, False, False, GlobalTimeCouplingPortProps),  # globalTimeCoupling
        ("last_egress", None, False, False, CouplingPortScheduler),  # lastEgress
        ("rate_policies", None, False, True, CouplingPortRatePolicy),  # ratePolicies
    ]

    def __init__(self) -> None:
        """Initialize CouplingPortDetails."""
        super().__init__()
        self.coupling_ports: list[CouplingPortStructuralElement] = []
        self.ethernet_priority: EthernetPriorityRegeneration = None
        self.ethernet_traffic: CouplingPortTrafficClassAssignment = None
        self.global_time_coupling: Optional[GlobalTimeCouplingPortProps] = None
        self.last_egress: Optional[CouplingPortScheduler] = None
        self.rate_policies: list[CouplingPortRatePolicy] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPortDetails to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortDetails":
        """Create CouplingPortDetails from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPortDetails instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPortDetails since parent returns ARObject
        return cast("CouplingPortDetails", obj)


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
