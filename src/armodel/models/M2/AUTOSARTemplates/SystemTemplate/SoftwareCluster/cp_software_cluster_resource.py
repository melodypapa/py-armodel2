"""CpSoftwareClusterResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 271)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 901)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.role_based_resource_dependency import (
    RoleBasedResourceDependency,
)


class CpSoftwareClusterResource(Identifiable):
    """AUTOSAR CpSoftwareClusterResource."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResource."""
        super().__init__()
        self.dependents: list[RoleBasedResourceDependency] = []
        self.global_resource: Optional[PositiveInteger] = None
        self.is_mandatory: Optional[Boolean] = None


class CpSoftwareClusterResourceBuilder:
    """Builder for CpSoftwareClusterResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterResource = CpSoftwareClusterResource()

    def build(self) -> CpSoftwareClusterResource:
        """Build and return CpSoftwareClusterResource object.

        Returns:
            CpSoftwareClusterResource instance
        """
        # TODO: Add validation
        return self._obj
