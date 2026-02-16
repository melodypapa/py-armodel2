"""BinaryManifestItem AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_addressable_object import (
    BinaryManifestAddressableObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
    BinaryManifestItem,
)


class BinaryManifestItem(BinaryManifestAddressableObject):
    """AUTOSAR BinaryManifestItem."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("auxiliary_fields", None, False, True, BinaryManifestItem),  # auxiliaryFields
        ("default_value", None, False, False, BinaryManifestItem),  # defaultValue
        ("is_unused", None, True, False, None),  # isUnused
        ("value", None, False, False, BinaryManifestItem),  # value
    ]

    def __init__(self) -> None:
        """Initialize BinaryManifestItem."""
        super().__init__()
        self.auxiliary_fields: list[BinaryManifestItem] = []
        self.default_value: Optional[BinaryManifestItem] = None
        self.is_unused: Optional[Boolean] = None
        self.value: Optional[BinaryManifestItem] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BinaryManifestItem to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItem":
        """Create BinaryManifestItem from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BinaryManifestItem instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BinaryManifestItem since parent returns ARObject
        return cast("BinaryManifestItem", obj)


class BinaryManifestItemBuilder:
    """Builder for BinaryManifestItem."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItem = BinaryManifestItem()

    def build(self) -> BinaryManifestItem:
        """Build and return BinaryManifestItem object.

        Returns:
            BinaryManifestItem instance
        """
        # TODO: Add validation
        return self._obj
