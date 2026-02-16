"""SomeipServiceVersion AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SomeipServiceVersion(ARObject):
    """AUTOSAR SomeipServiceVersion."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("major_version", None, True, False, None),  # majorVersion
        ("minor_version", None, True, False, None),  # minorVersion
    ]

    def __init__(self) -> None:
        """Initialize SomeipServiceVersion."""
        super().__init__()
        self.major_version: Optional[PositiveInteger] = None
        self.minor_version: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SomeipServiceVersion to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipServiceVersion":
        """Create SomeipServiceVersion from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SomeipServiceVersion instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SomeipServiceVersion since parent returns ARObject
        return cast("SomeipServiceVersion", obj)


class SomeipServiceVersionBuilder:
    """Builder for SomeipServiceVersion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipServiceVersion = SomeipServiceVersion()

    def build(self) -> SomeipServiceVersion:
        """Build and return SomeipServiceVersion object.

        Returns:
            SomeipServiceVersion instance
        """
        # TODO: Add validation
        return self._obj
