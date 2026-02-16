"""GenericEthernetFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import (
    AbstractEthernetFrame,
)


class GenericEthernetFrame(AbstractEthernetFrame):
    """AUTOSAR GenericEthernetFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize GenericEthernetFrame."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GenericEthernetFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GenericEthernetFrame":
        """Create GenericEthernetFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GenericEthernetFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GenericEthernetFrame since parent returns ARObject
        return cast("GenericEthernetFrame", obj)


class GenericEthernetFrameBuilder:
    """Builder for GenericEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GenericEthernetFrame = GenericEthernetFrame()

    def build(self) -> GenericEthernetFrame:
        """Build and return GenericEthernetFrame object.

        Returns:
            GenericEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
