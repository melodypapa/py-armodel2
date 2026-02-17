"""J1939SharedAddressCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 694)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.j1939_cluster import (
    J1939Cluster,
)


class J1939SharedAddressCluster(Identifiable):
    """AUTOSAR J1939SharedAddressCluster."""

    participatings: list[J1939Cluster]
    def __init__(self) -> None:
        """Initialize J1939SharedAddressCluster."""
        super().__init__()
        self.participatings: list[J1939Cluster] = []


class J1939SharedAddressClusterBuilder:
    """Builder for J1939SharedAddressCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939SharedAddressCluster = J1939SharedAddressCluster()

    def build(self) -> J1939SharedAddressCluster:
        """Build and return J1939SharedAddressCluster object.

        Returns:
            J1939SharedAddressCluster instance
        """
        # TODO: Add validation
        return self._obj
