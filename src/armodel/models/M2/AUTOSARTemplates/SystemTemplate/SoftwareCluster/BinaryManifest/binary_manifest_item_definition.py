"""BinaryManifestItemDefinition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
    BinaryManifestItem,
)


class BinaryManifestItemDefinition(Identifiable):
    """AUTOSAR BinaryManifestItemDefinition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("auxiliary_fields", None, False, True, BinaryManifestItem),  # auxiliaryFields
        ("is_optional", None, True, False, None),  # isOptional
        ("size", None, True, False, None),  # size
    ]

    def __init__(self) -> None:
        """Initialize BinaryManifestItemDefinition."""
        super().__init__()
        self.auxiliary_fields: list[BinaryManifestItem] = []
        self.is_optional: Optional[Boolean] = None
        self.size: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BinaryManifestItemDefinition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItemDefinition":
        """Create BinaryManifestItemDefinition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BinaryManifestItemDefinition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BinaryManifestItemDefinition since parent returns ARObject
        return cast("BinaryManifestItemDefinition", obj)


class BinaryManifestItemDefinitionBuilder:
    """Builder for BinaryManifestItemDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemDefinition = BinaryManifestItemDefinition()

    def build(self) -> BinaryManifestItemDefinition:
        """Build and return BinaryManifestItemDefinition object.

        Returns:
            BinaryManifestItemDefinition instance
        """
        # TODO: Add validation
        return self._obj
