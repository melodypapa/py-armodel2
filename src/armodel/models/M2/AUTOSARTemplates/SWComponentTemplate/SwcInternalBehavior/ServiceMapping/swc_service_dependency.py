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
    represented_port: Optional[PortGroup]
    service_needs: Optional[ServiceNeeds]
    def __init__(self) -> None:
        """Initialize SwcServiceDependency."""
        super().__init__()
        self.assigned_datas: list[Any] = []
        self.assigned_ports: list[RoleBasedPortAssignment] = []
        self.represented_port: Optional[PortGroup] = None
        self.service_needs: Optional[ServiceNeeds] = None


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
