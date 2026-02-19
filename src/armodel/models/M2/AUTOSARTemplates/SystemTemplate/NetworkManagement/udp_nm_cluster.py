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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UdpNmCluster":
        """Deserialize XML element to UdpNmCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UdpNmCluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse nm_cbv_position
        child = ARObject._find_child_element(element, "NM-CBV-POSITION")
        if child is not None:
            nm_cbv_position_value = child.text
            obj.nm_cbv_position = nm_cbv_position_value

        # Parse nm_immediate
        child = ARObject._find_child_element(element, "NM-IMMEDIATE")
        if child is not None:
            nm_immediate_value = child.text
            obj.nm_immediate = nm_immediate_value

        # Parse nm_message
        child = ARObject._find_child_element(element, "NM-MESSAGE")
        if child is not None:
            nm_message_value = child.text
            obj.nm_message = nm_message_value

        # Parse nm_msg_cycle
        child = ARObject._find_child_element(element, "NM-MSG-CYCLE")
        if child is not None:
            nm_msg_cycle_value = child.text
            obj.nm_msg_cycle = nm_msg_cycle_value

        # Parse nm_network
        child = ARObject._find_child_element(element, "NM-NETWORK")
        if child is not None:
            nm_network_value = child.text
            obj.nm_network = nm_network_value

        # Parse nm_nid_position
        child = ARObject._find_child_element(element, "NM-NID-POSITION")
        if child is not None:
            nm_nid_position_value = child.text
            obj.nm_nid_position = nm_nid_position_value

        # Parse nm_remote
        child = ARObject._find_child_element(element, "NM-REMOTE")
        if child is not None:
            nm_remote_value = child.text
            obj.nm_remote = nm_remote_value

        # Parse nm_repeat
        child = ARObject._find_child_element(element, "NM-REPEAT")
        if child is not None:
            nm_repeat_value = child.text
            obj.nm_repeat = nm_repeat_value

        # Parse nm_wait_bus
        child = ARObject._find_child_element(element, "NM-WAIT-BUS")
        if child is not None:
            nm_wait_bus_value = child.text
            obj.nm_wait_bus = nm_wait_bus_value

        # Parse vlan
        child = ARObject._find_child_element(element, "VLAN")
        if child is not None:
            vlan_value = child.text
            obj.vlan = vlan_value

        return obj



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
