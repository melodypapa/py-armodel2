"""EndToEndDescription AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class EndToEndDescription(ARObject):
    """AUTOSAR EndToEndDescription."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("category", None, True, False, None),  # category
        ("counter_offset", None, True, False, None),  # counterOffset
        ("crc_offset", None, True, False, None),  # crcOffset
        ("data_id_mode", None, True, False, None),  # dataIdMode
        ("data_id_nibble", None, True, False, None),  # dataIdNibble
        ("data_length", None, True, False, None),  # dataLength
        ("max_delta", None, True, False, None),  # maxDelta
    ]

    def __init__(self) -> None:
        """Initialize EndToEndDescription."""
        super().__init__()
        self.category: Optional[NameToken] = None
        self.counter_offset: Optional[PositiveInteger] = None
        self.crc_offset: Optional[PositiveInteger] = None
        self.data_id_mode: Optional[PositiveInteger] = None
        self.data_id_nibble: Optional[PositiveInteger] = None
        self.data_length: Optional[PositiveInteger] = None
        self.max_delta: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EndToEndDescription to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndDescription":
        """Create EndToEndDescription from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EndToEndDescription instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EndToEndDescription since parent returns ARObject
        return cast("EndToEndDescription", obj)


class EndToEndDescriptionBuilder:
    """Builder for EndToEndDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndDescription = EndToEndDescription()

    def build(self) -> EndToEndDescription:
        """Build and return EndToEndDescription object.

        Returns:
            EndToEndDescription instance
        """
        # TODO: Add validation
        return self._obj
