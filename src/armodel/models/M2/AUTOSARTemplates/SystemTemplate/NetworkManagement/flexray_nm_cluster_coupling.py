"""FlexrayNmClusterCoupling AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 679)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    FlexrayNmScheduleVariant,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.flexray_nm_cluster import (
    FlexrayNmCluster,
)


class FlexrayNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR FlexrayNmClusterCoupling."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    coupled_clusters: list[FlexrayNmCluster]
    nm_schedule: Optional[FlexrayNmScheduleVariant]
    def __init__(self) -> None:
        """Initialize FlexrayNmClusterCoupling."""
        super().__init__()
        self.coupled_clusters: list[FlexrayNmCluster] = []
        self.nm_schedule: Optional[FlexrayNmScheduleVariant] = None


class FlexrayNmClusterCouplingBuilder:
    """Builder for FlexrayNmClusterCoupling."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmClusterCoupling = FlexrayNmClusterCoupling()

    def build(self) -> FlexrayNmClusterCoupling:
        """Build and return FlexrayNmClusterCoupling object.

        Returns:
            FlexrayNmClusterCoupling instance
        """
        # TODO: Add validation
        return self._obj
