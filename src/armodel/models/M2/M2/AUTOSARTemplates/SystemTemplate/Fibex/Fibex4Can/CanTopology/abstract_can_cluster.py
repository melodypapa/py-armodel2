"""AbstractCanCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.can_cluster_bus_off_recovery import (
    CanClusterBusOffRecovery,
)


class AbstractCanCluster(ARObject):
    """AUTOSAR AbstractCanCluster."""

    def __init__(self) -> None:
        """Initialize AbstractCanCluster."""
        super().__init__()
        self.bus_off_recovery: Optional[CanClusterBusOffRecovery] = None
        self.can_fd_baudrate: Optional[PositiveUnlimitedInteger] = None
        self.can_xl_baudrate: Optional[PositiveUnlimitedInteger] = None


class AbstractCanClusterBuilder:
    """Builder for AbstractCanCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCluster = AbstractCanCluster()

    def build(self) -> AbstractCanCluster:
        """Build and return AbstractCanCluster object.

        Returns:
            AbstractCanCluster instance
        """
        # TODO: Add validation
        return self._obj
