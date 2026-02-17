"""TDEventFrameEthernet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 69)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.static_socket_connection import (
    StaticSocketConnection,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_header_id_range import (
    TDHeaderIdRange,
)


class TDEventFrameEthernet(TDEventCom):
    """AUTOSAR TDEventFrameEthernet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "static_socket": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=StaticSocketConnection,
        ),  # staticSocket
        "td_event_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TDEventFrameEthernet,
        ),  # tdEventType
        "td_header_id_filters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TDHeaderIdRange,
        ),  # tdHeaderIdFilters
        "td_pdu_triggerings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PduTriggering,
        ),  # tdPduTriggerings
    }

    def __init__(self) -> None:
        """Initialize TDEventFrameEthernet."""
        super().__init__()
        self.static_socket: Optional[StaticSocketConnection] = None
        self.td_event_type: Optional[TDEventFrameEthernet] = None
        self.td_header_id_filters: list[TDHeaderIdRange] = []
        self.td_pdu_triggerings: list[PduTriggering] = []


class TDEventFrameEthernetBuilder:
    """Builder for TDEventFrameEthernet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventFrameEthernet = TDEventFrameEthernet()

    def build(self) -> TDEventFrameEthernet:
        """Build and return TDEventFrameEthernet object.

        Returns:
            TDEventFrameEthernet instance
        """
        # TODO: Add validation
        return self._obj
