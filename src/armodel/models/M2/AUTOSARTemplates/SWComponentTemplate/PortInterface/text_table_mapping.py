"""TextTableMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_value_pair import (
    TextTableValuePair,
)


class TextTableMapping(ARObject):
    """AUTOSAR TextTableMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bitfield_text_table", None, True, False, None),  # bitfieldTextTable
        ("identical", None, True, False, None),  # identical
        ("mapping", None, False, False, MappingDirectionEnum),  # mapping
        ("value_pairs", None, False, True, TextTableValuePair),  # valuePairs
    ]

    def __init__(self) -> None:
        """Initialize TextTableMapping."""
        super().__init__()
        self.bitfield_text_table: Optional[PositiveInteger] = None
        self.identical: Optional[Boolean] = None
        self.mapping: Optional[MappingDirectionEnum] = None
        self.value_pairs: list[TextTableValuePair] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TextTableMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextTableMapping":
        """Create TextTableMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TextTableMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TextTableMapping since parent returns ARObject
        return cast("TextTableMapping", obj)


class TextTableMappingBuilder:
    """Builder for TextTableMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextTableMapping = TextTableMapping()

    def build(self) -> TextTableMapping:
        """Build and return TextTableMapping object.

        Returns:
            TextTableMapping instance
        """
        # TODO: Add validation
        return self._obj
