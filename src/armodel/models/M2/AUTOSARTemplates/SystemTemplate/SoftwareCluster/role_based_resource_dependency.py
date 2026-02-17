"""RoleBasedResourceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 272)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 902)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class RoleBasedResourceDependency(ARObject):
    """AUTOSAR RoleBasedResourceDependency."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "resource": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CpSoftwareCluster,
        ),  # resource
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
    }

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
