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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcServiceDependency, cls).deserialize(element)

        # Parse assigned_datas (list from container "ASSIGNED-DATAS")
        obj.assigned_datas = []
        container = ARObject._find_child_element(element, "ASSIGNED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_datas.append(child_value)

        # Parse assigned_ports (list from container "ASSIGNED-PORTS")
        obj.assigned_ports = []
        container = ARObject._find_child_element(element, "ASSIGNED-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_ports.append(child_value)

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
