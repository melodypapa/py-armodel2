"""BinaryManifestRequireResource AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_resource import (
    BinaryManifestResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class BinaryManifestRequireResource(BinaryManifestResource):
    """AUTOSAR BinaryManifestRequireResource."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("connection_is", None, True, False, None),  # connectionIs
    ]

    def __init__(self) -> None:
        """Initialize BinaryManifestRequireResource."""
        super().__init__()
        self.connection_is: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BinaryManifestRequireResource to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestRequireResource":
        """Create BinaryManifestRequireResource from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BinaryManifestRequireResource instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BinaryManifestRequireResource since parent returns ARObject
        return cast("BinaryManifestRequireResource", obj)


class BinaryManifestRequireResourceBuilder:
    """Builder for BinaryManifestRequireResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestRequireResource = BinaryManifestRequireResource()

    def build(self) -> BinaryManifestRequireResource:
        """Build and return BinaryManifestRequireResource object.

        Returns:
            BinaryManifestRequireResource instance
        """
        # TODO: Add validation
        return self._obj
