"""PduToFrameMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)


class PduToFrameMapping(ARObject):
    """AUTOSAR PduToFrameMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("packing_byte", None, False, False, ByteOrderEnum),  # packingByte
        ("pdu", None, False, False, Pdu),  # pdu
        ("start_position", None, True, False, None),  # startPosition
        ("update", None, True, False, None),  # update
    ]

    def __init__(self) -> None:
        """Initialize PduToFrameMapping."""
        super().__init__()
        self.packing_byte: Optional[ByteOrderEnum] = None
        self.pdu: Optional[Pdu] = None
        self.start_position: Optional[Integer] = None
        self.update: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PduToFrameMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduToFrameMapping":
        """Create PduToFrameMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PduToFrameMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PduToFrameMapping since parent returns ARObject
        return cast("PduToFrameMapping", obj)


class PduToFrameMappingBuilder:
    """Builder for PduToFrameMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduToFrameMapping = PduToFrameMapping()

    def build(self) -> PduToFrameMapping:
        """Build and return PduToFrameMapping object.

        Returns:
            PduToFrameMapping instance
        """
        # TODO: Add validation
        return self._obj
