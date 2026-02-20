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

    def serialize(self) -> ET.Element:
        """Serialize TDEventFrameEthernet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventFrameEthernet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize static_socket
        if self.static_socket is not None:
            serialized = ARObject._serialize_item(self.static_socket, "StaticSocketConnection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATIC-SOCKET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_type
        if self.td_event_type is not None:
            serialized = ARObject._serialize_item(self.td_event_type, "TDEventFrameEthernet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_header_id_filters (list to container "TD-HEADER-ID-FILTERS")
        if self.td_header_id_filters:
            wrapper = ET.Element("TD-HEADER-ID-FILTERS")
            for item in self.td_header_id_filters:
                serialized = ARObject._serialize_item(item, "TDHeaderIdRange")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize td_pdu_triggering_refs (list to container "TD-PDU-TRIGGERING-REFS")
        if self.td_pdu_triggering_refs:
            wrapper = ET.Element("TD-PDU-TRIGGERING-REFS")
            for item in self.td_pdu_triggering_refs:
                serialized = ARObject._serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("TD-PDU-TRIGGERING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventFrameEthernet":
        """Deserialize XML element to TDEventFrameEthernet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventFrameEthernet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventFrameEthernet, cls).deserialize(element)

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

        # Parse td_header_id_filters (list from container "TD-HEADER-ID-FILTERS")
        obj.td_header_id_filters = []
        container = ARObject._find_child_element(element, "TD-HEADER-ID-FILTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.td_header_id_filters.append(child_value)

        # Parse td_pdu_triggering_refs (list from container "TD-PDU-TRIGGERING-REFS")
        obj.td_pdu_triggering_refs = []
        container = ARObject._find_child_element(element, "TD-PDU-TRIGGERING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.td_pdu_triggering_refs.append(child_value)

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
