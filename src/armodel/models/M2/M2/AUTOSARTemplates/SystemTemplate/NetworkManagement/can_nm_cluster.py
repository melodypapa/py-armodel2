"""CanNmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 682)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "nm_busload": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmBusload
        "nm_car_wake_up": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmCarWakeUp
        "nm_car_wake_up_filter_node_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmCarWakeUpFilterNodeId
        "nm_cbv_position": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmCbvPosition
        "nm_immediate": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmImmediate
        "nm_message": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmMessage
        "nm_msg_cycle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmMsgCycle
        "nm_network": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmNetwork
        "nm_nid_position": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmNidPosition
        "nm_remote": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmRemote
        "nm_repeat": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmRepeat
        "nm_wait_bus": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmWaitBus
    }

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
