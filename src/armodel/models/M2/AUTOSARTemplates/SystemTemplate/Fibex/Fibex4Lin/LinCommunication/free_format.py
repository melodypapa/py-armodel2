"""FreeFormat AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.free_format_entry import (
    FreeFormatEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class FreeFormat(FreeFormatEntry):
    """AUTOSAR FreeFormat."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("byte_values", None, False, True, None),  # byteValues
    ]

    def __init__(self) -> None:
        """Initialize FreeFormat."""
        super().__init__()
        self.byte_values: list[Integer] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FreeFormat to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FreeFormat":
        """Create FreeFormat from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FreeFormat instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FreeFormat since parent returns ARObject
        return cast("FreeFormat", obj)


class FreeFormatBuilder:
    """Builder for FreeFormat."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FreeFormat = FreeFormat()

    def build(self) -> FreeFormat:
        """Build and return FreeFormat object.

        Returns:
            FreeFormat instance
        """
        # TODO: Add validation
        return self._obj
