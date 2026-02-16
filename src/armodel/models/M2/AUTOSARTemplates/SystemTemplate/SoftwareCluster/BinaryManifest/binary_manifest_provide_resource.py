"""BinaryManifestProvideResource AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_resource import (
    BinaryManifestResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class BinaryManifestProvideResource(BinaryManifestResource):
    """AUTOSAR BinaryManifestProvideResource."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("number_of", None, True, False, None),  # numberOf
        ("supports", None, True, False, None),  # supports
    ]

    def __init__(self) -> None:
        """Initialize BinaryManifestProvideResource."""
        super().__init__()
        self.number_of: Optional[PositiveInteger] = None
        self.supports: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BinaryManifestProvideResource to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestProvideResource":
        """Create BinaryManifestProvideResource from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BinaryManifestProvideResource instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BinaryManifestProvideResource since parent returns ARObject
        return cast("BinaryManifestProvideResource", obj)


class BinaryManifestProvideResourceBuilder:
    """Builder for BinaryManifestProvideResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestProvideResource = BinaryManifestProvideResource()

    def build(self) -> BinaryManifestProvideResource:
        """Build and return BinaryManifestProvideResource object.

        Returns:
            BinaryManifestProvideResource instance
        """
        # TODO: Add validation
        return self._obj
