"""FlexrayNmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 678)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)


class FlexrayNmCluster(NmCluster):
    """AUTOSAR FlexrayNmCluster."""

    def __init__(self) -> None:
        """Initialize FlexrayNmCluster."""
        super().__init__()
        self.nm_car_wake_up: Optional[Boolean] = None
        self.nm_data_cycle: Optional[Integer] = None
        self.nm_main: Optional[TimeValue] = None
        self.nm_remote: Optional[TimeValue] = None
        self.nm_repeat: Optional[TimeValue] = None
        self.nm_repetition: Optional[Integer] = None
        self.nm_voting_cycle: Optional[Integer] = None


class FlexrayNmClusterBuilder:
    """Builder for FlexrayNmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmCluster = FlexrayNmCluster()

    def build(self) -> FlexrayNmCluster:
        """Build and return FlexrayNmCluster object.

        Returns:
            FlexrayNmCluster instance
        """
        # TODO: Add validation
        return self._obj
