"""UdpNmClusterCoupling AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.udp_nm_cluster import (
    UdpNmCluster,
)


class UdpNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR UdpNmClusterCoupling."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "coupled_clusters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=UdpNmCluster,
        ),  # coupledClusters
        "nm_immediate": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmImmediate
    }

    def __init__(self) -> None:
        """Initialize UdpNmClusterCoupling."""
        super().__init__()
        self.coupled_clusters: list[UdpNmCluster] = []
        self.nm_immediate: Optional[Boolean] = None


class UdpNmClusterCouplingBuilder:
    """Builder for UdpNmClusterCoupling."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpNmClusterCoupling = UdpNmClusterCoupling()

    def build(self) -> UdpNmClusterCoupling:
        """Build and return UdpNmClusterCoupling object.

        Returns:
            UdpNmClusterCoupling instance
        """
        # TODO: Add validation
        return self._obj
