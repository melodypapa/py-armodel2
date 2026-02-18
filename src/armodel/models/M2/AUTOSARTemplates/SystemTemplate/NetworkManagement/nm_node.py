"""NmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    NmCoordinatorRoleEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
    NmPdu,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_ecu import (
        NmEcu,
    )

from abc import ABC, abstractmethod


class NmNode(Identifiable, ABC):
    """AUTOSAR NmNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    controller: Optional[Any]
    nm_coord_cluster: Optional[PositiveInteger]
    nm_coordinator_role: Optional[NmCoordinatorRoleEnum]
    nm_if_ecu: Optional[NmEcu]
    nm_node_id: Optional[Integer]
    nm_passive: Optional[Boolean]
    rx_nm_pdus: list[NmPdu]
    tx_nm_pdus: list[NmPdu]
    def __init__(self) -> None:
        """Initialize NmNode."""
        super().__init__()
        self.controller: Optional[Any] = None
        self.nm_coord_cluster: Optional[PositiveInteger] = None
        self.nm_coordinator_role: Optional[NmCoordinatorRoleEnum] = None
        self.nm_if_ecu: Optional[NmEcu] = None
        self.nm_node_id: Optional[Integer] = None
        self.nm_passive: Optional[Boolean] = None
        self.rx_nm_pdus: list[NmPdu] = []
        self.tx_nm_pdus: list[NmPdu] = []


class NmNodeBuilder:
    """Builder for NmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmNode = NmNode()

    def build(self) -> NmNode:
        """Build and return NmNode object.

        Returns:
            NmNode instance
        """
        # TODO: Add validation
        return self._obj
