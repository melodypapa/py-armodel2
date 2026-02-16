"""FlexrayNmClusterCoupling AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.flexray_nm_cluster import (
    FlexrayNmCluster,
)


class FlexrayNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR FlexrayNmClusterCoupling."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "coupled_clusters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FlexrayNmCluster,
        ),  # coupledClusters
        "nm_schedule": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FlexrayNmScheduleVariant,
        ),  # nmSchedule
    }

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
