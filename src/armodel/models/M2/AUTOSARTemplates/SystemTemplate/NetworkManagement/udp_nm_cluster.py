"""UdpNmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 687)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
    TimeValue,
)


class UdpNmCluster(NmCluster):
    """AUTOSAR UdpNmCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_cbv_position: Optional[Integer]
    nm_immediate: Optional[PositiveInteger]
    nm_message: Optional[TimeValue]
    nm_msg_cycle: Optional[TimeValue]
    nm_network: Optional[TimeValue]
    nm_nid_position: Optional[Integer]
    nm_remote: Optional[TimeValue]
    nm_repeat: Optional[TimeValue]
    nm_wait_bus: Optional[TimeValue]
    vlan: Optional[Any]
    def __init__(self) -> None:
        """Initialize UdpNmCluster."""
        super().__init__()
        self.nm_cbv_position: Optional[Integer] = None
        self.nm_immediate: Optional[PositiveInteger] = None
        self.nm_message: Optional[TimeValue] = None
        self.nm_msg_cycle: Optional[TimeValue] = None
        self.nm_network: Optional[TimeValue] = None
        self.nm_nid_position: Optional[Integer] = None
        self.nm_remote: Optional[TimeValue] = None
        self.nm_repeat: Optional[TimeValue] = None
        self.nm_wait_bus: Optional[TimeValue] = None
        self.vlan: Optional[Any] = None


class UdpNmClusterBuilder:
    """Builder for UdpNmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpNmCluster = UdpNmCluster()

    def build(self) -> UdpNmCluster:
        """Build and return UdpNmCluster object.

        Returns:
            UdpNmCluster instance
        """
        # TODO: Add validation
        return self._obj
