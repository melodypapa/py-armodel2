"""CpSoftwareClusterResourceToApplicationPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 284)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterResourceToApplicationPartitionMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterResourceToApplicationPartitionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application: Optional[ApplicationPartition]
    resource: Optional[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResourceToApplicationPartitionMapping."""
        super().__init__()
        self.application: Optional[ApplicationPartition] = None
        self.resource: Optional[CpSoftwareCluster] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterResourceToApplicationPartitionMapping":
        """Deserialize XML element to CpSoftwareClusterResourceToApplicationPartitionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterResourceToApplicationPartitionMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterResourceToApplicationPartitionMapping, cls).deserialize(element)

        # Parse application
        child = ARObject._find_child_element(element, "APPLICATION")
        if child is not None:
            application_value = ARObject._deserialize_by_tag(child, "ApplicationPartition")
            obj.application = application_value

        # Parse resource
        child = ARObject._find_child_element(element, "RESOURCE")
        if child is not None:
            resource_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.resource = resource_value

        return obj



class CpSoftwareClusterResourceToApplicationPartitionMappingBuilder:
    """Builder for CpSoftwareClusterResourceToApplicationPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterResourceToApplicationPartitionMapping = CpSoftwareClusterResourceToApplicationPartitionMapping()

    def build(self) -> CpSoftwareClusterResourceToApplicationPartitionMapping:
        """Build and return CpSoftwareClusterResourceToApplicationPartitionMapping object.

        Returns:
            CpSoftwareClusterResourceToApplicationPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj
