"""CpSoftwareClusterMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 285)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "port_element_tos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PortElementToCommunicationResourceMapping,
        ),  # portElementTos
        "resource_tos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CpSoftwareCluster,
        ),  # resourceTos
        "software_clusters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (CpSoftwareClusterTo),
        ),  # softwareClusters
        "swc_tos": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwcToApplicationPartitionMapping,
        ),  # swcTos
    }

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterMappingSet."""
        super().__init__()
        self.port_element_tos: list[PortElementToCommunicationResourceMapping] = []
        self.resource_tos: list[CpSoftwareCluster] = []
        self.software_clusters: list[Any] = []
        self.swc_tos: list[SwcToApplicationPartitionMapping] = []


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
