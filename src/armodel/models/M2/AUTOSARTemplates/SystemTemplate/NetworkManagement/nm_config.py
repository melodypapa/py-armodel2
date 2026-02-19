"""NmConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 672)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_ecu import (
    NmEcu,
)


class NmConfig(FibexElement):
    """AUTOSAR NmConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_clusters: list[NmCluster]
    nm_cluster_couplings: list[NmClusterCoupling]
    nm_if_ecus: list[NmEcu]
    def __init__(self) -> None:
        """Initialize NmConfig."""
        super().__init__()
        self.nm_clusters: list[NmCluster] = []
        self.nm_cluster_couplings: list[NmClusterCoupling] = []
        self.nm_if_ecus: list[NmEcu] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmConfig":
        """Deserialize XML element to NmConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmConfig, cls).deserialize(element)

        # Parse nm_clusters (list from container "NM-CLUSTERS")
        obj.nm_clusters = []
        container = ARObject._find_child_element(element, "NM-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nm_clusters.append(child_value)

        # Parse nm_cluster_couplings (list from container "NM-CLUSTER-COUPLINGS")
        obj.nm_cluster_couplings = []
        container = ARObject._find_child_element(element, "NM-CLUSTER-COUPLINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nm_cluster_couplings.append(child_value)

        # Parse nm_if_ecus (list from container "NM-IF-ECUS")
        obj.nm_if_ecus = []
        container = ARObject._find_child_element(element, "NM-IF-ECUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nm_if_ecus.append(child_value)

        return obj



class NmConfigBuilder:
    """Builder for NmConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmConfig = NmConfig()

    def build(self) -> NmConfig:
        """Build and return NmConfig object.

        Returns:
            NmConfig instance
        """
        # TODO: Add validation
        return self._obj
