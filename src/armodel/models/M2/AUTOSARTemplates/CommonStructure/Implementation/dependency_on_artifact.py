"""DependencyOnArtifact AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)


class DependencyOnArtifact(Identifiable):
    """AUTOSAR DependencyOnArtifact."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("artifact", None, False, False, AutosarEngineeringObject),  # artifact
        ("usages", None, False, True, DependencyUsageEnum),  # usages
    ]

    def __init__(self) -> None:
        """Initialize DependencyOnArtifact."""
        super().__init__()
        self.artifact: Optional[AutosarEngineeringObject] = None
        self.usages: list[DependencyUsageEnum] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DependencyOnArtifact to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DependencyOnArtifact":
        """Create DependencyOnArtifact from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DependencyOnArtifact instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DependencyOnArtifact since parent returns ARObject
        return cast("DependencyOnArtifact", obj)


class DependencyOnArtifactBuilder:
    """Builder for DependencyOnArtifact."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DependencyOnArtifact = DependencyOnArtifact()

    def build(self) -> DependencyOnArtifact:
        """Build and return DependencyOnArtifact object.

        Returns:
            DependencyOnArtifact instance
        """
        # TODO: Add validation
        return self._obj
