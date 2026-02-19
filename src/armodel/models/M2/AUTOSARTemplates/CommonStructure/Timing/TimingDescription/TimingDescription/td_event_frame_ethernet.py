"""TDEventFrameEthernet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 69)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    static_socket: Optional[StaticSocketConnection]
    td_event_type: Optional[TDEventFrameEthernet]
    td_header_id_filters: list[TDHeaderIdRange]
    td_pdu_triggering_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventFrameEthernet."""
        super().__init__()
        self.static_socket: Optional[StaticSocketConnection] = None
        self.td_event_type: Optional[TDEventFrameEthernet] = None
        self.td_header_id_filters: list[TDHeaderIdRange] = []
        self.td_pdu_triggering_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventFrameEthernet":
        """Deserialize XML element to TDEventFrameEthernet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventFrameEthernet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse static_socket
        child = ARObject._find_child_element(element, "STATIC-SOCKET")
        if child is not None:
            static_socket_value = ARObject._deserialize_by_tag(child, "StaticSocketConnection")
            obj.static_socket = static_socket_value

        # Parse td_event_type
        child = ARObject._find_child_element(element, "TD-EVENT-TYPE")
        if child is not None:
            td_event_type_value = ARObject._deserialize_by_tag(child, "TDEventFrameEthernet")
            obj.td_event_type = td_event_type_value

        # Parse td_header_id_filters (list)
        obj.td_header_id_filters = []
        for child in ARObject._find_all_child_elements(element, "TD-HEADER-ID-FILTERS"):
            td_header_id_filters_value = ARObject._deserialize_by_tag(child, "TDHeaderIdRange")
            obj.td_header_id_filters.append(td_header_id_filters_value)

        # Parse td_pdu_triggering_refs (list)
        obj.td_pdu_triggering_refs = []
        for child in ARObject._find_all_child_elements(element, "TD-PDU-TRIGGERINGS"):
            td_pdu_triggering_refs_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.td_pdu_triggering_refs.append(td_pdu_triggering_refs_value)

        return obj



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
