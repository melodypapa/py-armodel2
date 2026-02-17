"""NmConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 672)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "nm_clusters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NmCluster,
        ),  # nmClusters
        "nm_cluster_couplings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NmClusterCoupling,
        ),  # nmClusterCouplings
        "nm_if_ecus": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NmEcu,
        ),  # nmIfEcus
    }

    def __init__(self) -> None:
        """Initialize NmConfig."""
        super().__init__()
        self.nm_clusters: list[NmCluster] = []
        self.nm_cluster_couplings: list[NmClusterCoupling] = []
        self.nm_if_ecus: list[NmEcu] = []


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
