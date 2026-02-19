"""SwcServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 224)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 608)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
    ServiceDependency,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_port_assignment import (
    RoleBasedPortAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class SwcServiceDependency(ServiceDependency):
    """AUTOSAR SwcServiceDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_datas: list[Any]
    assigned_ports: list[RoleBasedPortAssignment]
    represented_port_ref: Optional[ARRef]
    service_needs: Optional[ServiceNeeds]
    def __init__(self) -> None:
        """Initialize SwcServiceDependency."""
        super().__init__()
        self.assigned_datas: list[Any] = []
        self.assigned_ports: list[RoleBasedPortAssignment] = []
        self.represented_port_ref: Optional[ARRef] = None
        self.service_needs: Optional[ServiceNeeds] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcServiceDependency":
        """Deserialize XML element to SwcServiceDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcServiceDependency object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse assigned_datas (list)
        obj.assigned_datas = []
        for child in ARObject._find_all_child_elements(element, "ASSIGNED-DATAS"):
            assigned_datas_value = child.text
            obj.assigned_datas.append(assigned_datas_value)

        # Parse assigned_ports (list)
        obj.assigned_ports = []
        for child in ARObject._find_all_child_elements(element, "ASSIGNED-PORTS"):
            assigned_ports_value = ARObject._deserialize_by_tag(child, "RoleBasedPortAssignment")
            obj.assigned_ports.append(assigned_ports_value)

        # Parse represented_port_ref
        child = ARObject._find_child_element(element, "REPRESENTED-PORT")
        if child is not None:
            represented_port_ref_value = ARObject._deserialize_by_tag(child, "PortGroup")
            obj.represented_port_ref = represented_port_ref_value

        # Parse service_needs
        child = ARObject._find_child_element(element, "SERVICE-NEEDS")
        if child is not None:
            service_needs_value = ARObject._deserialize_by_tag(child, "ServiceNeeds")
            obj.service_needs = service_needs_value

        return obj



class SwcServiceDependencyBuilder:
    """Builder for SwcServiceDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcServiceDependency = SwcServiceDependency()

    def build(self) -> SwcServiceDependency:
        """Build and return SwcServiceDependency object.

        Returns:
            SwcServiceDependency instance
        """
        # TODO: Add validation
        return self._obj
