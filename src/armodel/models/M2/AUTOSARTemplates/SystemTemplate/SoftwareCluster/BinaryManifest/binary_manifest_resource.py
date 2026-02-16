"""BinaryManifestResource AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class BinaryManifestResource(Identifiable):
    """AUTOSAR BinaryManifestResource."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("global_resource", None, True, False, None),  # globalResource
        ("resource", None, False, False, any (BinaryManifest)),  # resource
        ("resource_guard", None, True, False, None),  # resourceGuard
    ]

    def __init__(self) -> None:
        """Initialize BinaryManifestResource."""
        super().__init__()
        self.global_resource: Optional[PositiveInteger] = None
        self.resource: Optional[Any] = None
        self.resource_guard: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BinaryManifestResource to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestResource":
        """Create BinaryManifestResource from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BinaryManifestResource instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BinaryManifestResource since parent returns ARObject
        return cast("BinaryManifestResource", obj)


class BinaryManifestResourceBuilder:
    """Builder for BinaryManifestResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestResource = BinaryManifestResource()

    def build(self) -> BinaryManifestResource:
        """Build and return BinaryManifestResource object.

        Returns:
            BinaryManifestResource instance
        """
        # TODO: Add validation
        return self._obj
