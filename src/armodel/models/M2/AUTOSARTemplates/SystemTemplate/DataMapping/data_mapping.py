"""DataMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class DataMapping(ARObject):
    """AUTOSAR DataMapping."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("introduction", None, False, False, DocumentationBlock),  # introduction
    ]

    def __init__(self) -> None:
        """Initialize DataMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataMapping":
        """Create DataMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataMapping since parent returns ARObject
        return cast("DataMapping", obj)


class DataMappingBuilder:
    """Builder for DataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataMapping = DataMapping()

    def build(self) -> DataMapping:
        """Build and return DataMapping object.

        Returns:
            DataMapping instance
        """
        # TODO: Add validation
        return self._obj
