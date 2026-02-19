"""StreamFilterMACAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
)


class StreamFilterMACAddress(ARObject):
    """AUTOSAR StreamFilterMACAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mac_address_string: Optional[MacAddressString]
    def __init__(self) -> None:
        """Initialize StreamFilterMACAddress."""
        super().__init__()
        self.mac_address_string: Optional[MacAddressString] = None
    def serialize(self) -> ET.Element:
        """Serialize StreamFilterMACAddress to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize mac_address_string
        if self.mac_address_string is not None:
            serialized = ARObject._serialize_item(self.mac_address_string, "MacAddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAC-ADDRESS-STRING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterMACAddress":
        """Deserialize XML element to StreamFilterMACAddress object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterMACAddress object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mac_address_string
        child = ARObject._find_child_element(element, "MAC-ADDRESS-STRING")
        if child is not None:
            mac_address_string_value = child.text
            obj.mac_address_string = mac_address_string_value

        return obj



class StreamFilterMACAddressBuilder:
    """Builder for StreamFilterMACAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterMACAddress = StreamFilterMACAddress()

    def build(self) -> StreamFilterMACAddress:
        """Build and return StreamFilterMACAddress object.

        Returns:
            StreamFilterMACAddress instance
        """
        # TODO: Add validation
        return self._obj
