"""Ieee1722TpEthernetFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import (
    AbstractEthernetFrame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class Ieee1722TpEthernetFrame(AbstractEthernetFrame):
    """AUTOSAR Ieee1722TpEthernetFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("relative", None, True, False, None),  # relative
        ("stream_identifier", None, True, False, None),  # streamIdentifier
        ("sub_type", None, True, False, None),  # subType
        ("version", None, True, False, None),  # version
    ]

    def __init__(self) -> None:
        """Initialize Ieee1722TpEthernetFrame."""
        super().__init__()
        self.relative: Optional[TimeValue] = None
        self.stream_identifier: Optional[PositiveInteger] = None
        self.sub_type: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ieee1722TpEthernetFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ieee1722TpEthernetFrame":
        """Create Ieee1722TpEthernetFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ieee1722TpEthernetFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ieee1722TpEthernetFrame since parent returns ARObject
        return cast("Ieee1722TpEthernetFrame", obj)


class Ieee1722TpEthernetFrameBuilder:
    """Builder for Ieee1722TpEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ieee1722TpEthernetFrame = Ieee1722TpEthernetFrame()

    def build(self) -> Ieee1722TpEthernetFrame:
        """Build and return Ieee1722TpEthernetFrame object.

        Returns:
            Ieee1722TpEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
