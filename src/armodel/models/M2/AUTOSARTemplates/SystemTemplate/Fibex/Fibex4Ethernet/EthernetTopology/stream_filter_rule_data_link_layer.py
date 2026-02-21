"""StreamFilterRuleDataLinkLayer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_mac_address import (
    StreamFilterMACAddress,
)


class StreamFilterRuleDataLinkLayer(ARObject):
    """AUTOSAR StreamFilterRuleDataLinkLayer."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_mac: Optional[StreamFilterMACAddress]
    ether_type: Optional[PositiveInteger]
    source_mac: Optional[StreamFilterMACAddress]
    vlan_id: Optional[PositiveInteger]
    vlan_priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize StreamFilterRuleDataLinkLayer."""
        super().__init__()
        self.destination_mac: Optional[StreamFilterMACAddress] = None
        self.ether_type: Optional[PositiveInteger] = None
        self.source_mac: Optional[StreamFilterMACAddress] = None
        self.vlan_id: Optional[PositiveInteger] = None
        self.vlan_priority: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterRuleDataLinkLayer to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize destination_mac
        if self.destination_mac is not None:
            serialized = SerializationHelper.serialize_item(self.destination_mac, "StreamFilterMACAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-MAC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ether_type
        if self.ether_type is not None:
            serialized = SerializationHelper.serialize_item(self.ether_type, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ETHER-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_mac
        if self.source_mac is not None:
            serialized = SerializationHelper.serialize_item(self.source_mac, "StreamFilterMACAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-MAC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan_id
        if self.vlan_id is not None:
            serialized = SerializationHelper.serialize_item(self.vlan_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan_priority
        if self.vlan_priority is not None:
            serialized = SerializationHelper.serialize_item(self.vlan_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterRuleDataLinkLayer":
        """Deserialize XML element to StreamFilterRuleDataLinkLayer object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterRuleDataLinkLayer object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destination_mac
        child = SerializationHelper.find_child_element(element, "DESTINATION-MAC")
        if child is not None:
            destination_mac_value = SerializationHelper.deserialize_by_tag(child, "StreamFilterMACAddress")
            obj.destination_mac = destination_mac_value

        # Parse ether_type
        child = SerializationHelper.find_child_element(element, "ETHER-TYPE")
        if child is not None:
            ether_type_value = child.text
            obj.ether_type = ether_type_value

        # Parse source_mac
        child = SerializationHelper.find_child_element(element, "SOURCE-MAC")
        if child is not None:
            source_mac_value = SerializationHelper.deserialize_by_tag(child, "StreamFilterMACAddress")
            obj.source_mac = source_mac_value

        # Parse vlan_id
        child = SerializationHelper.find_child_element(element, "VLAN-ID")
        if child is not None:
            vlan_id_value = child.text
            obj.vlan_id = vlan_id_value

        # Parse vlan_priority
        child = SerializationHelper.find_child_element(element, "VLAN-PRIORITY")
        if child is not None:
            vlan_priority_value = child.text
            obj.vlan_priority = vlan_priority_value

        return obj



class StreamFilterRuleDataLinkLayerBuilder:
    """Builder for StreamFilterRuleDataLinkLayer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterRuleDataLinkLayer = StreamFilterRuleDataLinkLayer()

    def build(self) -> StreamFilterRuleDataLinkLayer:
        """Build and return StreamFilterRuleDataLinkLayer object.

        Returns:
            StreamFilterRuleDataLinkLayer instance
        """
        # TODO: Add validation
        return self._obj
