"""ServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 609)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceDiagnosticRelevanceEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_data_type_assignment import (
    RoleBasedDataTypeAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.symbolic_name_props import (
    SymbolicNameProps,
)


class ServiceDependency(ARObject):
    """AUTOSAR ServiceDependency."""
    """Abstract base class - do not instantiate directly."""

    assigned_data: Optional[RoleBasedDataTypeAssignment]
    diagnostic: Optional[ServiceDiagnosticRelevanceEnum]
    symbolic_name_props: Optional[SymbolicNameProps]
    def __init__(self) -> None:
        """Initialize ServiceDependency."""
        super().__init__()
        self.assigned_data: Optional[RoleBasedDataTypeAssignment] = None
        self.diagnostic: Optional[ServiceDiagnosticRelevanceEnum] = None
        self.symbolic_name_props: Optional[SymbolicNameProps] = None


class ServiceDependencyBuilder:
    """Builder for ServiceDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceDependency = ServiceDependency()

    def build(self) -> ServiceDependency:
        """Build and return ServiceDependency object.

        Returns:
            ServiceDependency instance
        """
        # TODO: Add validation
        return self._obj
