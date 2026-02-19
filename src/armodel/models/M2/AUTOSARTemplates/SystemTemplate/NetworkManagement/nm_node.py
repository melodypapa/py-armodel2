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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmNode":
        """Deserialize XML element to NmNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmNode object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse controller
        child = ARObject._find_child_element(element, "CONTROLLER")
        if child is not None:
            controller_value = child.text
            obj.controller = controller_value

        # Parse nm_coord_cluster
        child = ARObject._find_child_element(element, "NM-COORD-CLUSTER")
        if child is not None:
            nm_coord_cluster_value = child.text
            obj.nm_coord_cluster = nm_coord_cluster_value

        # Parse nm_coordinator_role
        child = ARObject._find_child_element(element, "NM-COORDINATOR-ROLE")
        if child is not None:
            nm_coordinator_role_value = child.text
            obj.nm_coordinator_role = nm_coordinator_role_value

        # Parse nm_if_ecu
        child = ARObject._find_child_element(element, "NM-IF-ECU")
        if child is not None:
            nm_if_ecu_value = ARObject._deserialize_by_tag(child, "NmEcu")
            obj.nm_if_ecu = nm_if_ecu_value

        # Parse nm_node_id
        child = ARObject._find_child_element(element, "NM-NODE-ID")
        if child is not None:
            nm_node_id_value = child.text
            obj.nm_node_id = nm_node_id_value

        # Parse nm_passive
        child = ARObject._find_child_element(element, "NM-PASSIVE")
        if child is not None:
            nm_passive_value = child.text
            obj.nm_passive = nm_passive_value

        # Parse rx_nm_pdus (list)
        obj.rx_nm_pdus = []
        for child in ARObject._find_all_child_elements(element, "RX-NM-PDUS"):
            rx_nm_pdus_value = ARObject._deserialize_by_tag(child, "NmPdu")
            obj.rx_nm_pdus.append(rx_nm_pdus_value)

        # Parse tx_nm_pdus (list)
        obj.tx_nm_pdus = []
        for child in ARObject._find_all_child_elements(element, "TX-NM-PDUS"):
            tx_nm_pdus_value = ARObject._deserialize_by_tag(child, "NmPdu")
            obj.tx_nm_pdus.append(tx_nm_pdus_value)

        return obj



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
