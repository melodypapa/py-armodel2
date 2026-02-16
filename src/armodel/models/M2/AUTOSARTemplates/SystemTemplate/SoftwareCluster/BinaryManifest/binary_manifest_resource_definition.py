"""BinaryManifestResourceDefinition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
    BinaryManifestItem,
)


class BinaryManifestResourceDefinition(Identifiable):
    """AUTOSAR BinaryManifestResourceDefinition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("item_definitions", None, False, True, BinaryManifestItem),  # itemDefinitions
    ]

    def __init__(self) -> None:
        """Initialize BinaryManifestResourceDefinition."""
        super().__init__()
        self.item_definitions: list[BinaryManifestItem] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BinaryManifestResourceDefinition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestResourceDefinition":
        """Create BinaryManifestResourceDefinition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BinaryManifestResourceDefinition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BinaryManifestResourceDefinition since parent returns ARObject
        return cast("BinaryManifestResourceDefinition", obj)


class BinaryManifestResourceDefinitionBuilder:
    """Builder for BinaryManifestResourceDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestResourceDefinition = BinaryManifestResourceDefinition()

    def build(self) -> BinaryManifestResourceDefinition:
        """Build and return BinaryManifestResourceDefinition object.

        Returns:
            BinaryManifestResourceDefinition instance
        """
        # TODO: Add validation
        return self._obj
