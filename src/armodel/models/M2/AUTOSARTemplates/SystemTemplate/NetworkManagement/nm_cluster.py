"""NmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 672)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)


class NmCluster(Identifiable):
    """AUTOSAR NmCluster."""
    """Abstract base class - do not instantiate directly."""

    communication_cluster: Optional[CommunicationCluster]
    nm_channel: Optional[Boolean]
    nm_node: Optional[Boolean]
    nm_node_id_enabled: Optional[Boolean]
    nm_pnc: Optional[Boolean]
    nm_repeat_msg_ind_enabled: Optional[Boolean]
    nm: Optional[Boolean]
    pnc_cluster: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize NmCluster."""
        super().__init__()
        self.communication_cluster: Optional[CommunicationCluster] = None
        self.nm_channel: Optional[Boolean] = None
        self.nm_node: Optional[Boolean] = None
        self.nm_node_id_enabled: Optional[Boolean] = None
        self.nm_pnc: Optional[Boolean] = None
        self.nm_repeat_msg_ind_enabled: Optional[Boolean] = None
        self.nm: Optional[Boolean] = None
        self.pnc_cluster: Optional[PositiveInteger] = None


class NmClusterBuilder:
    """Builder for NmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmCluster = NmCluster()

    def build(self) -> NmCluster:
        """Build and return NmCluster object.

        Returns:
            NmCluster instance
        """
        # TODO: Add validation
        return self._obj
