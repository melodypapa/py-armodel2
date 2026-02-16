"""Ipv4AutoIpProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class Ipv4AutoIpProps(ARObject):
    """AUTOSAR Ipv4AutoIpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_ip_auto_ip_init", None, True, False, None),  # tcpIpAutoIpInit
    ]

    def __init__(self) -> None:
        """Initialize Ipv4AutoIpProps."""
        super().__init__()
        self.tcp_ip_auto_ip_init: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ipv4AutoIpProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4AutoIpProps":
        """Create Ipv4AutoIpProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ipv4AutoIpProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ipv4AutoIpProps since parent returns ARObject
        return cast("Ipv4AutoIpProps", obj)


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
