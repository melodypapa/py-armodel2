"""CpSoftwareClusterToEcuInstanceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 283)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class CpSoftwareClusterToEcuInstanceMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToEcuInstanceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu_instance: Optional[EcuInstance]
    machine_id: Optional[PositiveInteger]
    sw_clusters: list[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToEcuInstanceMapping."""
        super().__init__()
        self.ecu_instance: Optional[EcuInstance] = None
        self.machine_id: Optional[PositiveInteger] = None
        self.sw_clusters: list[CpSoftwareCluster] = []


class CpSoftwareClusterToEcuInstanceMappingBuilder:
    """Builder for CpSoftwareClusterToEcuInstanceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterToEcuInstanceMapping = CpSoftwareClusterToEcuInstanceMapping()

    def build(self) -> CpSoftwareClusterToEcuInstanceMapping:
        """Build and return CpSoftwareClusterToEcuInstanceMapping object.

        Returns:
            CpSoftwareClusterToEcuInstanceMapping instance
        """
        # TODO: Add validation
        return self._obj
