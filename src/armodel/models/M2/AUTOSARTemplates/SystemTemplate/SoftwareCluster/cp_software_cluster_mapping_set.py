"""CpSoftwareClusterMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 285)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.port_element_to_communication_resource_mapping import (
    PortElementToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_application_partition_mapping import (
    SwcToApplicationPartitionMapping,
)


class CpSoftwareClusterMappingSet(ARElement):
    """AUTOSAR CpSoftwareClusterMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    port_element_tos: list[PortElementToCommunicationResourceMapping]
    resource_tos: list[CpSoftwareCluster]
    software_clusters: list[Any]
    swc_tos: list[SwcToApplicationPartitionMapping]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterMappingSet."""
        super().__init__()
        self.port_element_tos: list[PortElementToCommunicationResourceMapping] = []
        self.resource_tos: list[CpSoftwareCluster] = []
        self.software_clusters: list[Any] = []
        self.swc_tos: list[SwcToApplicationPartitionMapping] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterMappingSet":
        """Deserialize XML element to CpSoftwareClusterMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterMappingSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse port_element_tos (list)
        obj.port_element_tos = []
        for child in ARObject._find_all_child_elements(element, "PORT-ELEMENT-TOS"):
            port_element_tos_value = ARObject._deserialize_by_tag(child, "PortElementToCommunicationResourceMapping")
            obj.port_element_tos.append(port_element_tos_value)

        # Parse resource_tos (list)
        obj.resource_tos = []
        for child in ARObject._find_all_child_elements(element, "RESOURCE-TOS"):
            resource_tos_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.resource_tos.append(resource_tos_value)

        # Parse software_clusters (list)
        obj.software_clusters = []
        for child in ARObject._find_all_child_elements(element, "SOFTWARE-CLUSTERS"):
            software_clusters_value = child.text
            obj.software_clusters.append(software_clusters_value)

        # Parse swc_tos (list)
        obj.swc_tos = []
        for child in ARObject._find_all_child_elements(element, "SWC-TOS"):
            swc_tos_value = ARObject._deserialize_by_tag(child, "SwcToApplicationPartitionMapping")
            obj.swc_tos.append(swc_tos_value)

        return obj



class CpSoftwareClusterMappingSetBuilder:
    """Builder for CpSoftwareClusterMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterMappingSet = CpSoftwareClusterMappingSet()

    def build(self) -> CpSoftwareClusterMappingSet:
        """Build and return CpSoftwareClusterMappingSet object.

        Returns:
            CpSoftwareClusterMappingSet instance
        """
        # TODO: Add validation
        return self._obj
