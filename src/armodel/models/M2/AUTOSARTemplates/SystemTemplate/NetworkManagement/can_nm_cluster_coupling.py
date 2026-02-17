"""CanNmClusterCoupling AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 684)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "coupled_clusters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CanNmCluster,
        ),  # coupledClusters
        "nm_busload_reduction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (BooleanEnabled),
        ),  # nmBusloadReduction
        "nm_immediate": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmImmediate
    }

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
