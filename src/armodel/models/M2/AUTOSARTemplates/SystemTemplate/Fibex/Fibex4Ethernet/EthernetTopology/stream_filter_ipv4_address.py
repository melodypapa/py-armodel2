"""StreamFilterIpv4Address AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
)


class StreamFilterIpv4Address(ARObject):
    """AUTOSAR StreamFilterIpv4Address."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ipv4_address: Optional[Ip4AddressString]
    def __init__(self) -> None:
        """Initialize StreamFilterIpv4Address."""
        super().__init__()
        self.ipv4_address: Optional[Ip4AddressString] = None

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterIpv4Address to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StreamFilterIpv4Address, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ipv4_address
        if self.ipv4_address is not None:
            serialized = SerializationHelper.serialize_item(self.ipv4_address, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterIpv4Address":
        """Deserialize XML element to StreamFilterIpv4Address object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterIpv4Address object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StreamFilterIpv4Address, cls).deserialize(element)

        # Parse ipv4_address
        child = SerializationHelper.find_child_element(element, "IPV4-ADDRESS")
        if child is not None:
            ipv4_address_value = child.text
            obj.ipv4_address = ipv4_address_value

        return obj



class StreamFilterIpv4AddressBuilder:
    """Builder for StreamFilterIpv4Address."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterIpv4Address = StreamFilterIpv4Address()

    def build(self) -> StreamFilterIpv4Address:
        """Build and return StreamFilterIpv4Address object.

        Returns:
            StreamFilterIpv4Address instance
        """
        # TODO: Add validation
        return self._obj
