"""CouplingElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element import (
    CouplingElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_cluster import (
    EthernetCluster,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.state_dependent_firewall import (
    StateDependentFirewall,
)


class CouplingElement(FibexElement):
    """AUTOSAR CouplingElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication", None, False, False, EthernetCluster),  # communication
        ("coupling", None, False, False, CouplingElement),  # coupling
        ("coupling_ports", None, False, True, CouplingPort),  # couplingPorts
        ("coupling_type", None, False, False, CouplingElementEnum),  # couplingType
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
        ("firewall_rules", None, False, True, StateDependentFirewall),  # firewallRules
    ]

    def __init__(self) -> None:
        """Initialize CouplingElement."""
        super().__init__()
        self.communication: Optional[EthernetCluster] = None
        self.coupling: Optional[CouplingElement] = None
        self.coupling_ports: list[CouplingPort] = []
        self.coupling_type: Optional[CouplingElementEnum] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.firewall_rules: list[StateDependentFirewall] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingElement":
        """Create CouplingElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingElement since parent returns ARObject
        return cast("CouplingElement", obj)


class CouplingElementBuilder:
    """Builder for CouplingElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingElement = CouplingElement()

    def build(self) -> CouplingElement:
        """Build and return CouplingElement object.

        Returns:
            CouplingElement instance
        """
        # TODO: Add validation
        return self._obj
