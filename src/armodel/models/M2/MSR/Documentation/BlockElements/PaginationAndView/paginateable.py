"""Paginateable AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.document_view_selectable import (
    DocumentViewSelectable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.chapter_enum_break import (
    ChapterEnumBreak,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.keep_with_previous_enum import (
    KeepWithPreviousEnum,
)


class Paginateable(DocumentViewSelectable):
    """AUTOSAR Paginateable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("break_", 'BREAK', False, False, ChapterEnumBreak),  # break
        ("keep_with", None, False, False, KeepWithPreviousEnum),  # keepWith
    ]

    def __init__(self) -> None:
        """Initialize Paginateable."""
        super().__init__()
        self.break_: Optional[ChapterEnumBreak] = None
        self.keep_with: Optional[KeepWithPreviousEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Paginateable to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Paginateable":
        """Create Paginateable from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Paginateable instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Paginateable since parent returns ARObject
        return cast("Paginateable", obj)


class PaginateableBuilder:
    """Builder for Paginateable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Paginateable = Paginateable()

    def build(self) -> Paginateable:
        """Build and return Paginateable object.

        Returns:
            Paginateable instance
        """
        # TODO: Add validation
        return self._obj
