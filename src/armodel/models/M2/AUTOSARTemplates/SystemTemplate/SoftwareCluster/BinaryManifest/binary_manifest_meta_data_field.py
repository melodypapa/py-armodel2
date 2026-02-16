"""BinaryManifestMetaDataField AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_addressable_object import (
    BinaryManifestAddressableObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    VerbatimString,
)


class BinaryManifestMetaDataField(BinaryManifestAddressableObject):
    """AUTOSAR BinaryManifestMetaDataField."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("size", None, True, False, None),  # size
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize BinaryManifestMetaDataField."""
        super().__init__()
        self.size: Optional[PositiveInteger] = None
        self.value: Optional[VerbatimString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BinaryManifestMetaDataField to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestMetaDataField":
        """Create BinaryManifestMetaDataField from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BinaryManifestMetaDataField instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BinaryManifestMetaDataField since parent returns ARObject
        return cast("BinaryManifestMetaDataField", obj)


class BinaryManifestMetaDataFieldBuilder:
    """Builder for BinaryManifestMetaDataField."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestMetaDataField = BinaryManifestMetaDataField()

    def build(self) -> BinaryManifestMetaDataField:
        """Build and return BinaryManifestMetaDataField object.

        Returns:
            BinaryManifestMetaDataField instance
        """
        # TODO: Add validation
        return self._obj
