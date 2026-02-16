"""SectionNamePrefix AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)


class SectionNamePrefix(ImplementationProps):
    """AUTOSAR SectionNamePrefix."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("implemented_in", None, False, False, DependencyOnArtifact),  # implementedIn
    ]

    def __init__(self) -> None:
        """Initialize SectionNamePrefix."""
        super().__init__()
        self.implemented_in: Optional[DependencyOnArtifact] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SectionNamePrefix to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SectionNamePrefix":
        """Create SectionNamePrefix from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SectionNamePrefix instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SectionNamePrefix since parent returns ARObject
        return cast("SectionNamePrefix", obj)


class SectionNamePrefixBuilder:
    """Builder for SectionNamePrefix."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SectionNamePrefix = SectionNamePrefix()

    def build(self) -> SectionNamePrefix:
        """Build and return SectionNamePrefix object.

        Returns:
            SectionNamePrefix instance
        """
        # TODO: Add validation
        return self._obj
