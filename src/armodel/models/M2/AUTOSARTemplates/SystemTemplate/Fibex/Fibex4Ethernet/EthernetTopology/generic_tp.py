"""GenericTp AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class GenericTp(TransportProtocolConfiguration):
    """AUTOSAR GenericTp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tp_address", None, True, False, None),  # tpAddress
        ("tp_technology", None, True, False, None),  # tpTechnology
    ]

    def __init__(self) -> None:
        """Initialize GenericTp."""
        super().__init__()
        self.tp_address: Optional[String] = None
        self.tp_technology: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GenericTp to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GenericTp":
        """Create GenericTp from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GenericTp instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GenericTp since parent returns ARObject
        return cast("GenericTp", obj)


class GenericTpBuilder:
    """Builder for GenericTp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GenericTp = GenericTp()

    def build(self) -> GenericTp:
        """Build and return GenericTp object.

        Returns:
            GenericTp instance
        """
        # TODO: Add validation
        return self._obj
