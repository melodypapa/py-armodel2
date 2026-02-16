"""FileInfoComment AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class FileInfoComment(ARObject):
    """AUTOSAR FileInfoComment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sdgs", None, False, True, Sdg),  # sdgs
    ]

    def __init__(self) -> None:
        """Initialize FileInfoComment."""
        super().__init__()
        self.sdgs: list[Sdg] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FileInfoComment to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FileInfoComment":
        """Create FileInfoComment from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FileInfoComment instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FileInfoComment since parent returns ARObject
        return cast("FileInfoComment", obj)


class FileInfoCommentBuilder:
    """Builder for FileInfoComment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FileInfoComment = FileInfoComment()

    def build(self) -> FileInfoComment:
        """Build and return FileInfoComment object.

        Returns:
            FileInfoComment instance
        """
        # TODO: Add validation
        return self._obj
