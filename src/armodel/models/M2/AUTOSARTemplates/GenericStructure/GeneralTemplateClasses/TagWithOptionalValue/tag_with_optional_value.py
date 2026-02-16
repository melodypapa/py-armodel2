"""TagWithOptionalValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)


class TagWithOptionalValue(ARObject):
    """AUTOSAR TagWithOptionalValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("key", None, True, False, None),  # key
        ("sequence_offset", None, True, False, None),  # sequenceOffset
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize TagWithOptionalValue."""
        super().__init__()
        self.key: Optional[String] = None
        self.sequence_offset: Optional[Integer] = None
        self.value: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TagWithOptionalValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TagWithOptionalValue":
        """Create TagWithOptionalValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TagWithOptionalValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TagWithOptionalValue since parent returns ARObject
        return cast("TagWithOptionalValue", obj)


class TagWithOptionalValueBuilder:
    """Builder for TagWithOptionalValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TagWithOptionalValue = TagWithOptionalValue()

    def build(self) -> TagWithOptionalValue:
        """Build and return TagWithOptionalValue object.

        Returns:
            TagWithOptionalValue instance
        """
        # TODO: Add validation
        return self._obj
