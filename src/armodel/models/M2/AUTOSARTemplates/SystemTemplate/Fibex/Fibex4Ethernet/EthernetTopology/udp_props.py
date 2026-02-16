"""UdpProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class UdpProps(ARObject):
    """AUTOSAR UdpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("udp_ttl", None, True, False, None),  # udpTtl
    ]

    def __init__(self) -> None:
        """Initialize UdpProps."""
        super().__init__()
        self.udp_ttl: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UdpProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UdpProps":
        """Create UdpProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UdpProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UdpProps since parent returns ARObject
        return cast("UdpProps", obj)


class UdpPropsBuilder:
    """Builder for UdpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpProps = UdpProps()

    def build(self) -> UdpProps:
        """Build and return UdpProps object.

        Returns:
            UdpProps instance
        """
        # TODO: Add validation
        return self._obj
