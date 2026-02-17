"""RoleBasedResourceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 272)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 902)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class RoleBasedResourceDependency(ARObject):
    """AUTOSAR RoleBasedResourceDependency."""

    resource: Optional[CpSoftwareCluster]
    role: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize RoleBasedResourceDependency."""
        super().__init__()
        self.resource: Optional[CpSoftwareCluster] = None
        self.role: Optional[Identifier] = None


class RoleBasedResourceDependencyBuilder:
    """Builder for RoleBasedResourceDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedResourceDependency = RoleBasedResourceDependency()

    def build(self) -> RoleBasedResourceDependency:
        """Build and return RoleBasedResourceDependency object.

        Returns:
            RoleBasedResourceDependency instance
        """
        # TODO: Add validation
        return self._obj
