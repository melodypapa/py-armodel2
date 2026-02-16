"""BinaryManifestItemValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class BinaryManifestItemValue(ARObject):
    """AUTOSAR BinaryManifestItemValue."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize BinaryManifestItemValue."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BinaryManifestItemValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItemValue":
        """Create BinaryManifestItemValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BinaryManifestItemValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BinaryManifestItemValue since parent returns ARObject
        return cast("BinaryManifestItemValue", obj)


class BinaryManifestItemValueBuilder:
    """Builder for BinaryManifestItemValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemValue = BinaryManifestItemValue()

    def build(self) -> BinaryManifestItemValue:
        """Build and return BinaryManifestItemValue object.

        Returns:
            BinaryManifestItemValue instance
        """
        # TODO: Add validation
        return self._obj
