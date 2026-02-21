"""Ipv4AutoIpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 147)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class Ipv4AutoIpProps(ARObject):
    """AUTOSAR Ipv4AutoIpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_auto_ip_init: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize Ipv4AutoIpProps."""
        super().__init__()
        self.tcp_ip_auto_ip_init: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv4AutoIpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize tcp_ip_auto_ip_init
        if self.tcp_ip_auto_ip_init is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_auto_ip_init, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-AUTO-IP-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4AutoIpProps":
        """Deserialize XML element to Ipv4AutoIpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4AutoIpProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tcp_ip_auto_ip_init
        child = SerializationHelper.find_child_element(element, "TCP-IP-AUTO-IP-INIT")
        if child is not None:
            tcp_ip_auto_ip_init_value = child.text
            obj.tcp_ip_auto_ip_init = tcp_ip_auto_ip_init_value

        return obj



class Ipv4AutoIpPropsBuilder:
    """Builder for Ipv4AutoIpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4AutoIpProps = Ipv4AutoIpProps()

    def build(self) -> Ipv4AutoIpProps:
        """Build and return Ipv4AutoIpProps object.

        Returns:
            Ipv4AutoIpProps instance
        """
        # TODO: Add validation
        return self._obj
