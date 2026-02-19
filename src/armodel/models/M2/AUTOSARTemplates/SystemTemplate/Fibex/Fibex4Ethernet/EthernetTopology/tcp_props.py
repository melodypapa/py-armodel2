"""TcpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 154)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class TcpProps(ARObject):
    """AUTOSAR TcpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_congestion: Optional[Boolean]
    tcp_delayed_ack: Optional[TimeValue]
    tcp_fast_recovery: Optional[Any]
    tcp_fast: Optional[Boolean]
    tcp_fin: Optional[TimeValue]
    tcp_keep_alive: Optional[TimeValue]
    tcp_max_rtx: Optional[PositiveInteger]
    tcp_msl: Optional[TimeValue]
    tcp_nagle: Optional[Boolean]
    tcp_receive_window_max: Optional[PositiveInteger]
    tcp: Optional[TimeValue]
    tcp_slow_start: Optional[Boolean]
    tcp_syn_max_rtx: Optional[PositiveInteger]
    tcp_syn_received: Optional[TimeValue]
    tcp_ttl: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize TcpProps."""
        super().__init__()
        self.tcp_congestion: Optional[Boolean] = None
        self.tcp_delayed_ack: Optional[TimeValue] = None
        self.tcp_fast_recovery: Optional[Any] = None
        self.tcp_fast: Optional[Boolean] = None
        self.tcp_fin: Optional[TimeValue] = None
        self.tcp_keep_alive: Optional[TimeValue] = None
        self.tcp_max_rtx: Optional[PositiveInteger] = None
        self.tcp_msl: Optional[TimeValue] = None
        self.tcp_nagle: Optional[Boolean] = None
        self.tcp_receive_window_max: Optional[PositiveInteger] = None
        self.tcp: Optional[TimeValue] = None
        self.tcp_slow_start: Optional[Boolean] = None
        self.tcp_syn_max_rtx: Optional[PositiveInteger] = None
        self.tcp_syn_received: Optional[TimeValue] = None
        self.tcp_ttl: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize TcpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize tcp_congestion
        if self.tcp_congestion is not None:
            serialized = ARObject._serialize_item(self.tcp_congestion, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-CONGESTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_delayed_ack
        if self.tcp_delayed_ack is not None:
            serialized = ARObject._serialize_item(self.tcp_delayed_ack, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-DELAYED-ACK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_fast_recovery
        if self.tcp_fast_recovery is not None:
            serialized = ARObject._serialize_item(self.tcp_fast_recovery, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-FAST-RECOVERY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_fast
        if self.tcp_fast is not None:
            serialized = ARObject._serialize_item(self.tcp_fast, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-FAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_fin
        if self.tcp_fin is not None:
            serialized = ARObject._serialize_item(self.tcp_fin, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-FIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_keep_alive
        if self.tcp_keep_alive is not None:
            serialized = ARObject._serialize_item(self.tcp_keep_alive, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-KEEP-ALIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_max_rtx
        if self.tcp_max_rtx is not None:
            serialized = ARObject._serialize_item(self.tcp_max_rtx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-MAX-RTX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_msl
        if self.tcp_msl is not None:
            serialized = ARObject._serialize_item(self.tcp_msl, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-MSL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_nagle
        if self.tcp_nagle is not None:
            serialized = ARObject._serialize_item(self.tcp_nagle, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-NAGLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_receive_window_max
        if self.tcp_receive_window_max is not None:
            serialized = ARObject._serialize_item(self.tcp_receive_window_max, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-RECEIVE-WINDOW-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp
        if self.tcp is not None:
            serialized = ARObject._serialize_item(self.tcp, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_slow_start
        if self.tcp_slow_start is not None:
            serialized = ARObject._serialize_item(self.tcp_slow_start, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-SLOW-START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_syn_max_rtx
        if self.tcp_syn_max_rtx is not None:
            serialized = ARObject._serialize_item(self.tcp_syn_max_rtx, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-SYN-MAX-RTX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_syn_received
        if self.tcp_syn_received is not None:
            serialized = ARObject._serialize_item(self.tcp_syn_received, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-SYN-RECEIVED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_ttl
        if self.tcp_ttl is not None:
            serialized = ARObject._serialize_item(self.tcp_ttl, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-TTL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpProps":
        """Deserialize XML element to TcpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tcp_congestion
        child = ARObject._find_child_element(element, "TCP-CONGESTION")
        if child is not None:
            tcp_congestion_value = child.text
            obj.tcp_congestion = tcp_congestion_value

        # Parse tcp_delayed_ack
        child = ARObject._find_child_element(element, "TCP-DELAYED-ACK")
        if child is not None:
            tcp_delayed_ack_value = child.text
            obj.tcp_delayed_ack = tcp_delayed_ack_value

        # Parse tcp_fast_recovery
        child = ARObject._find_child_element(element, "TCP-FAST-RECOVERY")
        if child is not None:
            tcp_fast_recovery_value = child.text
            obj.tcp_fast_recovery = tcp_fast_recovery_value

        # Parse tcp_fast
        child = ARObject._find_child_element(element, "TCP-FAST")
        if child is not None:
            tcp_fast_value = child.text
            obj.tcp_fast = tcp_fast_value

        # Parse tcp_fin
        child = ARObject._find_child_element(element, "TCP-FIN")
        if child is not None:
            tcp_fin_value = child.text
            obj.tcp_fin = tcp_fin_value

        # Parse tcp_keep_alive
        child = ARObject._find_child_element(element, "TCP-KEEP-ALIVE")
        if child is not None:
            tcp_keep_alive_value = child.text
            obj.tcp_keep_alive = tcp_keep_alive_value

        # Parse tcp_max_rtx
        child = ARObject._find_child_element(element, "TCP-MAX-RTX")
        if child is not None:
            tcp_max_rtx_value = child.text
            obj.tcp_max_rtx = tcp_max_rtx_value

        # Parse tcp_msl
        child = ARObject._find_child_element(element, "TCP-MSL")
        if child is not None:
            tcp_msl_value = child.text
            obj.tcp_msl = tcp_msl_value

        # Parse tcp_nagle
        child = ARObject._find_child_element(element, "TCP-NAGLE")
        if child is not None:
            tcp_nagle_value = child.text
            obj.tcp_nagle = tcp_nagle_value

        # Parse tcp_receive_window_max
        child = ARObject._find_child_element(element, "TCP-RECEIVE-WINDOW-MAX")
        if child is not None:
            tcp_receive_window_max_value = child.text
            obj.tcp_receive_window_max = tcp_receive_window_max_value

        # Parse tcp
        child = ARObject._find_child_element(element, "TCP")
        if child is not None:
            tcp_value = child.text
            obj.tcp = tcp_value

        # Parse tcp_slow_start
        child = ARObject._find_child_element(element, "TCP-SLOW-START")
        if child is not None:
            tcp_slow_start_value = child.text
            obj.tcp_slow_start = tcp_slow_start_value

        # Parse tcp_syn_max_rtx
        child = ARObject._find_child_element(element, "TCP-SYN-MAX-RTX")
        if child is not None:
            tcp_syn_max_rtx_value = child.text
            obj.tcp_syn_max_rtx = tcp_syn_max_rtx_value

        # Parse tcp_syn_received
        child = ARObject._find_child_element(element, "TCP-SYN-RECEIVED")
        if child is not None:
            tcp_syn_received_value = child.text
            obj.tcp_syn_received = tcp_syn_received_value

        # Parse tcp_ttl
        child = ARObject._find_child_element(element, "TCP-TTL")
        if child is not None:
            tcp_ttl_value = child.text
            obj.tcp_ttl = tcp_ttl_value

        return obj



class TcpPropsBuilder:
    """Builder for TcpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpProps = TcpProps()

    def build(self) -> TcpProps:
        """Build and return TcpProps object.

        Returns:
            TcpProps instance
        """
        # TODO: Add validation
        return self._obj
