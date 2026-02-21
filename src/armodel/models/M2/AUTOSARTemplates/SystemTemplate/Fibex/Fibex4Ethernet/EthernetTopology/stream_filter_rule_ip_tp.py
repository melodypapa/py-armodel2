"""StreamFilterRuleIpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_ipv6_address import (
    StreamFilterIpv6Address,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_port_range import (
    StreamFilterPortRange,
)


class StreamFilterRuleIpTp(ARObject):
    """AUTOSAR StreamFilterRuleIpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination: Optional[StreamFilterIpv6Address]
    destination_ports: list[StreamFilterPortRange]
    source: Optional[StreamFilterIpv6Address]
    source_ports: list[StreamFilterPortRange]
    def __init__(self) -> None:
        """Initialize StreamFilterRuleIpTp."""
        super().__init__()
        self.destination: Optional[StreamFilterIpv6Address] = None
        self.destination_ports: list[StreamFilterPortRange] = []
        self.source: Optional[StreamFilterIpv6Address] = None
        self.source_ports: list[StreamFilterPortRange] = []

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterRuleIpTp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize destination
        if self.destination is not None:
            serialized = SerializationHelper.serialize_item(self.destination, "StreamFilterIpv6Address")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize destination_ports (list to container "DESTINATION-PORTS")
        if self.destination_ports:
            wrapper = ET.Element("DESTINATION-PORTS")
            for item in self.destination_ports:
                serialized = SerializationHelper.serialize_item(item, "StreamFilterPortRange")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source
        if self.source is not None:
            serialized = SerializationHelper.serialize_item(self.source, "StreamFilterIpv6Address")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_ports (list to container "SOURCE-PORTS")
        if self.source_ports:
            wrapper = ET.Element("SOURCE-PORTS")
            for item in self.source_ports:
                serialized = SerializationHelper.serialize_item(item, "StreamFilterPortRange")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterRuleIpTp":
        """Deserialize XML element to StreamFilterRuleIpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterRuleIpTp object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destination
        child = SerializationHelper.find_child_element(element, "DESTINATION")
        if child is not None:
            destination_value = SerializationHelper.deserialize_by_tag(child, "StreamFilterIpv6Address")
            obj.destination = destination_value

        # Parse destination_ports (list from container "DESTINATION-PORTS")
        obj.destination_ports = []
        container = SerializationHelper.find_child_element(element, "DESTINATION-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.destination_ports.append(child_value)

        # Parse source
        child = SerializationHelper.find_child_element(element, "SOURCE")
        if child is not None:
            source_value = SerializationHelper.deserialize_by_tag(child, "StreamFilterIpv6Address")
            obj.source = source_value

        # Parse source_ports (list from container "SOURCE-PORTS")
        obj.source_ports = []
        container = SerializationHelper.find_child_element(element, "SOURCE-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.source_ports.append(child_value)

        return obj



class StreamFilterRuleIpTpBuilder:
    """Builder for StreamFilterRuleIpTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterRuleIpTp = StreamFilterRuleIpTp()

    def build(self) -> StreamFilterRuleIpTp:
        """Build and return StreamFilterRuleIpTp object.

        Returns:
            StreamFilterRuleIpTp instance
        """
        # TODO: Add validation
        return self._obj
