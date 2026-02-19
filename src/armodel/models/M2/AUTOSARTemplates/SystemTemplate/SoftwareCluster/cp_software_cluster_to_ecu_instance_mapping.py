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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToEcuInstanceMapping":
        """Deserialize XML element to CpSoftwareClusterToEcuInstanceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterToEcuInstanceMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        # Parse machine_id
        child = ARObject._find_child_element(element, "MACHINE-ID")
        if child is not None:
            machine_id_value = child.text
            obj.machine_id = machine_id_value

        # Parse sw_clusters (list)
        obj.sw_clusters = []
        for child in ARObject._find_all_child_elements(element, "SW-CLUSTERS"):
            sw_clusters_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.sw_clusters.append(sw_clusters_value)

        return obj



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
