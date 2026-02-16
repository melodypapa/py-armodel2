"""CanNmCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)


class CanNmCluster(NmCluster):
    """AUTOSAR CanNmCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("nm_busload", None, True, False, None),  # nmBusload
        ("nm_car_wake_up", None, True, False, None),  # nmCarWakeUp
        ("nm_car_wake_up_filter_node_id", None, True, False, None),  # nmCarWakeUpFilterNodeId
        ("nm_cbv_position", None, True, False, None),  # nmCbvPosition
        ("nm_immediate", None, True, False, None),  # nmImmediate
        ("nm_message", None, True, False, None),  # nmMessage
        ("nm_msg_cycle", None, True, False, None),  # nmMsgCycle
        ("nm_network", None, True, False, None),  # nmNetwork
        ("nm_nid_position", None, True, False, None),  # nmNidPosition
        ("nm_remote", None, True, False, None),  # nmRemote
        ("nm_repeat", None, True, False, None),  # nmRepeat
        ("nm_wait_bus", None, True, False, None),  # nmWaitBus
    ]

    def __init__(self) -> None:
        """Initialize CanNmCluster."""
        super().__init__()
        self.nm_busload: Optional[Boolean] = None
        self.nm_car_wake_up: Optional[PositiveInteger] = None
        self.nm_car_wake_up_filter_node_id: Optional[PositiveInteger] = None
        self.nm_cbv_position: Optional[Integer] = None
        self.nm_immediate: Optional[PositiveInteger] = None
        self.nm_message: Optional[TimeValue] = None
        self.nm_msg_cycle: Optional[TimeValue] = None
        self.nm_network: Optional[TimeValue] = None
        self.nm_nid_position: Optional[Integer] = None
        self.nm_remote: Optional[TimeValue] = None
        self.nm_repeat: Optional[TimeValue] = None
        self.nm_wait_bus: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanNmCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanNmCluster":
        """Create CanNmCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanNmCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanNmCluster since parent returns ARObject
        return cast("CanNmCluster", obj)


class CanNmClusterBuilder:
    """Builder for CanNmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanNmCluster = CanNmCluster()

    def build(self) -> CanNmCluster:
        """Build and return CanNmCluster object.

        Returns:
            CanNmCluster instance
        """
        # TODO: Add validation
        return self._obj
