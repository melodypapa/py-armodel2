"""Ipv4Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_arp_props import (
    Ipv4ArpProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_auto_ip_props import (
    Ipv4AutoIpProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_fragmentation_props import (
    Ipv4FragmentationProps,
)


class Ipv4Props(ARObject):
    """AUTOSAR Ipv4Props."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arp_props: Optional[Ipv4ArpProps]
    auto_ip_props: Optional[Ipv4AutoIpProps]
    fragmentation: Optional[Ipv4FragmentationProps]
    def __init__(self) -> None:
        """Initialize Ipv4Props."""
        super().__init__()
        self.arp_props: Optional[Ipv4ArpProps] = None
        self.auto_ip_props: Optional[Ipv4AutoIpProps] = None
        self.fragmentation: Optional[Ipv4FragmentationProps] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv4Props to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize arp_props
        if self.arp_props is not None:
            serialized = SerializationHelper.serialize_item(self.arp_props, "Ipv4ArpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize auto_ip_props
        if self.auto_ip_props is not None:
            serialized = SerializationHelper.serialize_item(self.auto_ip_props, "Ipv4AutoIpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-IP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fragmentation
        if self.fragmentation is not None:
            serialized = SerializationHelper.serialize_item(self.fragmentation, "Ipv4FragmentationProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAGMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4Props":
        """Deserialize XML element to Ipv4Props object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4Props object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse arp_props
        child = SerializationHelper.find_child_element(element, "ARP-PROPS")
        if child is not None:
            arp_props_value = SerializationHelper.deserialize_by_tag(child, "Ipv4ArpProps")
            obj.arp_props = arp_props_value

        # Parse auto_ip_props
        child = SerializationHelper.find_child_element(element, "AUTO-IP-PROPS")
        if child is not None:
            auto_ip_props_value = SerializationHelper.deserialize_by_tag(child, "Ipv4AutoIpProps")
            obj.auto_ip_props = auto_ip_props_value

        # Parse fragmentation
        child = SerializationHelper.find_child_element(element, "FRAGMENTATION")
        if child is not None:
            fragmentation_value = SerializationHelper.deserialize_by_tag(child, "Ipv4FragmentationProps")
            obj.fragmentation = fragmentation_value

        return obj



class Ipv4PropsBuilder:
    """Builder for Ipv4Props."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4Props = Ipv4Props()

    def build(self) -> Ipv4Props:
        """Build and return Ipv4Props object.

        Returns:
            Ipv4Props instance
        """
        # TODO: Add validation
        return self._obj
