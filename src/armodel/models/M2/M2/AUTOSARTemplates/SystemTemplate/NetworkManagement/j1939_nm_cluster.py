"""J1939NmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 691)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class J1939NmCluster(NmCluster):
    """AUTOSAR J1939NmCluster."""

    def __init__(self) -> None:
        """Initialize J1939NmCluster."""
        super().__init__()
        self.address_claim: Optional[Boolean] = None
        self.uses_dynamic: Optional[Boolean] = None


class J1939NmClusterBuilder:
    """Builder for J1939NmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NmCluster = J1939NmCluster()

    def build(self) -> J1939NmCluster:
        """Build and return J1939NmCluster object.

        Returns:
            J1939NmCluster instance
        """
        # TODO: Add validation
        return self._obj
