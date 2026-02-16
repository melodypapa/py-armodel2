"""BinaryManifestItemNumericalValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_value import (
    BinaryManifestItemValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class BinaryManifestItemNumericalValue(BinaryManifestItemValue):
    """AUTOSAR BinaryManifestItemNumericalValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize BinaryManifestItemNumericalValue."""
        super().__init__()
        self.value: Optional[Numerical] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BinaryManifestItemNumericalValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItemNumericalValue":
        """Create BinaryManifestItemNumericalValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BinaryManifestItemNumericalValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BinaryManifestItemNumericalValue since parent returns ARObject
        return cast("BinaryManifestItemNumericalValue", obj)


class BinaryManifestItemNumericalValueBuilder:
    """Builder for BinaryManifestItemNumericalValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemNumericalValue = BinaryManifestItemNumericalValue()

    def build(self) -> BinaryManifestItemNumericalValue:
        """Build and return BinaryManifestItemNumericalValue object.

        Returns:
            BinaryManifestItemNumericalValue instance
        """
        # TODO: Add validation
        return self._obj
