"""SenderRecArrayTypeMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SenderRecArrayTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecArrayTypeMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("array_elements", None, False, True, any (SenderRecArray)),  # arrayElements
        ("sender_to_signal", None, False, False, TextTableMapping),  # senderToSignal
        ("signal_to", None, False, False, TextTableMapping),  # signalTo
    ]

    def __init__(self) -> None:
        """Initialize SenderRecArrayTypeMapping."""
        super().__init__()
        self.array_elements: list[Any] = []
        self.sender_to_signal: Optional[TextTableMapping] = None
        self.signal_to: Optional[TextTableMapping] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SenderRecArrayTypeMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecArrayTypeMapping":
        """Create SenderRecArrayTypeMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SenderRecArrayTypeMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SenderRecArrayTypeMapping since parent returns ARObject
        return cast("SenderRecArrayTypeMapping", obj)


class SenderRecArrayTypeMappingBuilder:
    """Builder for SenderRecArrayTypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecArrayTypeMapping = SenderRecArrayTypeMapping()

    def build(self) -> SenderRecArrayTypeMapping:
        """Build and return SenderRecArrayTypeMapping object.

        Returns:
            SenderRecArrayTypeMapping instance
        """
        # TODO: Add validation
        return self._obj
