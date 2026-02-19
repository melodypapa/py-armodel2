"""CouplingElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 107)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElementEnum,
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication: Optional[EthernetCluster]
    coupling: Optional[CouplingElement]
    coupling_ports: list[CouplingPort]
    coupling_type: Optional[CouplingElementEnum]
    ecu_instance: Optional[EcuInstance]
    firewall_rules: list[StateDependentFirewall]
    def __init__(self) -> None:
        """Initialize CouplingElement."""
        super().__init__()
        self.communication: Optional[EthernetCluster] = None
        self.coupling: Optional[CouplingElement] = None
        self.coupling_ports: list[CouplingPort] = []
        self.coupling_type: Optional[CouplingElementEnum] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.firewall_rules: list[StateDependentFirewall] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingElement":
        """Deserialize XML element to CouplingElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse communication
        child = ARObject._find_child_element(element, "COMMUNICATION")
        if child is not None:
            communication_value = ARObject._deserialize_by_tag(child, "EthernetCluster")
            obj.communication = communication_value

        # Parse coupling
        child = ARObject._find_child_element(element, "COUPLING")
        if child is not None:
            coupling_value = ARObject._deserialize_by_tag(child, "CouplingElement")
            obj.coupling = coupling_value

        # Parse coupling_ports (list)
        obj.coupling_ports = []
        for child in ARObject._find_all_child_elements(element, "COUPLING-PORTS"):
            coupling_ports_value = ARObject._deserialize_by_tag(child, "CouplingPort")
            obj.coupling_ports.append(coupling_ports_value)

        # Parse coupling_type
        child = ARObject._find_child_element(element, "COUPLING-TYPE")
        if child is not None:
            coupling_type_value = child.text
            obj.coupling_type = coupling_type_value

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        # Parse firewall_rules (list)
        obj.firewall_rules = []
        for child in ARObject._find_all_child_elements(element, "FIREWALL-RULES"):
            firewall_rules_value = ARObject._deserialize_by_tag(child, "StateDependentFirewall")
            obj.firewall_rules.append(firewall_rules_value)

        return obj



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
