"""Ieee1722Tp AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class Ieee1722Tp(TransportProtocolConfiguration):
    """AUTOSAR Ieee1722Tp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("relative", None, True, False, None),  # relative
        ("stream_identifier", None, True, False, None),  # streamIdentifier
        ("sub_type", None, True, False, None),  # subType
        ("version", None, True, False, None),  # version
    ]

    def __init__(self) -> None:
        """Initialize Ieee1722Tp."""
        super().__init__()
        self.relative: Optional[TimeValue] = None
        self.stream_identifier: Optional[PositiveInteger] = None
        self.sub_type: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Ieee1722Tp to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ieee1722Tp":
        """Create Ieee1722Tp from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Ieee1722Tp instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Ieee1722Tp since parent returns ARObject
        return cast("Ieee1722Tp", obj)


class Ieee1722TpBuilder:
    """Builder for Ieee1722Tp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ieee1722Tp = Ieee1722Tp()

    def build(self) -> Ieee1722Tp:
        """Build and return Ieee1722Tp object.

        Returns:
            Ieee1722Tp instance
        """
        # TODO: Add validation
        return self._obj
