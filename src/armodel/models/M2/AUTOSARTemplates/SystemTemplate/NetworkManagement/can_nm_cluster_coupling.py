"""CanNmClusterCoupling AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 684)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.can_nm_cluster import (
    CanNmCluster,
)


class CanNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR CanNmClusterCoupling."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    coupled_clusters: list[CanNmCluster]
    nm_busload_reduction: Optional[Any]
    nm_immediate: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CanNmClusterCoupling."""
        super().__init__()
        self.coupled_clusters: list[CanNmCluster] = []
        self.nm_busload_reduction: Optional[Any] = None
        self.nm_immediate: Optional[Boolean] = None


class CanNmClusterCouplingBuilder:
    """Builder for CanNmClusterCoupling."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanNmClusterCoupling = CanNmClusterCoupling()

    def build(self) -> CanNmClusterCoupling:
        """Build and return CanNmClusterCoupling object.

        Returns:
            CanNmClusterCoupling instance
        """
        # TODO: Add validation
        return self._obj
